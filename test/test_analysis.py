import pytest

from predicate import always_false_p, always_true_p, ge_p, is_int_p, is_str_p
from predicate.analysis import are_equivalent, is_satisfiable, is_tautology
from predicate.range_predicate import ge_le_p


def test_is_tautology_always_true():
    assert is_tautology(always_true_p)


def test_is_tautology_always_false():
    assert not is_tautology(always_false_p)


def test_is_tautology_p_or_not_p():
    assert is_tautology(is_int_p | ~is_int_p)


def test_is_tautology_simple_predicate():
    assert not is_tautology(is_int_p)


def test_is_satisfiable_always_true():
    assert is_satisfiable(always_true_p)


def test_is_satisfiable_always_false():
    assert not is_satisfiable(always_false_p)


def test_is_satisfiable_contradiction():
    assert not is_satisfiable(is_int_p & is_str_p)


def test_is_satisfiable_simple_predicate():
    assert is_satisfiable(is_int_p)


def test_are_equivalent_same_predicate():
    assert are_equivalent(is_int_p, is_int_p)


def test_are_equivalent_range():
    from predicate import le_p

    assert are_equivalent(ge_le_p(lower=1, upper=5), ge_p(1) & le_p(5))


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (always_true_p, always_true_p, True),
        (always_false_p, always_false_p, True),
        (always_true_p, always_false_p, False),
        (is_int_p, is_str_p, False),
    ],
)
def test_are_equivalent_parametrized(p, q, expected):
    assert are_equivalent(p, q) is expected
