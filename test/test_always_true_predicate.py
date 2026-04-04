from typing import Any

import pytest
from helpers import exercise_predicate
from more_itertools import one, take

from predicate import always_true_p
from predicate.consumes import consumes
from predicate.generator.helpers import random_anys


@pytest.mark.parametrize("value", take(5, random_anys()))
def test_always_true_p(value):
    assert always_true_p(value)


def test_always_true_p_klass():
    assert always_true_p.klass is type(Any)


def test_always_true_exercise():
    exercise_predicate(always_true_p)


@pytest.mark.parametrize("iterable", [["foo"], [1, 2], (3, 4, 5, "foo", 6)])
def test_always_true_consumes(iterable):
    end = one(consumes(always_true_p, iterable))

    assert end == 1
