from predicate import (
    can_optimize,
    optimize,
    ge_p,
    always_true_p,
    XorPredicate,
    always_false_p,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
    gt_p,
)
from helpers import is_not_p, is_xor_p


def test_xor():
    """a ^ b"""
    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    ge_2_xor_ge_4 = ge_2 ^ ge_4

    assert ge_2_xor_ge_4(1) is False
    assert ge_2_xor_ge_4(2) is True
    assert ge_2_xor_ge_4(4) is False


def test_xor_commutative():
    """a ^ b == b ^ a"""
    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    ge_2_xor_ge_4 = ge_2 ^ ge_4

    assert ge_2_xor_ge_4(1) is False
    assert ge_2_xor_ge_4(2) is True
    assert ge_2_xor_ge_4(4) is False

    ge_4_xor_ge_4 = ge_4 ^ ge_2

    assert ge_4_xor_ge_4(1) is False
    assert ge_4_xor_ge_4(2) is True
    assert ge_4_xor_ge_4(4) is False


def test_xor_optimize_false_true():
    """False ^ True == True"""
    always_true = always_false_p ^ always_true_p

    assert is_xor_p(always_true)
    assert can_optimize(always_true) is True

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_xor_optimize_true_false():
    """True ^ False == True"""
    always_true = always_true_p ^ always_false_p

    assert is_xor_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_xor_optimize_false_false():
    """False ^ False == False"""
    xor_false = always_false_p ^ always_false_p

    assert is_xor_p(xor_false)
    assert can_optimize(xor_false)

    optimized = optimize(xor_false)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_xor_optimize_true_true():
    """True ^ True == False"""
    xor_true = always_true_p ^ always_true_p

    assert is_xor_p(xor_true)
    assert can_optimize(xor_true)

    optimized = optimize(xor_true)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_xor_optimize_eq():
    """p ^ p == False"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 ^ p_2

    assert is_xor_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysFalsePredicate)

    not_same = p_1 ^ p_3

    assert is_xor_p(not_same)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert is_xor_p(not_optimized)


def test_xor_optimize_not():
    """p ^ ~p == True"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 ^ ~p_2

    assert is_xor_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysTruePredicate)

    same = ~p_1 ^ p_2

    assert is_xor_p(same)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysTruePredicate)

    not_same = p_1 ^ p_3

    assert isinstance(not_same, XorPredicate)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, XorPredicate)


def test_xor_optimize_false_right():
    """a ^ False == a"""
    ge_2 = ge_p(2)

    ge_2_xor_false = ge_2 ^ always_false_p

    assert is_xor_p(ge_2_xor_false)
    assert can_optimize(ge_2_xor_false)

    optimized = optimize(ge_2_xor_false)

    assert not is_xor_p(optimized)


def test_xor_optimize_false_left():
    """False ^ a == a"""
    ge_2 = ge_p(2)

    false_xor_ge_2 = always_false_p ^ ge_2

    assert is_xor_p(false_xor_ge_2)
    assert can_optimize(false_xor_ge_2)

    optimized = optimize(false_xor_ge_2)

    assert not is_xor_p(optimized)


def test_xor_optimize__true_right():
    """a ^ True == ~a"""
    ge_2 = ge_p(2)

    ge_2_xor_true = ge_2 ^ always_true_p

    assert is_xor_p(ge_2_xor_true)
    assert can_optimize(ge_2_xor_true) is True

    optimized = optimize(ge_2_xor_true)

    assert is_not_p(optimized)


def test_xor_optimize_true_left():
    """True ^ a == ~a"""
    ge_2 = ge_p(2)

    true_xor_ge_2 = always_true_p ^ ge_2

    assert is_xor_p(true_xor_ge_2)
    assert can_optimize(true_xor_ge_2) is True

    optimized = optimize(true_xor_ge_2)

    assert is_not_p(optimized)
