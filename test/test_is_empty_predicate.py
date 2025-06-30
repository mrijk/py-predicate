import pytest
from helpers import exercise_predicate

from predicate import is_empty_p
from predicate.explain import explain


def test_is_empty_ok():
    assert is_empty_p([])
    assert is_empty_p(())
    assert is_empty_p("")


def test_is_empty_fail():
    assert not is_empty_p([1])


def test_is_empty_explain():
    expected = {"reason": "Expected length eq_p(0), actual: 3", "result": False}
    assert explain(is_empty_p, {1, 2, 3}) == expected


@pytest.mark.skip("TODO")
def test_is_empty_exercise():
    exercise_predicate(is_empty_p)
