from helpers import exercise_predicate

from predicate import is_none_p
from predicate.explain import explain


def test_is_none_p():
    assert not is_none_p(13)
    assert is_none_p(None)


def test_is_none_explain():
    expected = {"reason": "42 is not None", "result": False}
    assert explain(is_none_p, 42) == expected


def test_none_exercise():
    exercise_predicate(is_none_p)
