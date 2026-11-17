import math
from itertools import islice

import pytest

from predicate import (
    generate_false,
    generate_true,
    is_integer_valued_p,
    is_probability_p,
    is_within_p,
    non_neg_p,
    non_pos_p,
)


@pytest.mark.parametrize("value", [0.0, -0.0, 3.0, -3.0, 2.0**53])
def test_integer_valued_float(value):
    assert is_integer_valued_p(value)


@pytest.mark.parametrize("value", [3.5, math.inf, -math.inf, math.nan, "3", None])
def test_not_integer_valued_float(value):
    assert not is_integer_valued_p(value)


def test_absolute_tolerance_without_relative_slack():
    within = is_within_p(1_000_000_000.0, 0.25)
    assert within(1_000_000_000.25)
    assert not within(1_000_000_000.5)
    assert is_within_p(0.0, 0.0)(-0.0)
    assert not is_within_p(0.0, 0.0)(math.ulp(0.0))


@pytest.mark.parametrize(
    "target,delta", [(0.0, -1.0), (0.0, math.nan), (0.0, math.inf), (math.inf, 1.0), (math.nan, 1.0)]
)
def test_invalid_absolute_tolerance(target, delta):
    with pytest.raises(ValueError):
        is_within_p(target, delta)


@pytest.mark.parametrize(
    "value,non_negative,non_positive,probability",
    [
        (-1, False, True, False),
        (0, True, True, True),
        (-0.0, True, True, True),
        (0.5, True, False, True),
        (1, True, False, True),
        (2, True, False, False),
        (math.nan, False, False, False),
        (math.inf, True, False, False),
        (-math.inf, False, True, False),
    ],
)
def test_numeric_domains(value, non_negative, non_positive, probability):
    assert non_neg_p(value) is non_negative
    assert non_pos_p(value) is non_positive
    assert is_probability_p(value) is probability


@pytest.mark.parametrize(
    "predicate", [is_integer_valued_p, is_probability_p, non_neg_p, non_pos_p, is_within_p(0.0, 0.1)]
)
def test_float_predicate_generators(predicate):
    for generator, expected in [(generate_true, True), (generate_false, False)]:
        values = list(islice(generator(predicate), 20))
        assert len(values) == 20
        assert all(predicate(value) is expected for value in values)
