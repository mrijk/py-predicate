from predicate import always_false_p, can_optimize, intersects_p, optimize


def test_optimize_intersects_empty():
    predicate = intersects_p(set())

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_false_p


def test_optimize_intersects_non_empty():
    predicate = intersects_p({1, 2, 3})

    assert not can_optimize(predicate)


def test_optimize_intersects_or_intersects():
    # intersects(A) | intersects(B) == intersects(A ∪ B)
    predicate = intersects_p({1, 2}) | intersects_p({3, 4})

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == intersects_p({1, 2, 3, 4})


def test_optimize_intersects_or_intersects_overlap():
    # intersects({1, 2}) | intersects({2, 3}) == intersects({1, 2, 3})
    predicate = intersects_p({1, 2}) | intersects_p({2, 3})

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == intersects_p({1, 2, 3})
