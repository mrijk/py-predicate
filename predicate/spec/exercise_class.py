from typing import AsyncIterator, Callable, Iterator, TypeVar, get_origin

from more_itertools import take

from predicate import always_true_p, is_instance_p
from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import (
    GENERATOR_ITEMS,
    call_args,
    check_exception,
    check_signature_against_spec,
    exercise_param_predicate,
    generate_values,
    get_return_predicate,
    is_skipped_param,
    no_spec_error,
    resolved_signature,
    take_async,
    verify_items,
    verify_result,
    yield_predicate,
)
from predicate.spec.spec import Spec


def _get_spec_from_class_annotation(f: Callable) -> Spec:
    sig = resolved_signature(f.__call__)  # type: ignore
    name = type(f).__name__

    if sig.return_annotation == sig.empty:
        raise no_spec_error(name, "missing return annotation")

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    parameters = {
        key: parameter for key, parameter in sig.parameters.items() if key != "self" and not is_skipped_param(parameter)
    }

    for key in parameters:
        parameter = parameters[key]
        annotation = parameter.annotation

        if annotation == parameter.empty:
            raise no_spec_error(name, f"parameter '{key}' has no annotation")

        if isinstance(f, Predicate):
            try:
                spec["args"][key] = is_instance_p(f.klass)
            except NotImplementedError:
                origin = get_origin(annotation)
                spec["args"][key] = is_instance_p(origin) if origin is not None else always_true_p
        elif type(annotation) is TypeVar:
            spec["args"][key] = always_true_p
        else:
            spec["args"][key] = exercise_param_predicate(parameter)

    return spec


def _resolve_class_spec(f: Callable, spec: Spec | None) -> Spec:
    if not spec:
        return _get_spec_from_class_annotation(f)
    return check_signature_against_spec(f, spec)


def exercise_class(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    spec = _resolve_class_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f.__call__)  # type: ignore
    item_p = yield_predicate(f.__call__)  # type: ignore[operator]

    for value in values:
        args, kwargs = call_args(sig, value)
        try:
            result = f(*args, **kwargs)
            # A generator's body only runs when it's iterated, so take its items here (#380)
            items = take(GENERATOR_ITEMS, result) if item_p is not None else None
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        if item_p is not None and items is not None:
            verify_items(item_p, value, items)
            result = items
        yield tuple(value.values()), result


async def async_exercise_class(f: Callable, spec: Spec | None, n: int) -> AsyncIterator[tuple]:
    spec = _resolve_class_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f.__call__)  # type: ignore
    item_p = yield_predicate(f.__call__)  # type: ignore[operator]

    for value in values:
        args, kwargs = call_args(sig, value)
        try:
            if item_p is None:
                result = await f(*args, **kwargs)
                items = None
            else:
                # An async generator function isn't awaited: its items are taken, which runs its body (#380)
                result = f(*args, **kwargs)
                items = await take_async(result, GENERATOR_ITEMS)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        if item_p is not None and items is not None:
            verify_items(item_p, value, items)
            result = items
        yield tuple(value.values()), result
