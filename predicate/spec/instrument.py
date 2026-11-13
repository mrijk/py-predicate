from fnmatch import fnmatch
from inspect import getmembers, isclass, isfunction
from types import ModuleType
from typing import Any, Callable

from more_itertools import consume, side_effect

from predicate.spec.instrument_class import instrument_class
from predicate.spec.instrument_function import (
    OnError,
    default_on_error,
    instrument_function,
    # noqa: F401
    # noqa: F401
)
from predicate.spec.spec import EMPTY_SPEC, Spec


def instrument(
    spec_or_func: Spec | Callable[..., Any] = None,  # type: ignore[assignment]
    *,
    on_error: OnError = default_on_error,
) -> Callable[..., Any]:
    if isclass(spec_or_func):
        instrument_class(spec_or_func, on_error=on_error)
        return spec_or_func

    if callable(spec_or_func):
        return instrument_function(spec_or_func, EMPTY_SPEC, on_error)

    spec = spec_or_func or EMPTY_SPEC

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        if isclass(func):
            instrument_class(func, on_error=on_error)
            return func
        return instrument_function(func, spec, on_error)

    return decorator


def _include_in_module(func: Callable[..., Any], module: ModuleType, pattern: str | None) -> bool:
    return func.__module__ == module.__name__ and (pattern is None or fnmatch(func.__name__, pattern))


def instrument_module(module: ModuleType, pattern: str | None = None, on_error: OnError = default_on_error) -> None:
    funcs = [func for _, func in getmembers(module, isfunction) if _include_in_module(func, module, pattern)]
    consume(side_effect(lambda func: instrument_function(func, EMPTY_SPEC, on_error), funcs))
