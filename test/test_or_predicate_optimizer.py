from helpers import is_or_p

from predicate import always_false_p, always_true_p, can_optimize, ge_p, gt_p, optimize
from predicate.standard_predicates import all_p, any_p, eq_p, in_p, ne_p, not_in_p


def test_or_optimize_true_left(p):
    # True | p == True
    predicate = always_true_p | p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_right_false(p):
    # p | False == p
    predicate = p | always_false_p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_or_optimize_left_false(p):
    # False | p == p
    predicate = always_false_p | p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_or_optimize_true_right(p):
    # p | True == True
    predicate = p | always_true_p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

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


def test_or_optimize_right_not_same(p):
    # p | ~p == True

    predicate = p | ~p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_right_not_same_after_optimization(p):
    # p | ~p == True

    q = all_p(p)
    r = any_p(~p)

    predicate = q | r

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_negate(p):
    # p | ~p == True
    predicate = p | ~p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_left_not_same(p):
    # ~p | p == True
    predicate = ~p | p

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_not_not_same(p, q):
    # p | ~q with p != q
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
    p = in_p(2, 3)
    q = not_in_p(2, 3, 4, 5)

    predicate = p | q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p(4, 5)


def test_optimize_in_and_not_in_single():
    p = in_p(2)
    q = not_in_p(2, 3)

    predicate = p | q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(3)


def test_optimize_in_and_not_in_empty():
    p1 = in_p(3, 4, 5)
    p2 = not_in_p(4, 5)

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
    p = in_p(2, 3, 4)
    q = eq_p(5)

    predicate = p | q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 3, 4, 5)


def test_optimize_nested_or(p, q):
    predicate = p | q | ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_nested_or_1(p, q, r, s):
    predicate = p | q | r | s | ~q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p
