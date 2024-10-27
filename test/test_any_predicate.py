from predicate import always_false_p, always_true_p, can_optimize, optimize
from predicate.standard_predicates import all_p, any_p, eq_p, is_int_p


def test_any():
    any_int = any_p(is_int_p)

    assert any_int(()) is False
    assert any_int((1, 2, 3)) is True
    assert any_int([1, 2, 3]) is True
    assert any_int([None, 2, 3]) is True


def test_optimize_any_ne():
    """Any(~p) => ~All(p)"""
    eq_2 = eq_p(2)

    predicate = any_p(~eq_2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~all_p(eq_2)


def test_optimize_any_always_false():
    predicate = any_p(always_false_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_any_always_true():
    predicate = any_p(always_true_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p
