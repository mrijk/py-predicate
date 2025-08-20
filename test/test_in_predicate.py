from predicate import in_p


def test_in_p():
    in_123 = in_p(["1", "2", "3"])

    assert in_123("1")
    assert not in_123("0")


def test_in_p_eq():
    p = in_p({"1", "2", "3"})
    q = in_p({"1", "2", "3"})

    assert p == q


def test_in_p_ne():
    p = in_p({"1", "2", "3"})
    q = in_p({"1", "2"})

    assert p != q
