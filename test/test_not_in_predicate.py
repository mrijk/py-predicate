from predicate import not_in_p


def test_not_in_p():
    not_in_123 = not_in_p(["1", "2", "3"])

    assert not_in_123("0")
    assert not not_in_123("1")
