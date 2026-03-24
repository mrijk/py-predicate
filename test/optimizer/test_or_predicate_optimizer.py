from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    can_optimize,
    eq_p,
    ge_p,
    gt_p,
    in_p,
    is_empty_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
    optimize,
)


def test_or_optimize_true_left(p):
    # True | p == True
    predicate = always_true_p | p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_right_false(p):
    # p | False == p
    predicate = p | always_false_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_or_optimize_left_false(p):
    # False | p == p
    predicate = always_false_p | p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_or_optimize_true_right(p):
    # p | True == True
    predicate = p | always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_eq(p):
    # p | p == p
    same = p | p

    assert can_optimize(same)

    optimized = optimize(same)

    assert optimized == p


def test_or_optimize_eq_not_same(p, q):
    not_same = p | q

    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == not_same


def test_or_optimize_right_not_same(p):
    # p | ~p == True

    predicate = p | ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_right_not_same_after_optimization(p):
    # p | ~p == True

    q = all_p(p)
    r = any_p(~p)

    predicate = q | r

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_negate(p):
    # p | ~p == True
    predicate = p | ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_left_not_same(p):
    # ~p | p == True
    predicate = ~p | p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_not_not_same(p, q):
    # p | ~q with p != q
    predicate = p | q

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

    assert optimized == in_p({2, 3})


def test_optimize_in_and_in():
    p = in_p({2, 3})
    q = in_p({4, 5})

    predicate = p | q

    assert can_optimize(predicate)


def test_optimize_in_and_not_in():
    p = in_p({2, 3})
    q = not_in_p({2, 3, 4, 5})

    predicate = p | q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p({4, 5})


def test_optimize_in_and_not_in_single():
    p = in_p([2])
    q = not_in_p({2, 3})

    predicate = p | q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(3)


def test_optimize_in_and_not_in_empty():
    p1 = in_p({3, 4, 5})
    p2 = not_in_p({4, 5})

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_eq_or_in():
    p1 = eq_p(5)
    p2 = in_p({2, 3, 4})

    predicate = p1 | p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p({2, 3, 4, 5})


def test_or_optimize_in_or_eq():
    p = in_p({2, 3, 4})
    q = eq_p(5)

    predicate = p | q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p({2, 3, 4, 5})


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


def test_or_optimize_all_or_any(p):
    predicate = all_p(p) | any_p(p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_empty_p | any_p(p)


def test_or_optimize_any_or_all(p):
    predicate = any_p(p) | all_p(p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_empty_p | any_p(p)


def test_or_optimize_right_is_or():
    # p | (q | r): right is OrPredicate → triggers case _, OrPredicate() swap
    predicate = ge_p(2) | (ge_p(3) | le_p(1))

    result = optimize(predicate)

    assert result is not None


def test_optimize_ge_or_le_always_true():
    # ge(2) | le(5) = True when lower <= upper

    predicate = ge_p(2) | le_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_ge_or_le_equal_bounds():
    # ge(3) | le(3) = True (every x is either >= 3 or <= 3)

    predicate = ge_p(3) | le_p(3)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_le_or_ge_always_true():
    # le(5) | ge(2) = True when lower <= upper (symmetric)

    predicate = le_p(5) | ge_p(2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_ge_or_le_not_always_true():
    # ge(5) | le(2) is NOT always true (e.g. x=3 fails both)

    predicate = ge_p(5) | le_p(2)

    assert not can_optimize(predicate)


def test_optimize_eq_or_gt():
    # eq(5) | gt(5) = ge(5)

    predicate = eq_p(5) | gt_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_p(5)


def test_optimize_gt_or_eq():
    # gt(5) | eq(5) = ge(5)

    predicate = gt_p(5) | eq_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_p(5)


def test_optimize_eq_or_lt():
    # eq(5) | lt(5) = le(5)

    predicate = eq_p(5) | lt_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == le_p(5)


def test_optimize_lt_or_eq():
    # lt(5) | eq(5) = le(5)

    predicate = lt_p(5) | eq_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == le_p(5)


def test_optimize_not_in_or_not_in():
    # not_in({1, 2}) | not_in({2, 3}) = not_in({2})

    predicate = not_in_p({1, 2}) | not_in_p({2, 3})

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(2)


def test_optimize_not_in_or_not_in_disjoint():
    # not_in({1, 2}) | not_in({3, 4}) = always_true  [disjoint sets → empty intersection]

    predicate = not_in_p({1, 2}) | not_in_p({3, 4})

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_not_in_or_not_in_same():
    # not_in({1, 2}) | not_in({1, 2}) = not_in({1, 2})  [identical sets]

    predicate = not_in_p({1, 2}) | not_in_p({1, 2})

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p({1, 2})
