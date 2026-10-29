import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    can_optimize,
    eq_p,
    ge_p,
    is_not_empty_p,
    ne_p,
    not_in_p,
    optimize,
)


def test_optimize_any_ne():
    # any_p(~eq_p(2)) => any_p(ne_p(2)): ~eq_p(2) simplifies, so any_p stays (rewriting it to ~all_p would cycle)
    predicate = any_p(~eq_p(2))

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == any_p(ne_p(2))


def test_optimize_any_ne_is_stable():
    assert not can_optimize(any_p(ne_p(2)))


def test_optimize_any_always_false():
    predicate = any_p(always_false_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_any_always_true():
    # any_p(always_true_p) is True for exactly the non-empty iterables (#369)
    predicate = any_p(always_true_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_not_empty_p


@pytest.mark.parametrize("value", [[], [0], (), (1, 2), "", "a", {}, {1: 2}])
def test_optimize_any_always_true_same_answers(value):
    predicate = any_p(always_true_p)

    assert optimize(predicate)(value) == predicate(value)


def test_optimize_any_not_in_empty_set():
    # not_in_p() with no values optimizes to always_true_p, so this hit the same rule
    predicate = any_p(not_in_p(set()))

    assert not optimize(predicate)([])


def test_optimize_any_not(p):
    # Any(~p) == ~All(p)

    predicate = any_p(~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~all_p(p)


def test_optimize_any_inner_change():
    # any_p(ge(5) | ge(3)): inner simplifies to ge(3), falls to final return

    predicate = any_p(ge_p(5) | ge_p(3))

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == any_p(ge_p(3))
