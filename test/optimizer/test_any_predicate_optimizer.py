import pytest

from predicate import all_p, always_false_p, always_true_p, any_p, can_optimize, eq_p, optimize


@pytest.mark.skip
def test_optimize_any_ne():
    # Any(~p) => ~All(p)
    eq_2 = eq_p(2)

    predicate = any_p(~eq_2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~all_p(eq_2)


@pytest.mark.skip
def test_optimize_any_always_false():
    predicate = any_p(always_false_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_any_always_true():
    predicate = any_p(always_true_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


@pytest.mark.skip
def test_optimize_any_not(p):
    # Any(~p) == ~All(p)

    predicate = any_p(~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~all_p(p)
