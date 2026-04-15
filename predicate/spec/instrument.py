import sys
from fnmatch import fnmatch
from functools import wraps
from inspect import getmembers, isfunction, signature, unwrap
from types import ModuleType
from typing import Any, Callable

from more_itertools import consume, side_effect

from predicate.explain import explain
from predicate.is_async_predicate import is_async_p
from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import annotation_to_predicate, get_return_predicate
from predicate.spec.spec import Spec


def enrich_spec(func: Callable, spec: Spec) -> Spec:
    sig = signature(func)

    args = dict(spec["args"])
    for name, param in sig.parameters.items():
        if name not in args and param.annotation is not param.empty:
            args[name] = annotation_to_predicate(param.annotation)

    enriched = spec | {"args": args}

    if not enriched.get("ret") and sig.return_annotation is not sig.empty:
        enriched = enriched | {"ret": get_return_predicate(sig)}

    return enriched


OnError = Callable[[str], None]


def _default_on_error(message: str) -> None:
    raise ValueError(message)


def _get_reason(predicate: Predicate, value: Any) -> str | None:
    if predicate(value):
        return None
    result = explain(predicate, value)
    return result.get("reason") or str(result)


def _check_args(spec: Spec, func_name: str, arguments: dict) -> str | None:
    for name, predicate in spec["args"].items():
        if name in arguments:
            if reason := _get_reason(predicate, value=arguments[name]):
                return f"Parameter predicate for function {func_name} failed. Reason: {reason}"
    return None


def _check_return_value(spec: Spec, func_name: str, result: Any) -> str | None:
    if return_p := spec.get("ret"):
        if reason := _get_reason(return_p, value=result):
            return f"Return predicate for function {func_name} failed. Reason: {reason}"
    return None


def _check_exception(spec: Spec, func_name: str, exc: Exception) -> str | None:
    if expected := spec.get("raises"):
        if not isinstance(exc, expected):
            return f"Unexpected exception {type(exc).__name__} for function {func_name}"
        return None
    return None


def _check_constraints(spec: Spec, func_name: str, arguments: dict, result: Any) -> str | None:
    if fn := spec.get("fn"):
        if not fn(**arguments, ret=result):
            return f"fn constraint for function {func_name} failed."

    if fn_p := spec.get("fn_p"):
        p = fn_p(**arguments)
        if reason := _get_reason(p, value=result):
            return f"fn_p constraint for function {func_name} failed. Reason: {reason}"

    return None


def instrument_function(func: Callable, spec: Spec, on_error: OnError = _default_on_error) -> Callable:
    func = unwrap(func)
    func_name = func.__name__
    spec = enrich_spec(func, spec)

    if is_async_p(func):

        @wraps(func)
        async def wrapped(*args, **kwargs):
            bound = signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            arguments = bound.arguments
            if error := _check_args(spec, func_name, arguments):
                on_error(error)

            try:
                result = await func(*args, **kwargs)
            except Exception as exc:
                if error := _check_exception(spec, func_name, exc):
                    on_error(error)
                raise

            if error := _check_return_value(spec, func_name, result):
                on_error(error)

            if error := _check_constraints(spec, func_name, arguments, result):
                on_error(error)

            return result
    else:

        @wraps(func)
        def wrapped(*args, **kwargs):
            bound = signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            arguments = bound.arguments
            if error := _check_args(spec, func_name, arguments):
                on_error(error)

            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                if error := _check_exception(spec, func_name, exc):
                    on_error(error)
                raise

            if error := _check_return_value(spec, func_name, result):
                on_error(error)

            if error := _check_constraints(spec, func_name, arguments, result):
                on_error(error)

            return result

    wrapped.__spec__ = spec  # type: ignore

    module_name = func.__module__
    module = sys.modules.get(module_name)

    if module and hasattr(module, func_name):
        setattr(module, func_name, wrapped)

    return wrapped


def instrument(spec_or_func: Spec | Callable = None, *, on_error: OnError = _default_on_error) -> Callable:  # type: ignore[assignment]
    empty_spec: Spec = {"args": {}}

    if callable(spec_or_func):
        return instrument_function(spec_or_func, empty_spec, on_error)

    spec = spec_or_func or empty_spec

    def decorator(func: Callable) -> Callable:
        return instrument_function(func, spec, on_error)

    return decorator


def _include_in_module(func: Callable, module: ModuleType, pattern: str | None) -> bool:
    return func.__module__ == module.__name__ and (pattern is None or fnmatch(func.__name__, pattern))


def instrument_module(module: ModuleType, pattern: str | None = None, on_error: OnError = _default_on_error) -> None:
    empty_spec: Spec = {"args": {}}
    funcs = [func for _, func in getmembers(module, isfunction) if _include_in_module(func, module, pattern)]
    consume(side_effect(lambda func: instrument_function(func, empty_spec, on_error), funcs))
