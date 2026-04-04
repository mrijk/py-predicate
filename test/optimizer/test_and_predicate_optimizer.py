import pytest
from helpers import is_eq_p

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    eq_p,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    in_p,
    is_empty_p,
    is_none_p,
    is_not_none_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
)
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.set_predicates import is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p
from predicate.standard_predicates import (
    is_int_p,
    is_str_p,
)


@pytest.mark.skip
def test_and_optimize_right_false(p):
    # p & False == False
    predicate = p & always_false_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_and_optimize_right_true(p):
    # p & True == p
    predicate = p & always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.skip
def test_and_optimize_left_false(p):
    # False & p == False
    predicate = always_false_p & p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_and_optimize_left_true(p):
    # True & p == p
    predicate = always_true_p & p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.parametrize(
    "left, right, expected, description",
    [
        (always_false_p, always_false_p, always_false_p, "False & False == False"),
        (always_false_p, always_true_p, always_false_p, "False & True == False"),
        (always_true_p, always_false_p, always_false_p, "True & False == False"),
        (always_true_p, always_true_p, always_true_p, "True & True == True"),
    ],
)
@pytest.mark.skip
def test_and_truth_combinations(left, right, expected, description):
    predicate = left & right

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == expected, description


@pytest.mark.skip
def test_and_optimize_eq_single_p(p):
    # p == p

    same = p

    assert not can_optimize(same)

    optimized = optimize(same)

    assert optimized == p


@pytest.mark.skip
def test_and_optimize_eq_multiple_p(p):
    # p & p & p == p

    same = p & p

    assert can_optimize(same)

    optimized = optimize(same)

    assert optimized == p


@pytest.mark.skip
def test_and_optimize_eq_nested_one(p, q):
    # p & q & p == p & q

    same = p & q & p

    assert can_optimize(same)

    optimized = optimize(same)

    assert optimized == p & q


@pytest.mark.skip
def test_and_optimize_eq_nested_two(p, q, r):
    # p & q & r & p == p & q & r

    same = p & q & r & p

    assert can_optimize(same)

    optimized = optimize(same)

    assert optimized == p & q & r


