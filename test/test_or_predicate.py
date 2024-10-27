from helpers import is_or_p

from predicate import (
    AlwaysTruePredicate,
    OrPredicate,
    always_false_p,
    always_true_p,
    ge_p,
    gt_p,
    le_p,
    lt_p,
)
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.standard_predicates import any_p, is_none_p, is_not_none_p


def test_or():
    ge_4 = ge_p(4)
    le_2 = le_p(2)

    le_2_or_ge_4 = le_2 | ge_4

    assert le_2_or_ge_4(2) is True
    assert le_2_or_ge_4(4) is True
    assert le_2_or_ge_4(3) is False


def test_or_commutative():
    lt_2 = lt_p(2)
    gt_4 = gt_p(4)

    p_1 = lt_2 | gt_4
    assert p_1(1) is True
    assert p_1(3) is False
    assert p_1(5) is True

    p_2 = gt_4 | lt_2
    assert p_2(1) is True
    assert p_2(3) is False
    assert p_2(5) is True


def test_or_always_true():
    always_true = is_none_p | is_not_none_p
    assert always_true(13) is True
    assert always_true(None) is True


def test_or_optimize_true_left():
    """True | p == True"""
    lt_2 = lt_p(2)
    always_true = always_true_p | lt_2

    assert is_or_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_or_optimize_right_false():
    """P | False == p"""
    lt_2 = lt_p(2)
    lt_2_or_false = lt_2 | always_false_p

    assert isinstance(lt_2_or_false, OrPredicate)
    assert can_optimize(lt_2_or_false) is True

    optimized = optimize(lt_2_or_false)

    assert isinstance(optimized, type(lt_2))


def test_or_optimize_left_false():
    """False | p == p"""
    lt_2 = lt_p(2)
    false_or_lt_2 = always_false_p | lt_2

    assert is_or_p(false_or_lt_2)
    assert can_optimize(false_or_lt_2) is True

    optimized = optimize(false_or_lt_2)

    assert isinstance(optimized, type(lt_2))


def test_or_optimize_true_right():
    """P | True == True"""
    lt_2 = lt_p(2)
    always_true = lt_2 | always_true_p

    assert is_or_p(always_true)
    assert can_optimize(always_true) is True

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_or_optimize_eq():
    """P | p == p"""
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


def test_or_optimize_not_same():
    """P | ~p == True"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)

    predicate = p_1 | ~p_2

    assert is_or_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_or_optimize_not_not_same():
    """P | ~q with p != q"""
    p_1 = gt_p(2)
    p_2 = gt_p(3)

    predicate = p_1 | ~p_2

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
