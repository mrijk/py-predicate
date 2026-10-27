import os
import sys
from fnmatch import fnmatch
from functools import cache, wraps
from inspect import getmembers, isclass, isfunction, signature, unwrap
from types import ModuleType
from typing import Any, Callable

from more_itertools import consume, first_true, side_effect

from predicate.explain import explain
from predicate.is_async_predicate import is_async_p
from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import (
    check_ret_name,
    get_return_predicate,
    param_predicate,
    resolved_signature,
    ret_name,
)
from predicate.spec.spec import Spec, SpecViolationError


def _enabled_from_environment(value: str | None) -> bool:
    return (value or "").strip().lower() not in {"0", "false", "no", "off"}


_enabled = _enabled_from_environment(os.environ.get("PREDICATE_INSTRUMENT"))


def set_instrumentation(enabled: bool) -> None:
    """Turn the checks of all instrumented functions on or off; when off they call the original function directly."""
    global _enabled
    _enabled = enabled


def is_instrumentation_enabled() -> bool:
    return _enabled


def enrich_spec(func: Callable, spec: Spec) -> Spec:
    try:
        sig = resolved_signature(func)
    except NameError as e:
        raise NameError(f"Cannot resolve annotations of {func.__qualname__}: {e}") from e

    check_ret_name(sig, spec)

    args = dict(spec["args"])
    for name, param in sig.parameters.items():
        if name not in args and param.annotation is not param.empty:
            args[name] = param_predicate(param)

    enriched = spec | {"args": args}

    if not enriched.get("ret") and sig.return_annotation is not sig.empty:
        enriched = enriched | {"ret": get_return_predicate(sig)}

    return enriched


OnError = Callable[[str], None]

_EMPTY_SPEC: Spec = {"args": {}}


def _default_on_error(message: str) -> None:
    raise SpecViolationError(message)


def is_instrumented(func: Callable) -> bool:
    return hasattr(func, "__spec__")


def _get_reason(predicate: Predicate, value: Any) -> str | None:
    if predicate(value):
        return None
    result = explain(predicate, value)
    return result.get("reason") or str(result)


def _check_args(spec: Spec, func_name: str, arguments: dict) -> str | None:
    failures = (
        (name, reason)
        for name, predicate in spec["args"].items()
        if name in arguments and (reason := _get_reason(predicate, value=arguments[name]))
    )
    if failure := first_true(failures):
        name, reason = failure
        return f"Parameter predicate for parameter '{name}' of function {func_name} failed. Reason: {reason}"

    if (pre := spec.get("pre")) and not pre(**arguments):
        args_str = ", ".join(f"{k}={v!r}" for k, v in arguments.items())
        return f"pre condition for function {func_name} failed. Arguments: {args_str}"
    return None


def _check_return_value(spec: Spec, func_name: str, result: Any) -> str | None:
    if return_p := spec.get("ret"):
        if reason := _get_reason(return_p, value=result):
            return f"Return predicate for function {func_name} failed. Reason: {reason}"
    return None


def _format_expected_exceptions(expected: type | tuple) -> str:
    if isinstance(expected, tuple):
        return ", ".join(e.__name__ for e in expected)
    return expected.__name__


def _check_exception(spec: Spec, func_name: str, exc: Exception) -> str | None:
    if expected := spec.get("raises"):
        if not isinstance(exc, expected):
            expected_str = _format_expected_exceptions(expected)
            return f"Unexpected exception {type(exc).__name__} for function {func_name}. Expected: {expected_str}"
        return None
    return None


def _check_constraints(spec: Spec, func_name: str, arguments: dict, result: Any) -> str | None:
    if fn := spec.get("fn"):
        name = ret_name(spec)
        if not fn(**arguments, **{name: result}):
            args_str = ", ".join(f"{k}={v!r}" for k, v in arguments.items())
            return f"fn constraint for function {func_name} failed. Arguments: {args_str}, {name}={result!r}"

    if fn_p := spec.get("fn_p"):
        p = fn_p(**arguments)
        if reason := _get_reason(p, value=result):
            return f"fn_p constraint for function {func_name} failed. Reason: {reason}"

    return None


