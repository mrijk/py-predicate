from typing import AsyncIterator, Callable, Iterator, TypeVar

from predicate import always_true_p, is_instance_p
from predicate.spec.exercise_helpers import (
    check_exception,
    check_signature_against_spec,
    generate_values,
    get_return_predicate,
    no_spec_error,
    resolved_signature,
    verify_result,
)
from predicate.spec.spec import Spec


def get_spec_from_function_annotation(f: Callable) -> Spec:
    sig = resolved_signature(f)

    if sig.return_annotation == sig.empty:
        raise no_spec_error(f.__name__, "missing return annotation")

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    for key in sig.parameters:
        parameter = sig.parameters[key]
        annotation = parameter.annotation

        if annotation == parameter.empty:
            raise no_spec_error(f.__name__, f"parameter '{key}' has no annotation")
        if type(annotation) is TypeVar:
            spec["args"][key] = always_true_p
        else:
            spec["args"][key] = is_instance_p(annotation)

    return spec


def _resolve_function_spec(f: Callable, spec: Spec | None) -> Spec:
    if not spec:
        return get_spec_from_function_annotation(f)
    return check_signature_against_spec(f, spec)


def exercise_function(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = generate_values(spec, n)

    for value in values:
        try:
            result = f(**value)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result


async def async_exercise_function(f: Callable, spec: Spec | None, n: int) -> AsyncIterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = generate_values(spec, n)

    for value in values:
        try:
            result = await f(**value)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result
