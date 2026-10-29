import datetime
import math
import zoneinfo
from typing import Annotated

import annotated_types as at
import pytest
from more_itertools import take

from predicate import exercise, ge_lt_p, generate_true
from predicate.spec.exercise_helpers import annotation_to_predicate
from predicate.spec.instrument import instrument

_amsterdam = zoneinfo.ZoneInfo("Europe/Amsterdam")

# annotation, a value that satisfies it, a value that breaks the constraint (but not the base type)
CASES = [
    (Annotated[int, at.Gt(0)], 1, 0),
    (Annotated[int, at.Ge(0)], 0, -1),
    (Annotated[int, at.Lt(0)], -1, 0),
    (Annotated[int, at.Le(0)], 0, 1),
    (Annotated[int, at.Interval(gt=0, le=10)], 10, 11),
    (Annotated[int, at.MultipleOf(5)], 10, 3),
    (Annotated[str, at.MinLen(3)], "abc", "ab"),
    (Annotated[str, at.MaxLen(3)], "abc", "abcd"),
    (Annotated[list, at.Len(2, 4)], [1, 2], [1]),
    (
        Annotated[datetime.datetime, at.Timezone(None)],
        datetime.datetime(2024, 1, 1),
        datetime.datetime(2024, 1, 1, tzinfo=datetime.UTC),
    ),
    (
        Annotated[datetime.datetime, at.Timezone(...)],
        datetime.datetime(2024, 1, 1, tzinfo=datetime.UTC),
        datetime.datetime(2024, 1, 1),
    ),
    (
        Annotated[datetime.datetime, at.Timezone("Europe/Amsterdam")],
        datetime.datetime(2024, 1, 1, tzinfo=_amsterdam),
        datetime.datetime(2024, 1, 1, tzinfo=datetime.UTC),
    ),
    (Annotated[str, at.Predicate(str.isupper)], "ABC", "abc"),
    (Annotated[int, at.Predicate(ge_lt_p(0, 150))], 30, 200),
    (at.LowerCase[str], "abc", "ABC"),
    (at.UpperCase[str], "ABC", "abc"),
    (at.IsDigits[str], "123", "a1"),  # type: ignore[type-arg, misc]  # IsDigits is a non-generic alias to mypy
    (at.IsFinite[float], 1.0, math.inf),
    (at.IsNotFinite[float], math.inf, 1.0),
    (at.IsNan[float], math.nan, 1.0),
    (at.IsNotNan[float], 1.0, math.nan),
    (at.IsInfinite[float], math.inf, 1.0),
    (at.IsNotInfinite[float], 1.0, math.inf),
]


@pytest.mark.parametrize(("annotation", "good", "bad"), CASES)
def test_annotated_constraint_checked(annotation, good, bad):
    # #384: the constraints in Annotated[T, ...] used to be dropped, so only T was checked
    predicate = annotation_to_predicate(annotation)

    assert predicate(good)
    assert not predicate(bad)


@pytest.mark.parametrize(("annotation", "good", "bad"), CASES)
def test_annotated_constraint_generated(annotation, good, bad):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in take(50, generate_true(predicate)))


@pytest.mark.parametrize(("annotation", "good", "bad"), CASES)
def test_annotated_constraint_instrumented(annotation, good, bad):
    errors = []

    @instrument(on_error=errors.append)
    def f(x: annotation) -> None: ...  # type: ignore[valid-type]

    f(good)
    assert not errors

    f(bad)
    assert errors


def test_exercise_respects_annotated_constraint():
    def positive(x: Annotated[int, at.Gt(0)]) -> int:
        assert x > 0
        return x

    assert len(take(20, exercise(positive, n=20))) == 20


def test_annotated_other_metadata_ignored():
    assert annotation_to_predicate(Annotated[int, "metadata", at.doc("a number")])(-5)


def test_annotated_type_alias_keeps_constraint():
    type Positive = Annotated[int, at.Gt(0)]

    assert not annotation_to_predicate(Positive)(0)
