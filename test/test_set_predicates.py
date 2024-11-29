from predicate.set_predicates import in_p, is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p, not_in_p


def test_is_subset():
    predicate = is_subset_p({1, 2, 3})

    assert predicate({1})
    assert predicate({1, 2})
    assert predicate({1, 2, 3})
    assert not predicate({1, 2, 3, 4})


def test_is_real_subset():
    predicate = is_real_subset_p({1, 2, 3})

    assert predicate({1})
    assert predicate({1, 2})
    assert not predicate({1, 2, 3})


def test_is_superset():
    predicate = is_superset_p({1, 2, 3})

    assert not predicate({1, 2})
    assert predicate({1, 2, 3})
    assert predicate({1, 2, 3, 4})


def test_is_real_superset():
    predicate = is_real_superset_p({1, 2, 3})

    assert not predicate({1, 2})
    assert not predicate({1, 2, 3})
    assert predicate({1, 2, 3, 4})


def test_in_p():
    in_123 = in_p("1", "2", "3")

    assert in_123("1")
    assert not in_123("0")


def test_in_p_eq():
    p = in_p("1", "2", "3")
    q = in_p("1", "2", "3")

    assert p == q


def test_in_p_ne():
    p = in_p("1", "2", "3")
    q = in_p("1", "2")

    assert p != q


def test_not_in_p():
    not_in_123 = not_in_p("1", "2", "3")

    assert not_in_123("0")
    assert not not_in_123("1")
