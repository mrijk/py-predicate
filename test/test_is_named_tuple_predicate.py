from collections import namedtuple
from typing import NamedTuple

from predicate import explain, is_named_tuple_p


class Point(NamedTuple):
    x: int
    y: int


def test_is_named_tuple():
    assert is_named_tuple_p(Point(1, 2))
    assert is_named_tuple_p(namedtuple("Pair", "a b")(1, 2))  # noqa: PYI024


def test_is_named_tuple_fail():
    assert not is_named_tuple_p((1, 2))
    assert not is_named_tuple_p([1, 2])
    assert not is_named_tuple_p(Point)


def test_is_named_tuple_explain():
    expected = {"reason": "(1, 2) is not a named tuple", "result": False}
    assert explain(is_named_tuple_p, (1, 2)) == expected
