from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from predicate.spec.exercise import exercise
from predicate.spec.instrument import instrument
from predicate.spec.spec import SpecViolationError, UnresolvedAnnotationWarning

if TYPE_CHECKING:
    import datetime as dt
    from decimal import Decimal

    from _typeshed import SupportsRead  # only exists for type checkers

    Amount = Decimal | int


@instrument
def add(x: int, y: int) -> int:
    return x + y


@instrument
def to_str(x: int) -> int:
    return str(x)  # type: ignore


class Node:
    @instrument
    def clone(self) -> Node:
        return Node()


@instrument
def type_checking_import(x: Decimal) -> int:
    return 0


@instrument
def type_checking_module_alias(x: dt.timedelta) -> int:
    return 0


@instrument
def type_checking_type_alias(x: Amount) -> int:
    return 0


@instrument
def unresolvable(x: SupportsRead[str]) -> int:
    return 0


def test_instrument_postponed_ok():
    assert add(1, 2) == 3


def test_instrument_postponed_wrong_parameter():
    with pytest.raises(SpecViolationError, match="Parameter predicate for parameter 'y' of function add failed"):
        add(1, "2")


def test_instrument_postponed_return_fails():
    with pytest.raises(SpecViolationError, match="Return predicate for function to_str failed"):
        to_str(1)


def test_instrument_postponed_forward_reference():
    assert isinstance(Node().clone(), Node)


def test_instrument_type_checking_import():
    from decimal import Decimal

    assert type_checking_import(Decimal(1)) == 0

    with pytest.raises(SpecViolationError, match="parameter 'x' of function type_checking_import failed"):
        type_checking_import(1)


def test_instrument_type_checking_module_alias():
    from datetime import timedelta

    assert type_checking_module_alias(timedelta(1)) == 0

    with pytest.raises(SpecViolationError, match="parameter 'x' of function type_checking_module_alias failed"):
        type_checking_module_alias(1)


def test_instrument_type_checking_type_alias():
    from decimal import Decimal

    assert type_checking_type_alias(Decimal(1)) == 0
    assert type_checking_type_alias(1) == 0

    with pytest.raises(SpecViolationError, match="parameter 'x' of function type_checking_type_alias failed"):
        type_checking_type_alias("1")


def test_exercise_type_checking_import():
    assert list(exercise(type_checking_module_alias.__wrapped__, n=3))


def test_instrument_postponed_unresolvable():
    # SupportsRead only exists for type checkers: the parameter is treated as Any, with a warning (#292)
    with pytest.warns(UnresolvedAnnotationWarning, match="'x' in unresolvable can't be evaluated"):
        assert unresolvable(0) == 0


def test_exercise_postponed():
    def adder(x: int, y: int) -> int:
        return x + y

    assert list(exercise(adder, n=3))


def test_instrument_postponed_quoted_annotations():
    @instrument
    def total(x: "list[int]", y: list["int"]) -> "int":
        return sum(x) + sum(y)

    assert total([1], [2]) == 3

    with pytest.raises(SpecViolationError, match="Parameter predicate for parameter 'y' of function total failed"):
        total([1], ["2"])
