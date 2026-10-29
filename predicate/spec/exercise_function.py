from collections.abc import Mapping
from inspect import Parameter
from typing import AsyncIterator, Callable, Iterator

from predicate.spec.exercise_helpers import (
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
    verify_result,
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

    for value in values:
        args, kwargs = call_args(sig, value)
        try:
            result = f(*args, **kwargs)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result


async def async_exercise_function(f: Callable, spec: Spec | None, n: int) -> AsyncIterator[tuple]:
    spec = _resolve_function_spec(f, spec)
    return_p, values = generate_values(spec, n)
    sig = resolved_signature(f)

    for value in values:
        args, kwargs = call_args(sig, value)
        try:
            result = await f(*args, **kwargs)
        except Exception as exc:
            yield tuple(value.values()), check_exception(spec, value, exc)
            continue
        verify_result(spec, return_p, value, result)
        yield tuple(value.values()), result
