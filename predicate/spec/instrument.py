import sys
from functools import wraps
from inspect import signature, unwrap
from typing import Any, Callable

from predicate import explain
from predicate.is_async_predicate import is_async_p
from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import get_return_predicate
from predicate.spec.spec import Spec


def enrich_spec(func: Callable, spec: Spec) -> Spec:
    if spec.get("ret"):
        return spec
    sig = signature(func)
    if sig.return_annotation == sig.empty:
        return spec
    return spec | {"ret": get_return_predicate(sig)}


def _get_reason(predicate: Predicate, value: Any) -> str | None:
    if predicate(value):
        return None
    result = explain(predicate, value)
    return result.get("reason") or str(result)


def _check_args(spec: Spec, func_name: str, arguments: dict) -> None:
    for name, predicate in spec["args"].items():
        if name in arguments:
            if reason := _get_reason(predicate, value=arguments[name]):
                raise ValueError(f"Parameter predicate for function {func_name} failed. Reason: {reason}")


def _check_return_value(spec: Spec, func_name: str, result: Any) -> None:
    if return_p := spec.get("ret"):
        if reason := _get_reason(return_p, value=result):
            raise ValueError(f"Return predicate for function {func_name} failed. Reason: {reason}")


def _check_constraints(spec: Spec, func_name: str, arguments: dict, result: Any) -> None:
    if fn := spec.get("fn"):
        if not fn(**arguments, ret=result):
            raise ValueError(f"fn constraint for function {func_name} failed.")

    if fn_p := spec.get("fn_p"):
        p = fn_p(**arguments)
        if reason := _get_reason(p, value=result):
            raise ValueError(f"fn_p constraint for function {func_name} failed. Reason: {reason}")


def instrument_function(func: Callable, spec: Spec) -> Callable:
    func = unwrap(func)
    func_name = func.__name__
    spec = enrich_spec(func, spec)

    if is_async_p(func):

        @wraps(func)
        async def wrapped(*args, **kwargs):
            bound = signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            arguments = bound.arguments
            _check_args(spec, func_name, arguments)

            result = await func(*args, **kwargs)

            _check_return_value(spec, func_name, result)

            _check_constraints(spec, func_name, arguments, result)

            return result
    else:

        @wraps(func)
        def wrapped(*args, **kwargs):
            bound = signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            arguments = bound.arguments
            _check_args(spec, func_name, arguments)

            result = func(*args, **kwargs)

            _check_return_value(spec, func_name, result)

            _check_constraints(spec, func_name, arguments, result)

            return result

    wrapped.__spec__ = spec  # type: ignore

    module_name = func.__module__
    module = sys.modules.get(module_name)

    if module and hasattr(module, func_name):
        setattr(module, func_name, wrapped)

    return wrapped


def instrument(spec: Spec) -> Callable:
    def decorator(func: Callable) -> Callable:
        return instrument_function(func, spec)

    return decorator
