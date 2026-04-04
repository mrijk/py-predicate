from typing import Any

import pytest
from helpers import exercise_predicate
from more_itertools import one, take

from predicate import always_false_p, explain
from predicate.consumes import consumes
from predicate.generator.helpers import random_anys


@pytest.mark.parametrize("value", take(5, random_anys()))
def test_always_false_p(value):
    assert not always_false_p(value)


def test_always_false_p_klass():
    assert always_false_p.klass is type(Any)


def test_always_false_p_explain():
    expected = {"reason": "Always returns False", "result": False}
    assert explain(always_false_p, None) == expected


def test_always_false_exercise():
    exercise_predicate(always_false_p)


@pytest.mark.parametrize("iterable", [[], ["foo"], [1, 2], (3, 4, 5, "foo", 6)])
def test_always_false_consumes(iterable):
    end = one(consumes(always_false_p, iterable))

    assert end == 0
