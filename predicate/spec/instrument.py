import sys
from functools import wraps
from inspect import signature, unwrap
from typing import Any, Callable

from predicate import explain
from predicate.predicate import Predicate
from predicate.spec.spec import Spec


def _get_reason(predicate: Predicate, value: Any) -> str | None:
    return None if predicate(value) else explain(predicate, value)["reason"]


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
