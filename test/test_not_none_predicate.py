import pytest
from helpers import exercise_predicate

from predicate import is_not_none_p
from predicate.explain import explain


@pytest.mark.skip
def test_is_not_none_p():
    assert not is_not_none_p(None)
    assert is_not_none_p(13)


@pytest.mark.skip
def test_is_not_none_explain():
    expected = {"reason": "Value is None", "result": False}
    assert explain(is_not_none_p, None) == expected


@pytest.mark.skip
def test_none_exercise():
    exercise_predicate(is_not_none_p)
