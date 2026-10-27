import sys
from typing import LiteralString, Never, NoReturn, Tuple

import pytest
from more_itertools import take

from predicate import exercise, generate_false, generate_true
from predicate.spec.exercise_helpers import annotation_to_predicate


def test_annotation_to_predicate_set():
    predicate = annotation_to_predicate(set[int])

    assert predicate({1, 2, 3}) is True
    assert predicate({"a", "b"}) is False
    assert predicate([1, 2, 3]) is False


def test_annotation_to_predicate_dict():
    predicate = annotation_to_predicate(dict[str, int])

    assert predicate({})
    assert predicate({"a": 1})
    assert not predicate({"a": "b"})
    assert not predicate([])


def test_annotation_to_predicate_frozenset():
    predicate = annotation_to_predicate(frozenset[int])

    assert predicate(frozenset({1, 2, 3})) is True
    assert predicate(frozenset({"a", "b"})) is False
    assert predicate({1, 2, 3}) is False


if sys.version_info >= (3, 15):

    def test_annotation_to_predicate_frozendict():
        predicate = annotation_to_predicate(frozendict[str, int])  # noqa: F821

        assert predicate(frozendict({"a": 1})) is True  # noqa: F821
        assert predicate(frozendict({"a": "b"})) is False  # noqa: F821
        assert predicate({"a": 1}) is False


@pytest.mark.parametrize("annotation", [Never, NoReturn])
def test_annotation_to_predicate_never(annotation):
    predicate = annotation_to_predicate(annotation)

    assert predicate(None) is False
    assert predicate(1) is False


def test_get_return_spec_uses_annotation():
    from predicate.spec.exercise_helpers import get_return_spec

    def f() -> list[int]:
        return [1]

    def g() -> NoReturn:
        raise ValueError

    ret = get_return_spec(f, {"args": {}})["ret"]
    assert ret([1, 2]) is True
    assert ret(["a"]) is False

    assert get_return_spec(g, {"args": {}})["ret"](None) is False


def test_annotation_to_predicate_literal_string():
    predicate = annotation_to_predicate(LiteralString)

    assert predicate("abc") is True
    assert predicate(1) is False


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (float, 1, True),
        (float, 1.5, True),
        (float, "1", False),
        (complex, 1, True),
        (complex, 1.5, True),
        (complex, 1j, True),
        (int, 1.5, False),
    ],
)
def test_annotation_to_predicate_numeric_tower(annotation, value, expected):
    assert annotation_to_predicate(annotation)(value) is expected


def test_annotation_to_predicate_union_of_three():
    predicate = annotation_to_predicate(int | str | None)

    assert predicate(1) is True
    assert predicate("a") is True
    assert predicate(None) is True
    assert predicate(1.5) is False


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (tuple[int, ...], (), True),
        (tuple[int, ...], (1, 2, 3), True),
        (tuple[int, ...], (1, "x"), False),
        (tuple[int, ...], [1, 2], False),
        (Tuple[str, ...], ("a",), True),
        (Tuple[str, ...], (1,), False),
        (tuple[()], (), True),
        (tuple[()], (1,), False),
        (tuple[()], [], False),
        (Tuple[()], (), True),
        (Tuple[()], (1,), False),
        (Tuple, (1, "x"), True),
        (tuple[int, str], (1, "x"), True),
        (tuple[int, str], (1, 2), False),
    ],
)
def test_annotation_to_predicate_tuple(annotation, value, expected):
    assert annotation_to_predicate(annotation)(value) is expected


@pytest.mark.parametrize("annotation", [tuple[int, ...], tuple[()]])
def test_annotation_to_predicate_tuple_generators(annotation):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


def test_exercise_variadic_tuple():
    def total(values: tuple[int, ...]) -> int:
        return sum(values)

    assert take(5, exercise(total))
