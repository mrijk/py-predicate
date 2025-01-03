from helpers import is_false_p, is_true_p, is_xor_p

from predicate import always_false_p, always_true_p, can_optimize, ge_p, gt_p, in_p, le_p, optimize
from predicate.standard_predicates import all_p, eq_p, lt_p


def test_xor_optimize_false_true():
    # False ^ True = True
    predicate = always_false_p ^ always_true_p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_xor_optimize_true_false():
    # True ^ False = True
    predicate = always_true_p ^ always_false_p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_xor_optimize_false_false():
    # False ^ False = False
    xor_false = always_false_p ^ always_false_p

    assert is_xor_p(xor_false)
    assert can_optimize(xor_false)

    optimized = optimize(xor_false)

    assert is_false_p(optimized)


def test_xor_optimize_true_true():
    # True ^ True = False
    predicate = always_true_p ^ always_true_p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_xor_optimize_eq():
    # p ^ p = False
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 ^ p_2

    assert is_xor_p(same)
    assert can_optimize(same)

    optimized = optimize(same)

    assert is_false_p(optimized)

    not_same = p_1 ^ p_3

    assert is_xor_p(not_same)
    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert is_xor_p(not_optimized)


def test_xor_optimize_not():
    # P ^ ~p = True
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 ^ ~p_2

    assert is_xor_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert is_true_p(optimized)

    same = ~p_1 ^ p_2

    assert is_xor_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert is_true_p(optimized)

    not_same = p_1 ^ p_3

    assert is_xor_p(not_same)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert is_xor_p(not_optimized)


def test_xor_optimize_false_right(p):
    # p ^ False == p

    predicate = p ^ always_false_p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_xor_optimize_false_left(p):
    # False ^ p = p

    predicate = always_false_p ^ p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_xor_optimize_true_right(p):
    # p ^ True = ~p
    p = ge_p(2)

    predicate = p ^ always_true_p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(2)


def test_xor_optimize_true_left():
    # True ^ p = ~p
    p = ge_p(2)

    predicate = always_true_p ^ p

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(2)


def test_xor_optimize_not_not():
    # ~p ^ ~q = p ^ q
    p = all_p(ge_p(2))
    q = all_p(le_p(3))

    predicate = ~p ^ ~q

    assert is_xor_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_xor_optimize_xor_left():
    # p ^ q ^ p = q
    p = all_p(ge_p(2))
    q = all_p(le_p(3))

    predicate = p ^ q ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


def test_xor_optimize_xor_right():
    # p ^ q ^ q = p
    p = all_p(ge_p(2))
    q = all_p(le_p(3))

    predicate = p ^ q ^ q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_optimize_in_xor_in():
    p1 = in_p(2, 3)
    p2 = in_p(4, 5)

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 3, 4, 5)


def test_optimize_in_xor_in_empty():
    p1 = in_p(2, 3, 4)
    p2 = in_p(2, 3, 4)

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_in_xor_in_single():
    p1 = in_p(2, 3)
    p2 = in_p(2)

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(3)
