from collections.abc import Mapping
from inspect import Parameter
from typing import AsyncIterator, Callable, Iterator

from more_itertools import take

from predicate.spec.exercise_helpers import (
    GENERATOR_ITEMS,
    call_args,
    callable_name,
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


def _annotatable_parameters(parameters: Mapping[str, Parameter]) -> Iterator[tuple[str, Parameter]]:
    yield from ((key, parameter) for key, parameter in parameters.items() if not is_skipped_param(parameter))


def get_spec_from_function_annotation(f: Callable) -> Spec:
    sig = resolved_signature(f)

    if sig.return_annotation == sig.empty:
        raise no_spec_error(callable_name(f), "missing return annotation")

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    for key, parameter in _annotatable_parameters(sig.parameters):
        if parameter.annotation == parameter.empty:
            raise no_spec_error(callable_name(f), f"parameter '{key}' has no annotation")
        spec["args"][key] = exercise_param_predicate(parameter)

    return spec


def _resolve_function_spec(f: Callable, spec: Spec | None) -> Spec:
    if not spec:
        return get_spec_from_function_annotation(f)
    return check_signature_against_spec(f, spec)


def exercise_function(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f)
    item_p = yield_predicate(f)

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


async def async_exercise_function(f: Callable, spec: Spec | None, n: int) -> AsyncIterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f)
    item_p = yield_predicate(f)

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
