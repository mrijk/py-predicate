from typing import Any

import pytest
from more_itertools import take

from predicate import always_false_p, explain
from predicate.generator.helpers import random_anys


@pytest.mark.parametrize("value", take(5, random_anys()))
def test_always_false_p(value):
    assert not always_false_p(value)


def test_always_false_p_klass():
    assert always_false_p.klass is type(Any)


def test_always_false_p_explain():
    expected = {"reason": "Always returns False", "result": False}
    assert explain(always_false_p, None) == expected
