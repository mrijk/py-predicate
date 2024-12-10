from predicate import is_none_p, is_not_none_p
from predicate.explain import explain


def test_is_not_none_p():
    assert not is_not_none_p(None)
    assert is_not_none_p(13)


def test_is_not_none_explain():
    expected = {"reason": "Value is None", "result": False}
    assert explain(is_not_none_p, None) == expected


def test_is_none_p():
    assert not is_none_p(13)
    assert is_none_p(None)


def test_is_none_explain():
    expected = {"reason": "42 is not None", "result": False}
    assert explain(is_none_p, 42) == expected
