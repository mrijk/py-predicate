from helpers import is_and_p, is_eq_p, is_false_p, is_true_p

from predicate import always_false_p, always_true_p, ge_p, gt_p, le_p, lt_p
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.predicate import is_empty_p
from predicate.standard_predicates import all_p, eq_p


def test_and():
    ge_2 = ge_p(2)
    le_3 = le_p(3)

    between_2_and_3 = ge_2 & le_3

    assert is_and_p(between_2_and_3)

    assert between_2_and_3(2) is True
    assert between_2_and_3(3) is True
    assert between_2_and_3(0) is False
    assert between_2_and_3(4) is False


def test_and_commutative():
    """A & b == b & a"""
    gt_2 = gt_p(2)
    lt_4 = lt_p(4)

    p_1 = gt_2 & lt_4
    assert p_1(2) is False
    assert p_1(4) is False
    assert p_1(3) is True

    p_2 = lt_4 & gt_2
    assert p_2(2) is False
    assert p_2(4) is False
    assert p_2(3) is True


def test_and_associative():
    # TODO
    pass


def test_and_optimize_right_false():
    """P & False == False"""
    ge_4 = ge_p(4)
    predicate = ge_4 & always_false_p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_false_p(optimized)


def test_and_optimize_right_true():
    """P & True == p"""
    ge_4 = ge_p(4)
    predicate = ge_4 & always_true_p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert not is_and_p(optimized)


def test_and_optimize_left_false():
    """False & p == False"""
    ge_4 = ge_p(4)
    predicate = always_false_p & ge_4

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_false_p(optimized)


def test_and_optimize_left_true():
    """True & p & == p"""
    ge_4 = ge_p(4)
    predicate = always_true_p & ge_4

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert not is_and_p(optimized)


def test_and_optimize_false_and_false():
    """False & False == False"""
    always_false = always_false_p & always_false_p

    assert is_and_p(always_false)
    assert can_optimize(always_false)

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_and_optimize_true_and_true():
    """True & True == True"""
    always_true = always_true_p & always_true_p

    assert is_and_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert is_true_p(optimized)


def test_and_optimize_true_and_false():
    """True & False == False"""
    always_false = always_true_p & always_false_p

    assert is_and_p(always_false)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_and_optimize_false_and_true():
    """False & True == False"""
    always_false = always_false_p & always_true_p

    assert is_and_p(always_false)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_and_optimize_eq():
    """P & p == p"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 & p_2

    assert is_and_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert not is_and_p(optimized)

    not_same = p_1 & p_3

    assert is_and_p(not_same)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert is_and_p(not_optimized)


def test_and_optimize_not_right():
    """P & ~p == False"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 & ~p_2

    assert is_and_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert is_false_p(optimized)

    not_same = p_1 & ~p_3

    assert is_and_p(not_same)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert is_and_p(not_optimized)


def test_and_optimize_not_left():
    """~p & p == False"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = ~p_1 & p_2

    assert is_and_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert is_false_p(optimized)

    not_same = p_1 & ~p_3

    assert is_and_p(not_same)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert is_and_p(not_optimized)


def test_optimize_eq_v1_eq_v2():
    # x == v1 & x == v2 & v1 != v2 => False
    p1 = eq_p(2)
    p2 = eq_p(3)

    predicate = p1 & p2

    assert can_optimize(predicate) is True

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_eq_v1_eq_v1():
    # x == v1 & x == v1 => x == v1
    p1 = eq_p(2)
    p2 = eq_p(2)

    predicate = p1 & p2

    assert can_optimize(predicate) is True

    optimized = optimize(predicate)

    assert optimized == p1


def test_optimize_eq_v1_ge_v1():
    # x = v & x >= v => x = v
    p1 = eq_p(2)
    p2 = ge_p(2)

    predicate = p1 & p2

    assert can_optimize(predicate) is True

    optimized = optimize(predicate)

    assert is_eq_p(optimized)
    assert optimized == p1


def test_optimize_eq_v1_ge_v2():
    # x = v & x >= w & w > v => False
    p1 = eq_p(2)
    p2 = ge_p(3)

    predicate = p1 & p2

    assert can_optimize(predicate) is True

    optimized = optimize(predicate)

    assert is_false_p(optimized)


def test_optimize_and_all():
    all_ge_2 = all_p(ge_p(2))
    all_ge_3 = all_p(ge_p(3))

    predicate = all_ge_2 & all_ge_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == all_ge_3


def test_optimize_and_all_not():
    ge_2 = ge_p(2)
    all_ge_2 = all_p(ge_2)
    all_lt_2 = all_p(~ge_2)

    predicate = all_ge_2 & all_lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_empty_p

    assert optimized([])
