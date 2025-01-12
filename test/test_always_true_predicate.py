from typing import Any

import pytest
from more_itertools import take

from predicate import always_true_p
from predicate.generator.helpers import random_anys


@pytest.mark.parametrize("value", take(5, random_anys()))
def test_always_true_p(value):
    assert always_true_p(value)


def test_always_true_p_klass():
    assert always_true_p.klass is type(Any)
