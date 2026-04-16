from predicate.set_predicates import intersects_p


def test_intersects_true():
    predicate = intersects_p({1, 2, 3})

    assert predicate([2, 4, 6])


def test_intersects_false():
    predicate = intersects_p({1, 2, 3})

    assert not predicate([4, 5, 6])


def test_intersects_empty_input():
    predicate = intersects_p({1, 2, 3})

    assert not predicate([])


def test_intersects_repr():
    predicate = intersects_p({1})

    assert repr(predicate) == "intersects_p({1})"


def test_intersects_with_set_input():
    predicate = intersects_p({1, 2, 3})

    assert predicate({3, 4, 5})
    assert not predicate({4, 5, 6})
