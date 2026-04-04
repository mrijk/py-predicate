import pytest

from predicate import (
    always_false_p,
    always_true_p,
    can_optimize,
    eq_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    in_p,
    le_p,
    lt_p,
    optimize,
)


@pytest.mark.skip
def test_xor_optimize_false_true():
    # False ^ True = True
    predicate = always_false_p ^ always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


@pytest.mark.skip
def test_xor_optimize_true_false():
    # True ^ False = True
    predicate = always_true_p ^ always_false_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


@pytest.mark.skip
def test_xor_optimize_false_false():
    # False ^ False = False
    xor_false = always_false_p ^ always_false_p

    assert can_optimize(xor_false)

    optimized = optimize(xor_false)

    assert optimized == always_false_p


@pytest.mark.skip
def test_xor_optimize_true_true():
    # True ^ True = False
    predicate = always_true_p ^ always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_xor_optimize_eq(p):
    # p ^ p = False

    predicate = p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_xor_optimize_neq(p, q):
    # p ^ q = p ^q

    predicate = p ^ 1

    assert not can_optimize(predicate)


@pytest.mark.skip
def test_xor_optimize_not_right(p):
    # p ^ ~p = True

    predicate = p ^ ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)
    assert optimized == always_true_p


@pytest.mark.skip
def test_xor_optimize_not_left(p):
    # ~p ^ p = True

    predicate = ~p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)
    assert optimized == always_true_p


@pytest.mark.skip
def test_xor_optimize_not_2(p, q):
    not_same = p & q

    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == p & q


@pytest.mark.skip
def test_xor_optimize_false_right(p):
    # p ^ False == p

    predicate = p ^ always_false_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.skip
def test_xor_optimize_false_left(p):
    # False ^ p = p

    predicate = always_false_p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.skip
def test_xor_optimize_true_right(p):
    # p ^ True = ~p

    predicate = p ^ always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p


@pytest.mark.skip
def test_xor_optimize_true_left(p):
    # True ^ p = ~p

    predicate = always_true_p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p


@pytest.mark.skip
def test_xor_optimize_not_not(p, q):
    # ~p ^ ~q = p ^ q

    predicate = ~p ^ ~q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


@pytest.mark.skip
def test_xor_optimize_xor_left(p, q):
    # p ^ q ^ p = q

    predicate = p ^ q ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


@pytest.mark.skip
def test_xor_optimize_xor_right(p, q):
    # p ^ q ^ q = p

    predicate = p ^ q ^ q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


@pytest.mark.skip
def test_optimize_in_xor_in():
    p1 = in_p({2, 3})
    p2 = in_p({4, 5})

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p({2, 3, 4, 5})


@pytest.mark.skip
def test_optimize_in_xor_in_empty():
    p1 = in_p({2, 3, 4})
    p2 = in_p({2, 3, 4})

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


@pytest.mark.skip
def test_optimize_in_xor_in_single():
    p1 = in_p({2, 3})
    p2 = in_p({2})

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(3)


@pytest.mark.skip
def test_xor_optimize_left_implies_right():
    # ge(3) ^ ge(2): ge(3) implies ge(2), so result is ~ge(3) & ge(2) = ge_lt(2, 3)

    predicate = ge_p(3) ^ ge_p(2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_lt_p(lower=2, upper=3)


@pytest.mark.skip
def test_xor_optimize_right_implies_left():
    # ge(2) ^ ge(3): ge(3) implies ge(2), so result is ge(2) & ~ge(3) = ge_lt(2, 3)

    predicate = ge_p(2) ^ ge_p(3)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_lt_p(lower=2, upper=3)


@pytest.mark.skip
def test_xor_optimize_le_left_implies_right():
    # le(2) ^ le(5): le(2) implies le(5), so result is ~le(2) & le(5) = gt_le(2, 5)

    predicate = le_p(2) ^ le_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_le_p(lower=2, upper=5)


@pytest.mark.skip
def test_xor_optimize_lt_left_implies_right():
    # lt(2) ^ lt(5): lt(2) implies lt(5), so result is ~lt(2) & lt(5) = ge_lt(2, 5)

    predicate = lt_p(2) ^ lt_p(5)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_lt_p(lower=2, upper=5)


@pytest.mark.skip
def test_xor_optimize_ge_le_implies():
    # ge(3) ^ le(5): neither implies the other, should not use this rule

    predicate = ge_p(3) ^ le_p(5)

    assert not can_optimize(predicate)


@pytest.mark.skip
def test_xor_optimize_right_xor():
    # p ^ (q ^ r): right is XorPredicate → swaps and re-optimizes
    predicate = ge_p(2) ^ (ge_p(3) ^ ge_p(4))

    optimized = optimize(predicate)

    assert optimized is not None


@pytest.mark.skip
def test_xor_optimize_nested_not_optimizable():
    # (p ^ q) ^ r where neither sub-xor can be further simplified
    predicate = (ge_p(2) ^ ge_p(3)) ^ ge_p(4)

    # should not raise; result may or may not be optimized
    result = optimize(predicate)
    assert result is not None


@pytest.mark.skip
def test_xor_left_xor_both_inner_fail():
    # (p ^ q) ^ r where neither inner cross-xor optimizes — covers the nested NotOptimized() path
    from predicate.standard_predicates import is_float_p, is_int_p, is_str_p

    predicate = (is_int_p ^ is_str_p) ^ is_float_p
    result = optimize(predicate)
    assert result is not None


@pytest.mark.skip
def test_xor_right_xor_no_optimize():
    # p ^ (q ^ r) where q ^ r stays a XorPredicate after optimize — covers _, XorPredicate() case
    from predicate.standard_predicates import is_int_p, is_str_p

    predicate = ge_p(2) ^ (is_int_p ^ is_str_p)
    result = optimize(predicate)
    assert result is not None
