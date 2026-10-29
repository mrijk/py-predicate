import pytest
from helpers import (
    is_and_p,
)

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    can_optimize,
    eq_p,
    ge_p,
    gt_p,
    le_p,
    lt_p,
    ne_p,
    optimize,
)


def test_can_optimize_returns_false_for_leaf():
    from predicate import eq_p

    assert can_optimize(eq_p(2)) is False


def test_optimize_not_or(p):
    # ~(p | ~p) == False

    predicate = ~(p | ~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_not_and(p):
    # ~(p & ~p) == True

    predicate = ~(p & ~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_not_xor_p_q(p, q):
    # ~(p ^ q) == ~p ^ q

    predicate = ~(p ^ q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p ^ q


def test_optimize_not_xor_not_p_q(p, q):
    # ~(~p ^ q) == p ^ q

    predicate = ~(~p ^ q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_not_xor_p_not_q(p, q):
    # ~(p ^ ~q) == p ^ q

    predicate = ~(p ^ ~q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_or_1(p, q):
    # p | (~p & q) == p | q

    predicate = p | (~p & q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p | q


def test_optimize_and_1(p, q):
    # p & (~p | q) == p & q

    predicate = p & (~p | q)

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
    # p ^ (p | q) = ~p & q

    predicate = p ^ (p | q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p & q


def test_optimize_xor_or_left_right(p, q):
    # p ^ (q | p) = ~p & q

    predicate = p ^ (q | p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p & q


def test_optimize_xor_or_right_left(p, q):
    # (p | q) ^ p = q & ~p

    predicate = (p | q) ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q & ~p


def test_optimize_xor_or_right_right(p, q):
    # (q | p) ^ p = q & ~p

    predicate = (q | p) ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q & ~p


_numbers = [-100, -1, 0, 1, 2, 5, 100]
_lists = [[], [0], [1], [-1, 0], [0, 5], [-5, -1]]


@pytest.mark.parametrize(
    "predicate, values",
    [
        # any_p(ne_p(v)) and ~all_p(eq_p(v)) rewrote into each other
        (all_p(eq_p(0)) | ((all_p(eq_p(1)) & any_p(ne_p(0))) | all_p(eq_p(2))), _lists),
        # ~any_p(p) and all_p(~p) rewrote into each other when ~p doesn't simplify
        (all_p(ge_p(0)) ^ (~any_p(ne_p(0) | le_p(0)) ^ all_p(ge_p(0))), _lists),
        (~all_p(eq_p(0) ^ le_p(0)) & (any_p(eq_p(3)) & ~all_p(gt_p(0))), _lists),
        # (p | q) & (r ^ s): the and-optimizer swapped the two sides back and forth
        ((le_p(0) | eq_p(5)) & (gt_p(0) ^ lt_p(0)), _numbers),
        ((gt_p(0) ^ lt_p(0)) & (le_p(0) | eq_p(5)), _numbers),
        # (p ^ q) & (r ^ s): the same swap with an Xor on both sides
        ((eq_p(1) ^ eq_p(2)) & (eq_p(3) ^ eq_p(4)), _numbers),
    ],
)
def test_optimize_terminates(predicate, values):
    # Used to raise RecursionError; the result must still give the same answers
    optimized = optimize(predicate)

    assert [optimized(v) for v in values] == [predicate(v) for v in values]
