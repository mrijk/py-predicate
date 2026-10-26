from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from predicate.spec.exercise import exercise
from predicate.spec.instrument import instrument

if TYPE_CHECKING:
    from decimal import Decimal


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
def unresolvable(x: Decimal) -> int:
    return 0


def test_instrument_postponed_ok():
    assert add(1, 2) == 3


def test_instrument_postponed_wrong_parameter():
    with pytest.raises(ValueError, match="Parameter predicate for function add failed"):
        add(1, "2")


def test_instrument_postponed_return_fails():
    with pytest.raises(ValueError, match="Return predicate for function to_str failed"):
        to_str(1)


def test_instrument_postponed_forward_reference():
    assert isinstance(Node().clone(), Node)


def test_instrument_postponed_unresolvable():
    with pytest.raises(NameError, match="Cannot resolve annotations of unresolvable"):
        unresolvable(0)


def test_exercise_postponed():
    def adder(x: int, y: int) -> int:
        return x + y

    assert list(exercise(adder, n=3))


def test_instrument_postponed_quoted_annotations():
    @instrument
    def total(x: "list[int]", y: list["int"]) -> "int":
        return sum(x) + sum(y)

    assert total([1], [2]) == 3

    with pytest.raises(ValueError, match="Parameter predicate for function total failed"):
        total([1], ["2"])
