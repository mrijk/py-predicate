from helpers import (
    is_xor_p,
    is_and_p,
    is_not_p,
    is_or_p,
    is_false_p,
    is_true_p,
    is_all_p,
)
from predicate import (
    gt_p,
    le_p,
    can_optimize,
    optimize,
    always_true_p,
)
from predicate.standard_predicates import all_p


def test_optimize_not_or():
    """~(p | ~p) == False"""
    p = gt_p(2)

    predicate = ~(p | ~p)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_false_p(optimized)


def test_optimize_not_and():
    """~(p & ~p) == True"""
    p = gt_p(2)

    predicate = ~(p & ~p)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_true_p(optimized)


def test_optimize_not_xor_p_q():
    """~(p ^ q) == ~p ^ q"""
    p = gt_p(2)
    q = le_p(0)

    predicate = ~(p ^ q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_xor_p(optimized)
    assert is_not_p(optimized.left)


def test_optimize_not_xor_not_p_q():
    """~(~p ^ q) == p ^ q"""
    p = gt_p(2)
    q = le_p(0)

    predicate = ~(~p ^ q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_xor_p(optimized)
    assert not is_not_p(optimized.left)


def test_optimize_not_xor_p_not_q():
    """~(p ^ ~q) == p ^ q"""
    p = gt_p(2)
    q = le_p(0)

    predicate = ~(p ^ ~q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_xor_p(optimized)
    assert not is_not_p(optimized.right)


def test_optimize_or_1():
    """p | (~p & q) == p | q"""
    p = gt_p(2)
    q = le_p(0)

    le_0_or_gt_2 = p | (~p & q)

    assert is_or_p(le_0_or_gt_2)
    assert can_optimize(le_0_or_gt_2)

    optimized = optimize(le_0_or_gt_2)

    assert is_or_p(optimized)
    assert optimized.left == p
    assert optimized.right == q


def test_optimize_and_1():
    """p & (~p | q) == p & q"""
    p = gt_p(2)
    q = le_p(0)

    le_0_and_gt_2 = p & (~p | q)

    assert is_and_p(le_0_and_gt_2)
    assert can_optimize(le_0_and_gt_2)

    optimized = optimize(le_0_and_gt_2)

    assert is_and_p(optimized)
    assert optimized.left == p
    assert optimized.right == q


def test_optimize_and_2():
    """p & (q | ~p) == p & q"""
    p = gt_p(2)
    q = le_p(0)

    le_0_and_gt_2 = p & (q | ~p)

    assert is_and_p(le_0_and_gt_2)
    assert can_optimize(le_0_and_gt_2)

    optimized = optimize(le_0_and_gt_2)

    assert is_and_p(optimized)
    assert optimized.left == p
    assert optimized.right == q


def test_optimize_and_3():
    """(~p | q) & p == q & p"""
    p = gt_p(2)
    q = le_p(0)

    predicate = (~p | q) & p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_and_p(optimized)
    assert optimized.left == q
    assert optimized.right == p


def test_optimize_xor_1():
    """p ^ (^p & q) = ~(p | q)"""
    p = gt_p(2)
    q = le_p(0)

    predicate = p ^ (~p & q)

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_not_p(optimized)
    not_predicate = optimized.predicate
    assert is_and_p(not_predicate)
    assert not_predicate.left == p
    assert not_predicate.right == q


def test_optimize_xor_2():
    """p ^ (q & ~p) = ~(p | q)"""
    p = gt_p(2)
    q = le_p(0)

    predicate = p ^ (q & ~p)

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_not_p(optimized)
    not_predicate = optimized.predicate
    assert is_and_p(not_predicate)
    assert not_predicate.left == p
    assert not_predicate.right == q


def test_optimize_xor_3():
    """(q & ~p) ^ p = ~(p | q)"""
    p = gt_p(2)
    q = le_p(0)

    predicate = (q & ~p) ^ p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_not_p(optimized)
    not_predicate = optimized.predicate
    assert is_and_p(not_predicate)
    assert not_predicate.left == p
    assert not_predicate.right == q


def test_optimize_xor_4():
    """(~p & q) ^ p = ~(p | q)"""
    p = gt_p(2)
    q = le_p(0)

    predicate = (~p & q) ^ p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_not_p(optimized)
    not_predicate = optimized.predicate
    assert is_and_p(not_predicate)
    assert not_predicate.left == p
    assert not_predicate.right == q
