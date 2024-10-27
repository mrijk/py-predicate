from predicate.standard_predicates import is_none_p, is_not_none_p


def test_is_not_none_p():
    assert is_not_none_p(13) is True
    assert is_not_none_p(None) is False


def test_is_none_p():
    assert is_none_p(13) is False
    assert is_none_p(None) is True
