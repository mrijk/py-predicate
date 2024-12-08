from datetime import datetime, timedelta
from uuid import UUID

from predicate import ge_p
from predicate.explain import explain


def test_int_ge_p():
    ge_2 = ge_p(2)

    assert not ge_2(1)
    assert ge_2(2)
    assert ge_2(3)


def test_float_ge_p():
    ge_pi = ge_p(3.14)

    assert not ge_pi(0.0)
    assert ge_pi(3.14)
    assert ge_pi(9.99)


def test_datetime_ge_p():
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)

    ge_now = ge_p(now)

    assert ge_now(tomorrow)
    assert ge_now(now)
    assert not ge_now(yesterday)


def test_uuid_ge_p():
    u1 = UUID("10bec12e-e216-42fd-9754-ff0e0abcf27c")
    u2 = UUID("a348c15c-57b1-40a0-94db-27a33897522b")

    u = UUID("7e05cf1e-a7ad-433b-9396-7aec1c9692d2")

    ge_u = ge_p(u)

    assert not ge_u(u1)
    assert ge_u(u2)
    assert ge_u(u)


def test_ge_explain():
    predicate = ge_p(2)

    expected = {"reason": "1 is not greater or equal to 2", "result": False}
    assert explain(predicate, 1) == expected
