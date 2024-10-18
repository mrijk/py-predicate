from predicate import (
    gt_p,
    NotPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    can_optimize,
    optimize,
)
from predicate.predicate import le_p, OrPredicate


def test_optimize_not_or():
    """~(p | ~p) == False"""
    p = gt_p(2)

    always_false = ~(p | ~p)

    assert isinstance(always_false, NotPredicate)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_optimize_not_and():
    """~(p & ~p) == True"""
    p = gt_p(2)

    always_true = ~(p & ~p)

    assert isinstance(always_true, NotPredicate)
    assert can_optimize(always_true) is True

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_optimize_or_1():
    """p | (~p & q) == p | q"""
    p = gt_p(2)
    q = le_p(0)

    le_0_or_gt_2 = p | (~p & q)

    assert isinstance(le_0_or_gt_2, OrPredicate)
    assert can_optimize(le_0_or_gt_2)

    optimized = optimize(le_0_or_gt_2)

    assert isinstance(optimized, OrPredicate)
