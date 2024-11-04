from helpers import is_and_p, is_eq_p, is_false_p, is_true_p

from predicate import always_false_p, always_true_p, ge_p, gt_p
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.predicate import is_empty_p
from predicate.standard_predicates import all_p, eq_p, fn_p, in_p, is_none_p, is_not_none_p, lt_p, ne_p, not_in_p


def test_and_optimize_right_false():
    # p & False == False
    ge_4 = ge_p(4)
    predicate = ge_4 & always_false_p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_false_p(optimized)


def test_and_optimize_right_true():
    # p & True == p
    ge_4 = ge_p(4)
    predicate = ge_4 & always_true_p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert not is_and_p(optimized)


def test_and_optimize_left_false():
    # False & p == False
    ge_4 = ge_p(4)
    predicate = always_false_p & ge_4

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_false_p(optimized)


def test_and_optimize_left_true():
    # True & p == p
    ge_4 = ge_p(4)
    predicate = always_true_p & ge_4

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert not is_and_p(optimized)


def test_and_optimize_false_and_false():
    # False & False == False
    always_false = always_false_p & always_false_p

    assert is_and_p(always_false)
    assert can_optimize(always_false)

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_and_optimize_true_and_true():
    # True & True == True
    always_true = always_true_p & always_true_p

    assert is_and_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert is_true_p(optimized)


def test_and_optimize_true_and_false():
    # True & False == False
    always_false = always_true_p & always_false_p

    assert is_and_p(always_false)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_and_optimize_false_and_true():
    # False & True == False
    always_false = always_false_p & always_true_p

    assert is_and_p(always_false)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_and_optimize_eq():
    # p & p == p
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
    # p & ~p == False
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
    # ~p & p == False
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


def test_optimize_none_and_not_none():
    # None & ~None => False
    predicate = is_none_p & is_not_none_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_not_none_and_none():
    # None & ~None => False
    predicate = is_not_none_p & is_none_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_in_and_in():
    p1 = in_p(2, 3)
    p2 = in_p(3, 4)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(3)


def test_optimize_in_and_not_in():
    p1 = in_p(2, 3, 4)
    p2 = not_in_p(3, 5)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 4)


def test_optimize_in_and_not_in_single():
    p1 = in_p(2, 3, 4)
    p2 = not_in_p(2, 3)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(4)


def test_optimize_in_and_not_in_empty():
    p1 = in_p(2, 3, 4)
    p2 = not_in_p(2, 3, 4)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_not_in_and_not_in():
    p1 = not_in_p(2, 3, 4)
    p2 = not_in_p(3, 5)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p(2, 3, 4, 5)


def test_optimize_not_in_and_not_in_single():
    p1 = not_in_p(2)
    p2 = not_in_p(2)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(2)


def test_optimize_not_in_and_not_in_empty():
    p1 = not_in_p()
    p2 = not_in_p()

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_nested_and():
    p1 = in_p(2, 3, 4)
    p2 = not_in_p(3)

    predicate = always_false_p & p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


# def test_optimize_nested_and_2():
#     p1 = ge_p(2)
#     p2 = ge_p(3)
#     p3 = lt_p(2)
#
#     predicate = p1 & p2 & p3

# assert can_optimize(predicate)
#
# optimized = optimize(predicate)
#
# assert optimized == always_false_p


def test_optimize_ge_and_lt():
    ge_4 = ge_p(4)
    lt_4 = lt_p(4)

    predicate = ge_4 & lt_4

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_fn_and_eq_false():
    p = fn_p(lambda x: x * x > 5)
    q = eq_p(2)

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_fn_and_eq_true():
    p = fn_p(lambda x: x * x > 5)
    q = eq_p(3)

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p
