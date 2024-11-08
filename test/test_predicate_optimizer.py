from helpers import (
    is_and_p,
    is_not_p,
    is_or_p,
)

from predicate import (
    always_false_p,
    always_true_p,
    can_optimize,
    optimize,
)


def test_optimize_not_or(p):
    # ~(p | ~p) == False

    predicate = ~(p | ~p)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_not_and(p):
    # ~(p & ~p) == True

    predicate = ~(p & ~p)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_not_xor_p_q(p, q):
    # ~(p ^ q) == ~p ^ q

    predicate = ~(p ^ q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p ^ q


def test_optimize_not_xor_not_p_q(p, q):
    # ~(~p ^ q) == p ^ q

    predicate = ~(~p ^ q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_not_xor_p_not_q(p, q):
    # ~(p ^ ~q) == p ^ q

    predicate = ~(p ^ ~q)

    assert is_not_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_or_1(p, q):
    # p | (~p & q) == p | q

    predicate = p | (~p & q)

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p | q


def test_optimize_and_1(p, q):
    # p & (~p | q) == p & q

    predicate = p & (~p | q)

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & q


def test_optimize_and_2(p, q):
    # p & (q | ~p) == p & q

    predicate = p & (q | ~p)

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & q


def test_optimize_and_3(p, q):
    # (~p | q) & p == q & p

    predicate = (~p | q) & p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q & p


def test_optimize_and_4(p, q):
    # (q | ~p) & p == q & p

    predicate = (q | ~p) & p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q & p


def test_optimize_xor_1(p, q):
    # p ^ (^p & q) = ~(p | q)

    predicate = p ^ (~p & q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_2(p, q):
    # p ^ (q & ~p) = ~(p | q)

    predicate = p ^ (q & ~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_3(p, q):
    # (q & ~p) ^ p = ~(p | q)

    predicate = (q & ~p) ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_4(p, q):
    # (~p & q) ^ p = ~(p | q)

    predicate = (~p & q) ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~(p | q)


def test_optimize_xor_5(p, q):
    # p ^ (p & q) = p & ~q

    predicate = p ^ (p & q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & ~q


def test_optimize_xor_or_left_left(p, q):
    # p ^ (p | q) = q

    predicate = p ^ (p | q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


def test_optimize_xor_or_left_right(p, q):
    # p ^ (q | p) = q

    predicate = p ^ (q | p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


def test_optimize_xor_or_right_left(p, q):
    # (p | q) ^ p = q

    predicate = (p | q) ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


def test_optimize_xor_or_right_right(p, q):
    # (q | p) ^ p = q

    predicate = (q | p) ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q
