import os
import sys
from collections.abc import Iterator
from functools import cache, wraps
from inspect import Signature, signature, unwrap
from typing import Any, Callable, TypeAlias

from more_itertools import first, first_true, only

from predicate.explain import explain
from predicate.predicate import Predicate
from predicate.spec.exercise_helpers import (
    callable_name,
    check_ret_name,
    get_return_predicate,
    param_predicate,
    ret_name,
    type_var_failure,
)
from predicate.spec.exercise_helpers import resolved_signature as resolve_signature
from predicate.spec.spec import InvalidSpecError, Spec, SpecViolationError

BeforeContext: TypeAlias = tuple[dict[str, Any], dict[str, Any]]


def _enabled_from_environment(value: str | None) -> bool:
    return (value or "").strip().lower() not in {"0", "false", "no", "off"}


_enabled = _enabled_from_environment(os.environ.get("PREDICATE_INSTRUMENT"))


def set_instrumentation(enabled: bool) -> None:
    """Turn the checks of all instrumented functions on or off; when off they call the original function directly."""
    global _enabled
    _enabled = enabled


def is_instrumentation_enabled() -> bool:
    return _enabled


def enrich_spec(func: Callable[..., Any], spec: Spec) -> Spec:
    sig = resolve_signature(func)  # unresolvable annotations become Any, with an UnresolvedAnnotationWarning

    snapshot = spec.get("snapshot", {})
    if unknown := first(snapshot.keys() - sig.parameters.keys(), False):
        raise InvalidSpecError(f"Snapshot parameter '{unknown}' not in function signature")

    if snapshot and "old" in sig.parameters:
        raise InvalidSpecError("Parameter 'old' is reserved when snapshots are configured")

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


def default_on_error(message: str) -> None:
    raise SpecViolationError(message)


def is_instrumented(func: Callable[..., Any]) -> bool:
    return hasattr(func, "__spec__")


def _get_reason(predicate: Predicate[Any], value: Any) -> str | None:
    if predicate(value):
        return None
    result = explain(predicate, value)
    return result.get("reason") or str(result)


def _check_args(spec: Spec, func_name: str, arguments: dict[str, Any]) -> str | None:
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


def _check_type_vars(sig: Signature, func_name: str, arguments: dict[str, Any], result: Any) -> str | None:
    if reason := type_var_failure(sig, arguments, result):
        return f"Type variable binding for function {func_name} failed. Reason: {reason}"
    return None


def _format_expected_exceptions(expected: type | tuple[Any, ...]) -> str:
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


def _check_fn_constraints(
    spec: Spec, func_name: str, arguments: dict[str, Any], result: Any, old: dict[str, Any]
) -> Iterator[str]:
    if fn := spec.get("fn"):
        kwargs = arguments | {ret_name(spec): result}

        if spec.get("snapshot"):
            kwargs["old"] = old

        if not fn(**kwargs):
            args_str = ", ".join(f"{k}={v!r}" for k, v in arguments.items())
            yield f"fn constraint for function {func_name} failed. Arguments: {args_str}, {ret_name(spec)}={result!r}"


def _check_fn_p_constraints(
    spec: Spec, func_name: str, arguments: dict[str, Any], result: Any, old: dict[str, Any]
) -> Iterator[str]:
    if fn_p := spec.get("fn_p"):
        kwargs = arguments

        if spec.get("snapshot"):
            kwargs["old"] = old

        p = fn_p(**kwargs)
        if reason := _get_reason(p, value=result):
            yield f"fn_p constraint for function {func_name} failed. Reason: {reason}"


def _check_constraints(
    spec: Spec, func_name: str, arguments: dict[str, Any], result: Any, old: dict[str, Any]
) -> Iterator[str]:
    yield from _check_fn_constraints(spec, func_name, arguments, result, old)
    yield from _check_fn_p_constraints(spec, func_name, arguments, result, old)


def _replace_in_module(func: Callable[..., Any], wrapped: Callable[..., Any]) -> None:
    # A partial or a callable instance has no __name__: it isn't a module-level function to replace (#362)
    name = getattr(func, "__name__", None)
    module = sys.modules.get(getattr(func, "__module__", None) or "")
    if name and module and hasattr(module, name):
        setattr(module, name, wrapped)


def _report(on_error: OnError, error: str | None) -> None:
    if error:
        on_error(error)


def _make_wrapper(
    func: Callable[..., Any],
    before: Callable[..., BeforeContext],
    on_exception: Callable[[Exception], None],
    after: Callable[[BeforeContext, Any], Any],
) -> Callable[..., Any]:
    from predicate import is_async_p

    if is_async_p(func):

        @wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
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
    def wrapped_sync(*args: Any, **kwargs: Any) -> Any:
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


def instrument_function(
    func: Callable[..., Any], spec: Spec, on_error: OnError = default_on_error
) -> Callable[..., Any]:
    if is_instrumented(func):
        return func
    func = unwrap(func)
    func_name = callable_name(func)
    # resolved once, on first call, so forward references (e.g. the enclosing class) exist by then
    resolved_signature = cache(lambda: signature(func))
    resolved_spec = cache(lambda: enrich_spec(func, spec))
    typed_signature = cache(lambda: resolve_signature(func))

    def _before(args: tuple[Any, ...], kwargs: dict[str, Any]) -> tuple[dict[Any, Any], dict[Any, Any]]:
        bound = resolved_signature().bind(*args, **kwargs)
        bound.apply_defaults()

        arguments = bound.arguments

        _report(on_error, _check_args(resolved_spec(), func_name, arguments))

        old = {name: capture(arguments[name]) for name, capture in resolved_spec().get("snapshot", {}).items()}

        return arguments, old

    def _on_exception(exc: Exception) -> None:
        _report(on_error, _check_exception(resolved_spec(), func_name, exc))

    def _after(context: tuple[dict[str, Any], dict[str, Any]], result: Any) -> Any:
        arguments, old = context

        _report(on_error, _check_return_value(resolved_spec(), func_name, result))
        _report(on_error, _check_type_vars(typed_signature(), func_name, arguments, result))
        _report(on_error, only(_check_constraints(resolved_spec(), func_name, arguments, result, old)))
        return result

    wrapped = _make_wrapper(func, _before, _on_exception, _after)
    wrapped.__spec__ = spec  # type: ignore
    _replace_in_module(func, wrapped)
    return wrapped
