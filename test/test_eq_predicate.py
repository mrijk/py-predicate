import pytest
from helpers import exercise_predicate

from predicate import eq_p
from predicate.explain import explain


@pytest.mark.parametrize("v, invalid", [(2, 3), ("foo", "bar")])
def test_eq_p(v, invalid):
    predicate = eq_p(v)
    assert predicate(v)
    assert not predicate(invalid)


def test_eq_explain():
    predicate = eq_p(2)

    expected = {"reason": "3 is not equal to 2", "result": False}
    assert explain(predicate, 3) == expected


def test_eq_int():
    eq_1 = eq_p(2)
    eq_2 = eq_p(2)
    eq_3 = eq_p(3)

    assert eq_1 == eq_1
    assert eq_1 == eq_2
    assert eq_1 != eq_3


def test_eq_str():
    eq_1 = eq_p("foo")
    eq_2 = eq_p("foo")
    eq_3 = eq_p("bar")

    assert eq_1 == eq_1
    assert eq_1 == eq_2
    assert eq_1 != eq_3


def test_eq_exercise():
    exercise_predicate(eq_p)
