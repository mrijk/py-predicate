from predicate import (
    gt_p,
    le_p,
    AndPredicate,
    NotPredicate,
    OrPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    can_optimize,
    optimize,
)


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
    assert can_optimize(le_0_or_gt_2) is True

    optimized = optimize(le_0_or_gt_2)

    assert isinstance(optimized, OrPredicate)
    assert optimized.left == p
    assert optimized.right == q


def test_optimize_and_1():
    """p & (~p | q) == p & q"""
    p = gt_p(2)
    q = le_p(0)

    le_0_and_gt_2 = p & (~p | q)

    assert isinstance(le_0_and_gt_2, AndPredicate)
    assert can_optimize(le_0_and_gt_2) is True

    optimized = optimize(le_0_and_gt_2)

    assert isinstance(optimized, AndPredicate)
    assert optimized.left == p
    assert optimized.right == q


def test_optimize_and_2():
    """p & (q | ~p) == p & q"""
    p = gt_p(2)
    q = le_p(0)

    le_0_and_gt_2 = p & (q | ~p)

    assert isinstance(le_0_and_gt_2, AndPredicate)
    assert can_optimize(le_0_and_gt_2) is True

    optimized = optimize(le_0_and_gt_2)

    assert isinstance(optimized, AndPredicate)
    assert optimized.left == p
    assert optimized.right == q


def test_optimize_and_3():
    """(~p | q) & p == q & p"""
    p = gt_p(2)
    q = le_p(0)

    le_0_and_gt_2 = (~p | q) & p

    assert isinstance(le_0_and_gt_2, AndPredicate)
    assert can_optimize(le_0_and_gt_2) is True

    optimized = optimize(le_0_and_gt_2)

    assert isinstance(optimized, AndPredicate)
    assert optimized.left == q
    assert optimized.right == p
