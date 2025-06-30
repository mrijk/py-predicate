from datetime import datetime, timedelta
from uuid import UUID

from helpers import exercise_predicate

from predicate import gt_p
from predicate.explain import explain


def test_gt_p():
    gt_2 = gt_p(2)

    assert not gt_2(2)
    assert gt_2(3)


def test_float_gt_p():
    gt_pi = gt_p(3.14)

    assert not gt_pi(0.0)
    assert not gt_pi(3.14)
    assert gt_pi(9.99)


def test_str_gt_p():
    gt_bar = gt_p("bar")

    assert not gt_bar("a")
    assert not gt_bar("A")
    assert not gt_bar("bar")
    assert gt_bar("foo")


def test_datetime_gt_p():
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)

    gt_now = gt_p(now)

    assert gt_now(tomorrow)
    assert not gt_now(now)
    assert not gt_now(yesterday)


def test_uuid_gt_p():
    u1 = UUID("10bec12e-e216-42fd-9754-ff0e0abcf27c")
    u2 = UUID("a348c15c-57b1-40a0-94db-27a33897522b")

    u = UUID("7e05cf1e-a7ad-433b-9396-7aec1c9692d2")

    gt_u = gt_p(u)

    assert not gt_u(u1)
    assert not gt_u(u)
    assert gt_u(u2)


def test_gt_explain():
    predicate = gt_p(2)

    expected = {"reason": "1 is not greater than 2", "result": False}
    assert explain(predicate, 1) == expected


def test_gt_exercise():
    exercise_predicate(gt_p)
