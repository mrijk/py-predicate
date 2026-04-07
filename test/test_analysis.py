import pytest

from predicate import always_false_p, always_true_p, ge_p, is_int_p, is_str_p, le_p
from predicate.analysis import are_equivalent, is_satisfiable, is_tautology
from predicate.range_predicate import ge_le_p


@pytest.mark.parametrize(
    "predicate, description",
    [
        (always_true_p, "always_true_p is a tautology"),
        (is_int_p | ~is_int_p, "p | ~p is a tautology"),
        (~(is_int_p & ~is_int_p), "~(p & ~p) is a tautology"),
    ],
)
def test_is_tautology(predicate, description):
    assert is_tautology(predicate), description


@pytest.mark.parametrize(
    "predicate, description",
    [
        (always_false_p, "always_false_p is not a tautology"),
        (is_int_p, "is_int_p is not a tautology"),
    ],
)
def test_is_not_tautology(predicate, description):
    assert not is_tautology(predicate), description


@pytest.mark.parametrize(
    "predicate, description",
    [
        (always_true_p, "always_true_p is satisfiable"),
        (is_int_p, "is_int_p is satisfiable"),
    ],
)
def test_is_satisfiable(predicate, description):
    assert is_satisfiable(predicate), description


@pytest.mark.parametrize(
    "predicate, description",
    [
        (always_false_p, "always_false_p is not satisfiable"),
        (is_int_p & is_str_p, "int & str contradiction is not satisfiable"),
    ],
)
def test_is_not_satisfiable(predicate, description):
    assert not is_satisfiable(predicate), description


@pytest.mark.parametrize(
    "p, q, description",
    [
        (always_true_p, always_true_p, "always_true_p is equivalent to itself"),
        (always_false_p, always_false_p, "always_false_p is equivalent to itself"),
        (is_int_p, is_int_p, "is_int_p is equivalent to itself"),
        (ge_le_p(lower=1, upper=5), ge_p(1) & le_p(5), "ge_le_p(1, 5) is equivalent to ge_p(1) & le_p(5)"),
    ],
)
def test_are_equivalent(p, q, description):
    assert are_equivalent(p, q), description


@pytest.mark.parametrize(
    "p, q, description",
    [
        (always_true_p, always_false_p, "always_true_p is not equivalent to always_false_p"),
        (is_int_p, is_str_p, "is_int_p is not equivalent to is_str_p"),
    ],
)
def test_are_not_equivalent(p, q, description):
    assert not are_equivalent(p, q), description