@pytest.mark.skip
def test_and_optimize_eq_complex(p, q, r):
    # p & q & r & p == p & q & r

    predicate = (p & q) & (p & ~q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_and_not_optimize_eq(p, q):
    # p & q == p & q

    not_same = p & q

    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == p & q


@pytest.mark.skip
def test_and_optimize_not_right(p):
    # p & ~p == False

    same = p & ~p

    assert can_optimize(same)

    optimized = optimize(same)

    assert optimized == always_false_p


@pytest.mark.skip
def test_and_optimize_not_right_different(p, q):
    not_same = p & ~q

    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == p & ~q


@pytest.mark.skip
def test_and_optimize_not_left(p):
    # ~p & p == False

    same = ~p & p

    assert can_optimize(same)

    optimized = optimize(same)

    assert optimized == always_false_p


@pytest.mark.skip
def test_and_optimize_not_left_different(p, q):
    not_same = ~p & q

    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == ~p & q


@pytest.mark.skip
def test_optimize_eq_v1_eq_v2():
    # x == v1 & x == v2 & v1 != v2 => False
    p1 = eq_p(2)
    p2 = eq_p(3)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_eq_v1_eq_v1():
    # x == v1 & x == v1 => x == v1
    p1 = eq_p(2)
    p2 = eq_p(2)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p1


@pytest.mark.skip
def test_optimize_eq_v1_ge_v1():
    # x = v & x >= v => x = v
    p1 = eq_p(2)
    p2 = ge_p(2)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert is_eq_p(optimized)
    assert optimized == p1


@pytest.mark.skip
def test_optimize_eq_v1_ge_v2():
    # x = v & x >= w & w > v => False
    p1 = eq_p(2)
    p2 = ge_p(1)

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p1


@pytest.mark.skip
def test_optimize_le_v1_le_v2():
    # le(v1) & le(v2) == le(min(v1, v2))
    predicate = le_p(5) & le_p(2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == le_p(2)


@pytest.mark.skip
def test_optimize_lt_v1_lt_v2():
    # lt(v1) & lt(v2) == lt(min(v1, v2))
    predicate = lt_p(5) & lt_p(2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(2)


@pytest.mark.skip
def test_optimize_ge_v1_le_v2():
    ge_2 = ge_p(2)
    le_3 = le_p(3)

    predicate = ge_2 & le_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_le_p(lower=2, upper=3)


@pytest.mark.skip
def test_optimize_ge_v1_le_v2_v1_is_v2():
    ge_2 = ge_p(2)
    le_2 = le_p(2)

    predicate = ge_2 & le_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(2)


@pytest.mark.skip
def test_optimize_ge_v1_le_v2_v1_ge_v2():
    ge_3 = ge_p(3)
    le_2 = le_p(2)

    predicate = ge_3 & le_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_ge_v1_lt_v2():
    ge_2 = ge_p(2)
    lt_3 = lt_p(3)

    predicate = ge_2 & lt_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_lt_p(lower=2, upper=3)


@pytest.mark.skip
def test_optimize_ge_v1_lt_v2_v1_is_v2():
    ge_2 = ge_p(2)
    lt_2 = lt_p(2)

    predicate = ge_2 & lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_ge_v1_lt_v2_v1_ge_v2():
    ge_3 = ge_p(3)
    lt_2 = lt_p(2)

    predicate = ge_3 & lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_gt_v1_le_v2():
    gt_2 = gt_p(2)
    le_3 = le_p(3)

    predicate = gt_2 & le_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_le_p(lower=2, upper=3)


@pytest.mark.skip
def test_optimize_gt_v1_le_v2_v1_is_v2():
    gt_2 = gt_p(2)
    le_2 = le_p(2)

    predicate = gt_2 & le_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_gt_v1_le_v2_v1_ge_v2():
    gt_3 = gt_p(3)
    le_2 = le_p(2)

    predicate = gt_3 & le_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_gt_v1_lt_v2():
    gt_2 = gt_p(2)
    lt_3 = lt_p(3)

    predicate = gt_2 & lt_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_lt_p(lower=2, upper=3)


@pytest.mark.skip
def test_optimize_gt_v1_lt_v2_v1_is_v2():
    gt_2 = gt_p(2)
    lt_2 = lt_p(2)

    predicate = gt_2 & lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_gt_v1_lt_v2_v1_ge_v2():
    gt_3 = gt_p(3)
    lt_2 = lt_p(2)

    predicate = gt_3 & lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_and_all():
    all_ge_2 = all_p(ge_p(2))
    all_ge_3 = all_p(ge_p(3))

    predicate = all_ge_2 & all_ge_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == all_ge_3


@pytest.mark.skip
def test_optimize_and_all_not():
    ge_2 = ge_p(2)
    all_ge_2 = all_p(ge_2)
    all_lt_2 = all_p(~ge_2)

    predicate = all_ge_2 & all_lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_empty_p

    assert optimized([])


@pytest.mark.skip
def test_optimize_none_and_not_none():
    # None & ~None => False
    predicate = is_none_p & is_not_none_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_not_none_and_none():
    # None & ~None => False
    predicate = is_not_none_p & is_none_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_in_and_in():
    p1 = in_p([2, 3])
    p2 = in_p([2, 3, 4])

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p({2, 3})


@pytest.mark.skip
def test_optimize_in_and_in_single():
    p1 = in_p([2, 3])
    p2 = in_p([3, 4])

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(3)


@pytest.mark.skip
def test_optimize_in_and_in_empty():
    p1 = in_p([2, 3])
    p2 = in_p([4, 5])

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_in_and_not_in():
    p1 = in_p([2, 3, 4])
    p2 = not_in_p([3, 5])

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p({2, 4})


@pytest.mark.skip
def test_optimize_in_and_not_in_single():
    p1 = in_p({2, 3, 4})
    p2 = not_in_p({2, 3})

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(4)


@pytest.mark.skip
def test_optimize_in_and_not_in_empty():
    p1 = in_p({2, 3})
    p2 = not_in_p({2, 3, 4})

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_not_in_and_not_in():
    p = not_in_p({2, 3, 4})
    q = not_in_p({3, 5})

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p({2, 3, 4, 5})


@pytest.mark.skip
def test_optimize_not_in_and_not_in_single():
    p1 = not_in_p({2})
    p2 = not_in_p({2})

    predicate = p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(2)


@pytest.mark.skip
def test_optimize_not_in_and_not_in_empty():
    p = not_in_p({})
    q = not_in_p({})

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


@pytest.mark.skip
def test_optimize_in_and_eq():
    p = in_p({2, 3, 4})
    q = eq_p(2)

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


@pytest.mark.skip
def test_optimize_nested_and():
    p1 = in_p({2, 3, 4})
    p2 = not_in_p({3})

    predicate = always_false_p & p1 & p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_nested_and_2(p, q):
    predicate = p & (q & ~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_nested_and_3(p, q, r, s):
    predicate = p & q & r & s & ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_nested_and_4(p, q, r):
    predicate = p & (q & r) & ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_ge_and_lt_false():
    ge_4 = ge_p(4)
    lt_4 = lt_p(4)

    predicate = ge_4 & lt_4

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_fn_and_eq_false():
    p = fn_p(lambda x: x * x > 5)
    q = eq_p(2)

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_fn_and_eq_true():
    p = fn_p(lambda x: x * x > 5)
    q = eq_p(3)

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


@pytest.mark.skip
def test_optimize_is_instance_different():
    predicate = is_int_p & is_str_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_is_subset():
    p = is_subset_p({1, 2, 3})
    q = is_real_subset_p({1, 2, 3})

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


@pytest.mark.skip
def test_optimize_is_superset():
    p = is_superset_p({1, 2, 3})
    q = is_real_superset_p({1, 2, 3})

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


@pytest.mark.skip
def test_optimize_is_subset_subset():
    p = is_subset_p({1, 2, 3})
    q = is_subset_p({2, 3, 4})

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_subset_p({2, 3})


@pytest.mark.skip
def test_optimize_is_subset_subset_empty():
    p = is_subset_p({1, 2, 3})
    q = is_subset_p({4, 5, 6})

    predicate = p & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_ne_and_gt():
    # ne(5) & gt(5) = gt(5)  [gt implies ne]

    predicate = ne_p(5) & gt_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_p(5)


@pytest.mark.skip
def test_optimize_gt_and_ne():
    # gt(5) & ne(5) = gt(5)  [gt implies ne, symmetric]

    predicate = gt_p(5) & ne_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_p(5)


@pytest.mark.skip
def test_optimize_ne_and_lt():
    # ne(5) & lt(5) = lt(5)  [lt implies ne]

    predicate = ne_p(5) & lt_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(5)


@pytest.mark.skip
def test_optimize_lt_and_ne():
    # lt(5) & ne(5) = lt(5)  [lt implies ne, symmetric]

    predicate = lt_p(5) & ne_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(5)


@pytest.mark.skip
def test_optimize_absorption_and_or(p, q):
    # p & (p | q) = p  [absorption]

    predicate = p & (p | q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.skip
def test_optimize_absorption_or_and(p, q):
    # (p | q) & p = p  [absorption, symmetric]

    predicate = (p | q) & p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.skip
def test_optimize_xor_and_left(p, q):
    # (p ^ q) & p = p & ~q

    predicate = (p ^ q) & p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & ~q


@pytest.mark.skip
def test_optimize_xor_and_right(p, q):
    # (p ^ q) & q = ~p & q

    predicate = (p ^ q) & q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p & q


@pytest.mark.skip
def test_optimize_and_xor_left(p, q):
    # p & (p ^ q) = p & ~q  [symmetric]

    predicate = p & (p ^ q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p & ~q


@pytest.mark.skip
def test_optimize_and_xor_right(p, q):
    # q & (p ^ q) = ~p & q  [symmetric]

    predicate = q & (p ^ q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p & q


@pytest.mark.skip
def test_optimize_le_ge_reversed():
    # le(v2) & ge(v1) => ge_le(v1, v2)  — reversed operand order

    assert optimize(le_p(3) & ge_p(1)) == ge_le_p(lower=1, upper=3)


@pytest.mark.skip
def test_optimize_le_gt_reversed():
    # le(v2) & gt(v1) => gt_le(v1, v2)  — reversed operand order

    assert optimize(le_p(3) & gt_p(1)) == gt_le_p(lower=1, upper=3)


@pytest.mark.skip
def test_optimize_lt_ge_reversed():
    # lt(v2) & ge(v1) => ge_lt(v1, v2)  — reversed operand order

    assert optimize(lt_p(3) & ge_p(1)) == ge_lt_p(lower=1, upper=3)


@pytest.mark.skip
def test_optimize_lt_gt_reversed():
    # lt(v2) & gt(v1) => gt_lt(v1, v2)  — reversed operand order

    assert optimize(lt_p(3) & gt_p(1)) == gt_lt_p(lower=1, upper=3)
