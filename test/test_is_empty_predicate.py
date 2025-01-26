from predicate import is_empty_p, is_not_empty_p
from predicate.explain import explain


def test_is_empty():
    assert not is_empty_p([1])
    assert is_empty_p([])
    assert is_empty_p(())
    assert is_empty_p("")


def test_is_empty_explain():
    expected = {"reason": "Expected length eq_p(0), actual: 3", "result": False}
    assert explain(is_empty_p, {1, 2, 3}) == expected


def test_is_not_empty():
    assert not is_not_empty_p([])
    assert not is_not_empty_p(())
    assert is_not_empty_p([1])
    assert is_not_empty_p("foo")


def test_is_not_empty_explain():
    expected = {"reason": "Expected length gt_p(0), actual: 0", "result": False}
    assert explain(is_not_empty_p, []) == expected
