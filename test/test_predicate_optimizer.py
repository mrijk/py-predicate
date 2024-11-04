from helpers import (
    is_and_p,
    is_not_p,
    is_or_p,
    is_xor_p,
)

from predicate import (
    always_false_p,
    always_true_p,
    can_optimize,
    gt_p,
    le_p,
    optimize,
)


def test_optimize_not_or():
    # ~(p | ~p) == False
    p = gt_p(2)

    predicate = ~(p | ~p)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_not_and():
    # ~(p & ~p) == True
    p = gt_p(2)

    predicate = ~(p & ~p)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_not_xor_p_q():
    # ~(p ^ q) == ~p ^ q
    p = gt_p(2)
    q = le_p(0)

    predicate = ~(p ^ q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p ^ q


def test_optimize_not_xor_not_p_q():
    # ~(~p ^ q) == p ^ q
    p = gt_p(2)
    q = le_p(0)

    predicate = ~(~p ^ q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_not_xor_p_not_q():
    # ~(p ^ ~q) == p ^ q
    p = gt_p(2)
    q = le_p(0)

    predicate = ~(p ^ ~q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_or_1():
    # p | (~p & q) == p | q
    p = gt_p(2)
    q = le_p(0)

    predicate = p | (~p & q)

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p | q


def test_optimize_and_1():
    # p & (~p | q) == p & q
    p = gt_p(2)
    q = le_p(0)

    predicate = p & (~p | q)

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & q


def test_optimize_and_2():
    # p & (q | ~p) == p & q
    p = gt_p(2)
    q = le_p(0)

    predicate = p & (q | ~p)

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & q


def test_optimize_and_3():
    # (~p | q) & p == q & p
    p = gt_p(2)
    q = le_p(0)

    predicate = (~p | q) & p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q & p


def test_optimize_and_4():
    # (q | ~p) & p == q & p
    p = gt_p(2)
    q = le_p(0)

    predicate = (q | ~p) & p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q & p


def test_optimize_xor_1():
    # p ^ (^p & q) = ~(p | q)
    p = gt_p(2)
    q = le_p(0)

    predicate = p ^ (~p & q)

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_2():
    # p ^ (q & ~p) = ~(p | q)
    p = gt_p(2)
    q = le_p(0)

    predicate = p ^ (q & ~p)

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_3():
    # (q & ~p) ^ p = ~(p | q)
    p = gt_p(2)
    q = le_p(0)

    predicate = (q & ~p) ^ p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_4():
    # (~p & q) ^ p = ~(p | q)
    p = gt_p(2)
    q = le_p(0)

    predicate = (~p & q) ^ p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)
