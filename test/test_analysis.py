import pytest

from predicate import always_false_p, always_true_p, ge_p, is_int_p, is_str_p, le_p
from predicate.analysis import are_equivalent, is_satisfiable, is_tautology
from predicate.range_predicate import ge_le_p


@pytest.mark.parametrize(
    "predicate, expected",
    [
        (always_true_p, True),
        (always_false_p, False),
        (is_int_p | ~is_int_p, True),
        (is_int_p, False),
        (~(is_int_p & ~is_int_p), True),
    ],
)
def test_is_tautology(predicate, expected):
    assert is_tautology(predicate) is expected


@pytest.mark.parametrize(
    "predicate, expected",
    [
        (always_true_p, True),
        (always_false_p, False),
        (is_int_p & is_str_p, False),
        (is_int_p, True),
    ],
)
def test_is_satisfiable(predicate, expected):
    assert is_satisfiable(predicate) is expected


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (always_true_p, always_true_p, True),
        (always_false_p, always_false_p, True),
        (always_true_p, always_false_p, False),
        (is_int_p, is_str_p, False),
        (is_int_p, is_int_p, True),
        (ge_le_p(lower=1, upper=5), ge_p(1) & le_p(5), True),
    ],
)
def test_are_equivalent(p, q, expected):
    assert are_equivalent(p, q) is expected
