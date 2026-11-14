"""Hypothesis integration for Specs: generate arguments for, and property-test, a function against its Spec."""

import inspect
from collections.abc import Callable
from functools import partial
from types import FunctionType
from typing import Any

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate.integrations.hypothesis.strategies import from_predicate
from predicate.is_async_predicate import is_async_p
from predicate.spec.exercise_function import get_spec_from_function_annotation
from predicate.spec.exercise_helpers import (
    call_args,
    callable_name,
    check_exception,
    check_signature_against_spec,
    resolved_signature,
    verify_result,
    yield_predicate,
)
from predicate.spec.spec import Spec


def from_spec(f: Callable[..., Any], spec: Spec | None = None) -> SearchStrategy[dict[str, Any]]:
    """Return a strategy of argument dicts ({parameter: value}) that satisfy the spec's arg predicates and pre."""
    return _arguments(_resolve(f, spec))


def given_spec(f: Callable[..., Any], spec: Spec | None = None) -> Callable[[], None]:
    """Return a Hypothesis test that calls f with generated arguments and verifies the results against its spec.

    Checks the same things as exercise (ret, fn, fn_p and raises), but with Hypothesis' shrinking and replay:
    test_f = given_spec(f, spec)
    """
    _check_supported(f)
    spec = _resolve(f, spec)
    sig = resolved_signature(f)

    def check(value: dict[str, Any]) -> None:
        args, kwargs = call_args(sig, value)
        try:
            result = f(*args, **kwargs)
        except Exception as exc:
            check_exception(spec, value, exc)  # re-raises unless the spec expects this exception
            return
        verify_result(spec, spec["ret"], value, result, sig)

    check.__name__ = f"check_{callable_name(f)}"
    return given(_arguments(spec))(check)


def _resolve(f: Callable[..., Any], spec: Spec | None) -> Spec:
    return check_signature_against_spec(f, spec) if spec else get_spec_from_function_annotation(f)


def _arguments(spec: Spec) -> SearchStrategy[dict[str, Any]]:
    arguments = st.fixed_dictionaries({name: from_predicate(p) for name, p in spec["args"].items()})
    if (pre := spec.get("pre")) is None:
        return arguments

    def satisfies_pre(value: dict[str, Any]) -> bool:
        return bool(pre(**value))

    return arguments.filter(satisfies_pre)


def _check_supported(f: Callable[..., Any]) -> None:
    # ponytail: plain sync functions only; add async, generators and classes (exercise_class) when needed
    if not isinstance(f, FunctionType | partial):
        raise NotImplementedError("given_spec only supports functions for now, not classes or callable objects")
    if is_async_p(f) or inspect.isasyncgenfunction(f) or yield_predicate(f) is not None:
        raise NotImplementedError("given_spec doesn't support async functions or generators yet")
