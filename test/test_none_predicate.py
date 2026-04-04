import pytest
from helpers import exercise_predicate

from predicate import PredicateError, is_int_p, is_none_p, none_is_exception_p, none_is_false_p, none_is_true_p
from predicate.explain import explain


def test_is_none_p():
    assert not is_none_p(13)
    assert is_none_p(None)


def test_is_none_explain():
    expected = {"reason": "42 is not None", "result": False}
    assert explain(is_none_p, 42) == expected


def test_none_is_false_p():
    predicate = none_is_false_p(is_int_p)
    assert predicate(13)
    assert not predicate(None)


def test_none_is_true_p():
    predicate = none_is_true_p(is_int_p)
    assert predicate(13)
    assert predicate(None)


def test_none_is_exception_p():
    predicate = none_is_exception_p(is_int_p)
    assert predicate(13)
    with pytest.raises(PredicateError):
        assert predicate(None)


def test_none_exercise():
    exercise_predicate(is_none_p)
