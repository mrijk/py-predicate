from predicate import always_false_p, always_true_p, can_optimize, eq_p, in_p, ne_p, not_in_p, optimize


def test_optimize_in_p_empty():
    in_empty = in_p({})

    assert can_optimize(in_empty)

    optimized = optimize(in_empty)

    assert optimized == always_false_p


def test_optimize_in_p_single():
    in_1 = in_p({1})

    assert can_optimize(in_1)

    optimized = optimize(in_1)

    assert optimized == eq_p(1)


def test_optimize_not_in_p_empty():
    not_in_empty = not_in_p({})

    assert can_optimize(not_in_empty)

    optimized = optimize(not_in_empty)

    assert optimized == always_true_p


def test_optimize_not_in_p_single():
    not_in_empty = not_in_p({1})

    assert can_optimize(not_in_empty)

    optimized = optimize(not_in_empty)

    assert optimized == ne_p(1)