def _replace_in_module(func: Callable, wrapped: Callable) -> None:
    module = sys.modules.get(func.__module__)
    if module and hasattr(module, func.__name__):
        setattr(module, func.__name__, wrapped)


def _report(on_error: OnError, error: str | None) -> None:
    if error:
        on_error(error)


def _make_wrapper(
    func: Callable,
    before: Callable[[tuple, dict], dict],
    on_exception: Callable[[Exception], None],
    after: Callable[[dict, Any], Any],
) -> Callable:
    if is_async_p(func):

        @wraps(func)
        async def wrapped(*args, **kwargs):
            if not _enabled:
                return await func(*args, **kwargs)
            arguments = before(args, kwargs)
            try:
                result = await func(*args, **kwargs)
            except Exception as exc:
                on_exception(exc)
                raise
            return after(arguments, result)

        return wrapped

    @wraps(func)
    def wrapped_sync(*args, **kwargs):
        if not _enabled:
            return func(*args, **kwargs)
        arguments = before(args, kwargs)
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            on_exception(exc)
            raise
        return after(arguments, result)

    return wrapped_sync


def instrument_function(func: Callable, spec: Spec, on_error: OnError = _default_on_error) -> Callable:
    if is_instrumented(func):
        return func
    func = unwrap(func)
    func_name = func.__name__
    # resolved once, on first call, so forward references (e.g. the enclosing class) exist by then
    resolved_signature = cache(lambda: signature(func))
    resolved_spec = cache(lambda: enrich_spec(func, spec))

    def _before(args: tuple, kwargs: dict) -> dict:
        bound = resolved_signature().bind(*args, **kwargs)
        bound.apply_defaults()
        _report(on_error, _check_args(resolved_spec(), func_name, bound.arguments))
        return bound.arguments

    def _on_exception(exc: Exception) -> None:
        _report(on_error, _check_exception(resolved_spec(), func_name, exc))

    def _after(arguments: dict, result: Any) -> Any:
        _report(on_error, _check_return_value(resolved_spec(), func_name, result))
        _report(on_error, _check_constraints(resolved_spec(), func_name, arguments, result))
        return result

    wrapped = _make_wrapper(func, _before, _on_exception, _after)
    wrapped.__spec__ = spec  # type: ignore
    _replace_in_module(func, wrapped)
    return wrapped


def instrument(spec_or_func: Spec | Callable = None, *, on_error: OnError = _default_on_error) -> Callable:  # type: ignore[assignment]
    if isclass(spec_or_func):
        instrument_class(spec_or_func, on_error=on_error)
        return spec_or_func

    if callable(spec_or_func):
        return instrument_function(spec_or_func, _EMPTY_SPEC, on_error)

    spec = spec_or_func or _EMPTY_SPEC

    def decorator(func: Callable) -> Callable:
        if isclass(func):
            instrument_class(func, on_error=on_error)
            return func
        return instrument_function(func, spec, on_error)

    return decorator


def _include_in_module(func: Callable, module: ModuleType, pattern: str | None) -> bool:
    return func.__module__ == module.__name__ and (pattern is None or fnmatch(func.__name__, pattern))


def instrument_module(module: ModuleType, pattern: str | None = None, on_error: OnError = _default_on_error) -> None:
    funcs = [func for _, func in getmembers(module, isfunction) if _include_in_module(func, module, pattern)]
    consume(side_effect(lambda func: instrument_function(func, _EMPTY_SPEC, on_error), funcs))


def instrument_class(cls: type, pattern: str | None = None, on_error: OnError = _default_on_error) -> None:
    for name, member in list(vars(cls).items()):
        descriptor = type(member) if isinstance(member, (staticmethod, classmethod)) else None
        func = member.__func__ if descriptor else member
        if isfunction(func) and not is_instrumented(func) and (pattern is None or fnmatch(name, pattern)):
            wrapped = instrument_function(func, _EMPTY_SPEC, on_error)
            setattr(cls, name, descriptor(wrapped) if descriptor else wrapped)
