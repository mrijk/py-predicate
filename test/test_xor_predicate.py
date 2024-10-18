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
    NotPredicate,
)


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

    assert isinstance(always_true, XorPredicate)
    assert can_optimize(always_true) is True

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_xor_optimize_false_false():
    """False ^ False == False"""
    xor_false = always_false_p ^ always_false_p

    assert isinstance(xor_false, XorPredicate)
    assert can_optimize(xor_false) is True

    optimized = optimize(xor_false)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_xor_optimize_true_true():
    """False ^ False == False"""
    xor_true = always_true_p ^ always_true_p

    assert isinstance(xor_true, XorPredicate)
    assert can_optimize(xor_true) is True

    optimized = optimize(xor_true)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_xor_optimize_eq():
    """p ^ p == False"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 ^ p_2

    assert isinstance(same, XorPredicate)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysFalsePredicate)

    not_same = p_1 ^ p_3

    assert isinstance(not_same, XorPredicate)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, XorPredicate)


def test_xor_optimize_not():
    """p ^ ~p == True"""
    p_1 = gt_p(2)
    p_2 = gt_p(2)
    p_3 = gt_p(3)

    same = p_1 ^ ~p_2

    assert isinstance(same, XorPredicate)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysTruePredicate)

    same = ~p_1 ^ p_2

    assert isinstance(same, XorPredicate)
    assert can_optimize(same) is True

    optimized = optimize(same)

    assert isinstance(optimized, AlwaysTruePredicate)

    not_same = p_1 ^ p_3

    assert isinstance(not_same, XorPredicate)
    assert can_optimize(not_same) is False

    not_optimized = optimize(not_same)

    assert isinstance(not_optimized, XorPredicate)


def test_xor_optimize_always_false_right():
    """a ^ False == a"""
    ge_2 = ge_p(2)

    ge_2_xor_false = ge_2 ^ always_false_p

    assert isinstance(ge_2_xor_false, XorPredicate)
    assert can_optimize(ge_2_xor_false) is True

    optimized = optimize(ge_2_xor_false)

    assert not isinstance(optimized, XorPredicate)


def test_xor_optimize_always_false_left():
    """False ^ a == a"""
    ge_2 = ge_p(2)

    false_xor_ge_2 = always_false_p ^ ge_2

    assert isinstance(false_xor_ge_2, XorPredicate)
    assert can_optimize(false_xor_ge_2) is True

    optimized = optimize(false_xor_ge_2)

    assert not isinstance(optimized, XorPredicate)


def test_xor_optimize_always_true_right():
    """a ^ True == ~a"""
    ge_2 = ge_p(2)

    ge_2_xor_true = ge_2 ^ always_true_p

    assert isinstance(ge_2_xor_true, XorPredicate)
    assert can_optimize(ge_2_xor_true) is True

    optimized = optimize(ge_2_xor_true)

    assert isinstance(optimized, NotPredicate)


def test_xor_optimize_always_true_left():
    """True ^ a == ~a"""
    ge_2 = ge_p(2)

    true_xor_ge_2 = always_true_p ^ ge_2

    assert isinstance(true_xor_ge_2, XorPredicate)
    assert can_optimize(true_xor_ge_2) is True

    optimized = optimize(true_xor_ge_2)

    assert isinstance(optimized, NotPredicate)
