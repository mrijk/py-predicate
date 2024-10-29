from helpers import is_or_p

from predicate import (
    AlwaysTruePredicate,
    OrPredicate,
    always_false_p,
    always_true_p,
    can_optimize,
    ge_p,
    gt_p,
    lt_p,
    optimize,
)
from predicate.predicate import FnPredicate
from predicate.standard_predicates import any_p


def test_or_optimize_true_left():
    # True | p == True
    lt_2 = lt_p(2)
    always_true = always_true_p | lt_2

    assert is_or_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_or_optimize_right_false():
    # p | False == p
    lt_2 = lt_p(2)
    lt_2_or_false = lt_2 | always_false_p

    assert isinstance(lt_2_or_false, OrPredicate)
    assert can_optimize(lt_2_or_false) is True

    optimized = optimize(lt_2_or_false)

    assert isinstance(optimized, type(lt_2))


def test_or_optimize_left_false():
    # False | p == p
    lt_2 = lt_p(2)
    false_or_lt_2 = always_false_p | lt_2

    assert is_or_p(false_or_lt_2)
    assert can_optimize(false_or_lt_2) is True

    optimized = optimize(false_or_lt_2)

    assert isinstance(optimized, type(lt_2))


def test_or_optimize_true_right():
    # p | True == True
    lt_2 = lt_p(2)
    always_true = lt_2 | always_true_p

    assert is_or_p(always_true)
    assert can_optimize(always_true) is True

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


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

    assert isinstance(not_same, OrPredicate)
    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, OrPredicate)


def test_or_optimize_right_not_same():
    # p | ~p == True
    p_1 = gt_p(2)
    p_2 = gt_p(2)

    predicate = p_1 | ~p_2

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


def test_optimize_to_xor_left():
    # (~p & q) | (p & ~q) == p ^ q
    p = FnPredicate(lambda x: x == 2)
    q = FnPredicate(lambda x: x in (2, 3))

    predicate = (~p & q) | (p & ~q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_optimize_to_xor_right():
    # (p & ~q) | (~p & q) == p ^ q
    p = FnPredicate(lambda x: x == 2)
    q = FnPredicate(lambda x: x in (2, 3))

    predicate = (p & ~q) | (~p & q)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q
