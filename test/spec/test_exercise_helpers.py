import collections.abc
import sys
from typing import AbstractSet, LiteralString, Never, NoReturn, Tuple

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


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (collections.abc.Sequence[int], [1, 2], True),
        (collections.abc.Sequence[int], (1, 2), True),
        (collections.abc.Sequence[int], [], True),
        (collections.abc.Sequence[int], [1, "x"], False),
        (collections.abc.Sequence[int], {1, 2}, False),
        (collections.abc.MutableSequence[int], (1, 2), False),
        (collections.abc.Collection[int], {1, 2}, True),
        (collections.abc.Collection[int], {"x"}, False),
        (collections.abc.Set[int], frozenset({1}), True),
        (collections.abc.Set[int], {"x"}, False),
        (AbstractSet[int], {1}, True),
        (collections.abc.MutableSet[int], frozenset({1}), False),
        (collections.abc.Mapping[str, int], {}, True),
        (collections.abc.Mapping[str, int], {"a": 1}, True),
        (collections.abc.Mapping[str, int], {"a": "b"}, False),
        (collections.abc.Mapping[str, int], [("a", 1)], False),
        (collections.abc.MutableMapping[str, int], {"a": 1}, True),
        (collections.abc.Sequence, ["x"], True),
    ],
)
def test_annotation_to_predicate_abc_generics(annotation, value, expected):
    assert annotation_to_predicate(annotation)(value) is expected


@pytest.mark.parametrize(
    "annotation",
    [
        collections.abc.Sequence[int],
        collections.abc.Sequence[str],
        collections.abc.MutableSequence[int],
        collections.abc.Collection[int],
        collections.abc.Set[str],
        collections.abc.MutableSet[int],
        collections.abc.Mapping[int, str],
        collections.abc.MutableMapping[str, int],
        collections.abc.Sequence[collections.abc.Sequence[int]],
    ],
)
def test_annotation_to_predicate_abc_generators(annotation):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


def test_exercise_variadic_tuple():
    def total(values: tuple[int, ...]) -> int:
        return sum(values)

    assert take(5, exercise(total))


def test_exercise_abc_generics():
    def count(values: collections.abc.Sequence[str], lookup: collections.abc.Mapping[str, int]) -> int:
        return sum(lookup.get(value, 0) for value in values)

    assert take(5, exercise(count))


def test_annotation_to_predicate_object():
    predicate = annotation_to_predicate(object)

    assert predicate(None)
    assert predicate(1)
    assert predicate(object())


def test_exercise_object_parameter():
    def describe(x: object) -> str:
        return type(x).__name__

    assert take(5, exercise(describe))
