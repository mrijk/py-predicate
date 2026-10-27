from inspect import Parameter
from typing import AsyncIterator, Callable, Iterator, TypeVar, get_origin

from predicate import always_true_p, is_instance_p
from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import (
    call_args,
    check_exception,
    check_signature_against_spec,
    generate_values,
    get_return_predicate,
    no_spec_error,
    param_predicate,
    resolved_signature,
    verify_result,
)
from predicate.spec.spec import Spec


def get_spec_from_class_annotation(f: Callable) -> Spec:
    sig = resolved_signature(f.__call__)  # type: ignore
    name = type(f).__name__

    if sig.return_annotation == sig.empty:
        raise no_spec_error(name, "missing return annotation")

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    parameters = {key: sig.parameters[key] for key in sig.parameters if key != "self"}

    for key in parameters:
        parameter = parameters[key]
        annotation = parameter.annotation

        if annotation == parameter.empty:
            if parameter.kind == Parameter.VAR_POSITIONAL:
                continue

            if parameter.kind == Parameter.VAR_KEYWORD:
                continue

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
            spec["args"][key] = param_predicate(parameter)

    return spec


def _resolve_class_spec(f: Callable, spec: Spec | None) -> Spec:
    if not spec:
        return get_spec_from_class_annotation(f)
    return check_signature_against_spec(f, spec)


def exercise_class(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    spec = _resolve_class_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f.__call__)  # type: ignore

    for value in values:
        args, kwargs = call_args(sig, value)
        try:
            result = f(*args, **kwargs)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result


async def async_exercise_class(f: Callable, spec: Spec | None, n: int) -> AsyncIterator[tuple]:
    spec = _resolve_class_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f.__call__)  # type: ignore

    for value in values:
        args, kwargs = call_args(sig, value)
        try:
            result = await f(*args, **kwargs)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result
