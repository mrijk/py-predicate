from predicate import always_false_p, always_true_p, can_optimize, eq_p, in_p, optimize


def test_xor_optimize_false_true():
    # False ^ True = True
    predicate = always_false_p ^ always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_xor_optimize_true_false():
    # True ^ False = True
    predicate = always_true_p ^ always_false_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_xor_optimize_false_false():
    # False ^ False = False
    xor_false = always_false_p ^ always_false_p

    assert can_optimize(xor_false)

    optimized = optimize(xor_false)

    assert optimized == always_false_p


def test_xor_optimize_true_true():
    # True ^ True = False
    predicate = always_true_p ^ always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_xor_optimize_eq(p):
    # p ^ p = False

    predicate = p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_xor_optimize_neq(p, q):
    # p ^ q = p ^q

    predicate = p ^ 1

    assert not can_optimize(predicate)


def test_xor_optimize_not_right(p):
    # p ^ ~p = True

    predicate = p ^ ~p

    assert can_optimize(predicate)

    optimized = optimize(predicate)
    assert optimized == always_true_p


def test_xor_optimize_not_left(p):
    # ~p ^ p = True

    predicate = ~p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)
    assert optimized == always_true_p


def test_xor_optimize_not_2(p, q):

    not_same = p & q

    assert not can_optimize(not_same)

    not_optimized = optimize(not_same)

    assert not_optimized == p & q


def test_xor_optimize_false_right(p):
    # p ^ False == p

    predicate = p ^ always_false_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_xor_optimize_false_left(p):
    # False ^ p = p

    predicate = always_false_p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_xor_optimize_true_right(p):
    # p ^ True = ~p

    predicate = p ^ always_true_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p


def test_xor_optimize_true_left(p):
    # True ^ p = ~p

    predicate = always_true_p ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~p


def test_xor_optimize_not_not(p, q):
    # ~p ^ ~q = p ^ q

    predicate = ~p ^ ~q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p ^ q


def test_xor_optimize_xor_left(p, q):
    # p ^ q ^ p = q

    predicate = p ^ q ^ p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == q


def test_xor_optimize_xor_right(p, q):
    # p ^ q ^ q = p

    predicate = p ^ q ^ q

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == p


def test_optimize_in_xor_in():
    p1 = in_p({2, 3})
    p2 = in_p({4, 5})

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p({2, 3, 4, 5})


def test_optimize_in_xor_in_empty():
    p1 = in_p({2, 3, 4})
    p2 = in_p({2, 3, 4})

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_in_xor_in_single():
    p1 = in_p({2, 3})
    p2 = in_p({2})

    predicate = p1 ^ p2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(3)
