from predicate import (
    AndPredicate,
    always_false_p,
    always_true_p,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
    ge_p,
    gt_p,
    le_p,
    lt_p,
)
from predicate.optimizer.predicate_optimizer import optimize, can_optimize
from helpers import is_and_p


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
    """a & b == b & a"""
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


def test_and_always_false():
    """p & False == False"""
    ge_4 = ge_p(4)
    always_false = ge_4 & always_false_p

    assert always_false.always_false is True
    assert always_false.always_true is False


def test_and_always_true():
    """True & True == True"""
    always_true = always_true_p & always_true_p

    assert always_true.always_false is False
    assert always_true.always_true is True


def test_and_optimize_right_false():
    """p & False == False"""
    ge_4 = ge_p(4)
    predicate = ge_4 & always_false_p

    assert is_and_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_and_optimize_right_true():
    """p & True == p"""
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

    assert isinstance(optimized, AlwaysFalsePredicate)


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

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_and_optimize_true_and_true():
    """True & True == True"""
    always_true = always_true_p & always_true_p

    assert isinstance(always_true, AndPredicate)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_and_optimize_true_and_false():
    """True & False == False"""
    always_false = always_true_p & always_false_p

    assert isinstance(always_false, AndPredicate)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_and_optimize_false_and_true():
    """False & True == False"""
    always_false = always_false_p & always_true_p

    assert isinstance(always_false, AndPredicate)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_and_optimize_eq():
    """p & p == p"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 & p_2

    assert isinstance(same, AndPredicate)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert not isinstance(optimized, AndPredicate)

    not_same = p_1 & p_3

    assert isinstance(not_same, AndPredicate)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, AndPredicate)


def test_and_optimize_not_right():
    """p & ~p == False"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 & ~p_2

    assert isinstance(same, AndPredicate)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysFalsePredicate)

    not_same = p_1 & ~p_3

    assert isinstance(not_same, AndPredicate)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, AndPredicate)


def test_and_optimize_not_left():
    """~p & p == False"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = ~p_1 & p_2

    assert isinstance(same, AndPredicate)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysFalsePredicate)

    not_same = p_1 & ~p_3

    assert isinstance(not_same, AndPredicate)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, AndPredicate)
