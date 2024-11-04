from helpers import is_all_p

from predicate import can_optimize, optimize
from predicate.predicate import always_false_p, always_true_p
from predicate.standard_predicates import all_p, any_p, eq_p, fn_p, ne_p, is_not_none_p, is_none_p


def test_optimize_all_true():
    predicate = all_p(always_true_p)

    assert is_all_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_all_false():
    predicate = all_p(always_false_p)

    assert is_all_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert not is_all_p(optimized)


def test_not_optimize_all():
    eq_2 = eq_p(2)
    predicate = all_p(predicate=~eq_2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == all_p(predicate=ne_p(2))


def test_optimize_all_any():
    eq_2 = eq_p(2)
    predicate = all_p(predicate=~any_p(eq_2))

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~any_p(predicate=any_p(eq_2))


def test_optimize_all_not():
    # All(~p) == ~Any(p)
    p = fn_p(lambda x: x == 2)

    predicate = all_p(~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~any_p(p)


def test_optimize_all_not_none():
    predicate = all_p(predicate=is_not_none_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~any_p(is_none_p)
