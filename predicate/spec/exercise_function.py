from inspect import signature
from typing import AsyncIterator, Callable, Iterator, TypeVar

from predicate import always_true_p, is_instance_p
from predicate.spec.exercise_helpers import (
    _generate_values,
    _verify_result,
    check_signature_against_spec,
    get_return_predicate,
)
from predicate.spec.spec import Spec


def get_spec_from_function_annotation(f: Callable) -> Spec | None:
    sig = signature(f)

    if sig.return_annotation == sig.empty:
        return None

    spec: Spec = {"args": {}, "ret": get_return_predicate(sig)}

    for key in sig.parameters:
        parameter = sig.parameters[key]
        annotation = parameter.annotation

        if annotation == parameter.empty:
            return None
        if type(annotation) is TypeVar:
            spec["args"][key] = always_true_p
        else:
            spec["args"][key] = is_instance_p(annotation)

    return spec


def _resolve_function_spec(f: Callable, spec: Spec | None) -> Spec:
    if not spec:
        if not (spec_from_annotation := get_spec_from_function_annotation(f)):
            raise ValueError("Not implemented yet")
        return spec_from_annotation
    check_signature_against_spec(f, spec)
    return spec


def exercise_function(f: Callable, spec: Spec | None, n: int) -> Iterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = _generate_values(spec, n)

    for value in values:
        result = f(**value)
        _verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result


async def async_exercise_function(f: Callable, spec: Spec | None, n: int) -> AsyncIterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = _generate_values(spec, n)

    for value in values:
        result = await f(**value)
        _verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result
