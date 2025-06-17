from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    can_optimize,
    eq_p,
    has_length_p,
    is_none_p,
    is_not_none_p,
    ne_p,
    optimize,
)


def test_optimize_all_true():
    predicate = all_p(always_true_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_all_false():
    predicate = all_p(always_false_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == has_length_p(eq_p(0))


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

    assert optimized == all_p(predicate=all_p(ne_p(2)))


def test_optimize_all_not(p):
    # All(~p) == ~Any(p)

    predicate = all_p(~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~any_p(p)


def test_optimize_all_not_none():
    predicate = all_p(predicate=is_not_none_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~any_p(is_none_p)
