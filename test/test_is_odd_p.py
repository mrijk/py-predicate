from predicate import is_odd_p


def test_is_odd():
    assert not is_odd_p(0)
    assert is_odd_p(1)
