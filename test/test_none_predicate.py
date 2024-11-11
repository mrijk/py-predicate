from predicate import is_none_p, is_not_none_p


def test_is_not_none_p():
    assert not is_not_none_p(None)
    assert is_not_none_p(13)


def test_is_none_p():
    assert not is_none_p(13)
    assert is_none_p(None)
