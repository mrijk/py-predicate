from helpers import is_or_p

from predicate import (
    always_false_p,
    always_true_p,
    can_optimize,
    ge_p,
    gt_p,
    lt_p,
    optimize,
)
from predicate.standard_predicates import any_p, eq_p, in_p, le_p, ne_p, not_in_p


def test_or_optimize_true_left():
    # True | p == True
    lt_2 = lt_p(2)
    predicate = always_true_p | lt_2

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_right_false():
    # p | False == p
    lt_2 = lt_p(2)
    predicate = lt_2 | always_false_p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_2


def test_or_optimize_left_false():
    # False | p == p
    lt_2 = lt_p(2)
    false_or_lt_2 = always_false_p | lt_2

    assert is_or_p(false_or_lt_2)
    assert can_optimize(false_or_lt_2)

    optimized = optimize(false_or_lt_2)

    assert optimized == lt_2


def test_or_optimize_true_right():
    # p | True == True
    lt_2 = lt_p(2)
    always_true = lt_2 | always_true_p

    assert is_or_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert optimized == always_true_p


def test_or_optimize_eq():
    # p | p == p
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 | p_2

    assert is_or_p(same)
    assert can_optimize(same)

    optimized = optimize(same)

    assert not is_or_p(optimized)

    not_same = p_1 | p_3

    assert is_or_p(not_same)
    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == not_same


def test_or_optimize_right_not_same():
    # p | ~p == True
    p_1 = gt_p(2)
    p_2 = gt_p(2)

    predicate = p_1 | ~p_2

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_negate():
    # p | ~p == True
    p_1 = gt_p(2)
    p_2 = le_p(2)

    predicate = p_1 | p_2

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_left_not_same():
    # ~p | p == True
    p_1 = gt_p(2)
    p_2 = gt_p(2)

    predicate = ~p_1 | p_2

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_not_not_same():
    # p | ~q with p != q
    p = gt_p(2)
    q = gt_p(3)

    predicate = p | q

    assert is_or_p(predicate)
    assert not can_optimize(predicate)


def test_optimize_or_any():
    ge_2 = ge_p(2)
    ge_3 = ge_p(3)
    any_ge_2 = any_p(ge_2)
    any_ge_3 = any_p(ge_3)

    predicate = any_ge_2 | any_ge_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == any_p(ge_2)


def test_optimize_to_xor_left(p, q):
    # (~p & q) | (p & ~q) == p ^ q

    predicate = (~p & q) | (p & ~q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_to_xor_right(p, q):
    # (p & ~q) | (~p & q) == p ^ q

    predicate = (p & ~q) | (~p & q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_or_optimize_not_optimize(p, q, r, s):
    # (p & q) | (r & s)

    predicate = (p & q) | (r & s)

    assert not can_optimize(predicate)


def test_optimize_multiple_eq():
    # x == 2 or x == 3 => x in (2, 3)
    eq_2 = eq_p(2)
    eq_3 = eq_p(3)

    predicate = eq_2 | eq_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 3)


def test_optimize_in_and_not_in():
    p1 = in_p(2, 3)
    p2 = not_in_p(2, 3, 4, 5)

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p(4, 5)


def test_optimize_in_and_not_in_single():
    p1 = in_p(2)
    p2 = not_in_p(2, 3)

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(3)


def test_optimize_in_and_not_in_empty():
    p1 = in_p(2)
    p2 = not_in_p(2)

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_eq_or_in():
    p1 = eq_p(5)
    p2 = in_p(2, 3, 4)

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 3, 4, 5)


def test_or_optimize_in_or_eq():
    p1 = in_p(2, 3, 4)
    p2 = eq_p(5)

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 3, 4, 5)


def test_optimize_nested_or(p, q):
    r = ~p

    predicate = p | q | r

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p
