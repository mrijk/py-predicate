from collections import namedtuple
from typing import NamedTuple

from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import exercise, generate_true, is_instance_p, is_named_tuple_p


class Point(NamedTuple):
    x: int
    label: str


def test_generate_is_named_tuple():
    assert_generated_true(is_named_tuple_p)


def test_generate_named_tuple_instance():
    predicate = is_instance_p(Point)
    assert_generated_true(predicate)

    for point in take(10, generate_true(predicate)):
        assert isinstance(point.x, int)
        assert isinstance(point.label, str)


def test_generate_untyped_named_tuple_instance():
    assert_generated_true(is_instance_p(namedtuple("Pair", "a b")))  # noqa: PYI024


def test_exercise_named_tuple_argument():
    def norm(p: Point) -> int:
        return p.x

    assert take(5, exercise(norm))
