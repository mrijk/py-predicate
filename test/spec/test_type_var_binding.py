from typing import TypeVar

import pytest

from predicate.spec.instrument import instrument_function
from predicate.spec.spec import SpecViolationError

T = TypeVar("T")


def dup(x: T) -> T:
    return x


def bad_dup(x: T) -> T:
    return str(x)  # type: ignore[return-value]


def first(xs: list[T]) -> T:
    return xs[0]


def bad_first(xs: list[T]) -> T:
    return 1  # type: ignore[return-value]


def widen(a: T, b: T) -> T:
    return b


def maybe(x: T) -> T | None:
    return None


def test_ok():
    assert instrument_function(dup, {"args": {}})(1) == 1
    assert instrument_function(first, {"args": {}})(["a"]) == "a"
    assert instrument_function(widen, {"args": {}})(1, "a") == "a"
    assert instrument_function(maybe, {"args": {}})(1) is None


def test_violation():
    with pytest.raises(SpecViolationError, match="T=int"):
        instrument_function(bad_dup, {"args": {}})(1)
    with pytest.raises(SpecViolationError, match="T=str"):
        instrument_function(bad_first, {"args": {}})(["a"])


def test_no_evidence():
    assert instrument_function(bad_first, {"args": {}})([]) == 1
