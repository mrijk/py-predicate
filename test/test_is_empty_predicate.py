from predicate.explain import explain
from predicate.is_empty_predicate import is_empty_p, is_not_empty_p


def test_is_empty():
    assert not is_empty_p([1])
    assert is_empty_p([])
    assert is_empty_p(())
    assert is_empty_p("")


def test_is_empty_explain():
    expected = {"reason": "Iterable {1, 2, 3} is not empty", "result": False}
    assert explain(is_empty_p, {1, 2, 3}) == expected


def test_is_not_empty():
    assert not is_not_empty_p([])
    assert not is_not_empty_p(())
    assert is_not_empty_p([1])
    assert is_not_empty_p("foo")


def test_is_not_empty_explain():
    expected = {"reason": "Iterable [] is empty", "result": False}
    assert explain(is_not_empty_p, []) == expected
