import pytest

from predicate import always_false_p, always_true_p, ge_p, is_int_p, is_str_p, le_p
from predicate.analysis import are_equivalent, is_satisfiable, is_tautology
from predicate.range_predicate import ge_le_p


@pytest.mark.parametrize(
    "predicate, expected, description",
    [
        (always_true_p, True, "always_true_p is a tautology"),
        (always_false_p, False, "always_false_p is not a tautology"),
        (is_int_p | ~is_int_p, True, "p | ~p is a tautology"),
        (is_int_p, False, "is_int_p is not a tautology"),
        (~(is_int_p & ~is_int_p), True, "~(p & ~p) is a tautology"),
    ],
)
def test_is_tautology(predicate, expected, description):
    assert is_tautology(predicate) is expected, description


@pytest.mark.parametrize(
    "predicate, expected, description",
    [
        (always_true_p, True, "always_true_p is satisfiable"),
        (always_false_p, False, "always_false_p is not satisfiable"),
        (is_int_p & is_str_p, False, "int & str contradiction is not satisfiable"),
        (is_int_p, True, "is_int_p is satisfiable"),
    ],
)
def test_is_satisfiable(predicate, expected, description):
    assert is_satisfiable(predicate) is expected, description


@pytest.mark.parametrize(
    "p, q, expected, description",
    [
        (always_true_p, always_true_p, True, "always_true_p is equivalent to itself"),
        (always_false_p, always_false_p, True, "always_false_p is equivalent to itself"),
        (always_true_p, always_false_p, False, "always_true_p is not equivalent to always_false_p"),
        (is_int_p, is_str_p, False, "is_int_p is not equivalent to is_str_p"),
        (is_int_p, is_int_p, True, "is_int_p is equivalent to itself"),
        (ge_le_p(lower=1, upper=5), ge_p(1) & le_p(5), True, "ge_le_p(1, 5) is equivalent to ge_p(1) & le_p(5)"),
    ],
)
def test_are_equivalent(p, q, expected, description):
    assert are_equivalent(p, q) is expected, description
