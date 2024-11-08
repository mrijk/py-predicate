from datetime import datetime, timedelta
from uuid import UUID, uuid4

import pytest

from predicate import Predicate, always_false_p, always_true_p, ge_p, gt_p, le_p, lt_p
from predicate.predicate import NamedPredicate
from predicate.standard_predicates import (
    eq_false_p,
    eq_p,
    eq_true_p,
    fn_p,
    in_p,
    is_datetime_p,
    is_dict_p,
    is_instance_p,
    is_int_p,
    is_list_p,
    is_not_none_p,
    is_str_p,
    is_uuid_p,
    ne_p,
    not_in_p,
)


def test_always_true_p():
    assert always_true_p(13)


def test_always_false_p():
    assert not always_false_p(13)


def test_in_p():
    in_123 = in_p("1", "2", "3")

    assert in_123("1")
    assert not in_123("0")


def test_in_p_eq():
    p = in_p("1", "2", "3")
    q = in_p("1", "2", "3")

    assert p == q


def test_in_p_ne():
    p = in_p("1", "2", "3")
    q = in_p("1", "2")

    assert p != q


def test_not_in_p():
    not_in_123 = not_in_p("1", "2", "3")

    assert not_in_123("0")
    assert not not_in_123("1")


def test_ge_p():
    ge_2 = ge_p(2)

    assert not ge_2(1)
    assert ge_2(2)
    assert ge_2(3)


def test_str_ge_p():
    ge_bar = ge_p("bar")

    assert ge_bar("foo")
    assert not ge_bar("a")
    assert not ge_bar("A")


def test_datetime_ge_p():
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)

    ge_now = ge_p(now)

    assert ge_now(tomorrow)
    assert not ge_now(yesterday)


def test_uuid_ge_p():
    u1 = UUID("10bec12e-e216-42fd-9754-ff0e0abcf27c")
    u2 = UUID("a348c15c-57b1-40a0-94db-27a33897522b")

    u = UUID("7e05cf1e-a7ad-433b-9396-7aec1c9692d2")

    ge_u = ge_p(u)

    assert not ge_u(u1)
    assert ge_u(u2)


def test_gt_p():
    gt_2 = gt_p(2)

    assert gt_2(2) is False
    assert gt_2(3) is True


def test_le_p():
    le_2 = le_p(2)

    assert le_2(1) is True
    assert le_2(2) is True
    assert le_2(3) is False


def test_lt_p():
    lt_2 = lt_p(2)

    assert lt_2(1) is True
    assert lt_2(2) is False


def test_eq_p():
    eq_2 = eq_p(2)

    assert eq_2(1) is False
    assert eq_2(2) is True

    eq_foo = eq_p("foo")

    assert eq_foo("bar") is False
    assert eq_foo("foo") is True


def test_ne_p():
    ne_2 = ne_p(2)

    assert ne_2(1) is True
    assert ne_2(2) is False

    ne_foo = ne_p("foo")

    assert ne_foo("bar") is True
    assert ne_foo("foo") is False


def test_eq_true_p():
    assert eq_true_p(True)
    assert not eq_true_p(False)


def test_eq_false_p():
    assert eq_false_p(True) is False
    assert eq_false_p(False) is True


def test_is_datetime_p():
    now = datetime.now()

    assert is_datetime_p(now)
    assert not is_datetime_p("foo")


def test_is_int_p():
    assert not is_int_p(None)
    assert not is_int_p("3")
    assert not is_int_p(3.0)

    assert is_int_p(3)


def test_is_str_p():
    assert is_str_p(None) is False
    assert is_str_p(3) is False

    assert is_str_p("3") is True


def test_is_list_p():
    assert is_list_p(None) is False
    assert is_list_p((3,)) is False
    assert is_list_p(3) is False

    assert is_list_p([]) is True
    assert is_list_p([3]) is True


def test_is_dict_p():
    assert not is_dict_p(None)
    assert not is_dict_p({3})

    assert is_dict_p({})
    assert is_dict_p({"x": 3})


def test_is_uuid_p():
    assert not is_uuid_p(None)

    assert is_uuid_p(uuid4())


def test_is_instance_p():
    is_str_or_int_p = is_instance_p(str, int)

    assert not is_str_or_int_p(None)
    assert not is_str_or_int_p([3])

    assert is_str_or_int_p(3)
    assert is_str_or_int_p("3")


def test_is_instance_eq():
    p = is_instance_p(int)
    q = is_instance_p(int)

    assert p == q


def test_is_instance_ne():
    p = is_instance_p(int)
    q = is_instance_p(str, int)

    assert p != q


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


def test_base_predicate():
    p = Predicate()
    with pytest.raises(NotImplementedError):
        p(1)


def test_named_predicate():
    p = NamedPredicate(name="p")
    q = NamedPredicate(name="q")

    assert not p(False)
    assert p != q


def test_lambda():
    in_123 = fn_p(lambda x: str(x) in ["1", "2", "3"])
    exists_p = is_not_none_p & in_123

    assert not exists_p(None)
    assert not exists_p(4)
    assert exists_p(3)
