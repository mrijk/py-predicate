import math

from helpers import exercise_predicate

from predicate import lt_p, neg_p
from predicate.explain import explain


def test_lt_p():
    lt_2 = lt_p(2)

    assert not lt_2(2)
    assert lt_2(1)


def test_lt_explain():
    predicate = lt_p(2)

    expected = {"reason": "2 is not less than 2", "result": False}
    assert explain(predicate, 2) == expected


def test_lt_exercise():
    exercise_predicate(lt_p)


def test_neg_p():
    assert not neg_p(1)
    assert not neg_p(0)
    assert neg_p(-1)
    assert neg_p(-3.14)
    assert neg_p(-math.inf)
