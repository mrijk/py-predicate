import pytest
from helpers import exercise_predicate

from predicate import is_not_empty_p
from predicate.explain import explain


def test_is_not_empty_ok():
    assert is_not_empty_p([1])
    assert is_not_empty_p("foo")


def test_is_not_empty_fail():
    assert not is_not_empty_p([])
    assert not is_not_empty_p(())


def test_is_not_empty_explain():
    expected = {"reason": "Expected length gt_p(0), actual: 0", "result": False}
    assert explain(is_not_empty_p, []) == expected


@pytest.mark.skip("TODO")
def test_is_not_empty_exercise():
    exercise_predicate(is_not_empty_p)
