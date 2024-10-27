from uuid import uuid4

from predicate import ge_p, gt_p, le_p, lt_p
from predicate.predicate import FnPredicate, always_false_p, always_true_p
from predicate.standard_predicates import (
    eq_false_p,
    eq_p,
    eq_true_p,
    in_p,
    is_dict_p,
    is_instance_p,
    is_int_p,
    is_list_p,
    is_none_p,
    is_not_none_p,
    is_str_p,
    is_uuid_p,
    ne_p,
)


def test_always_true_p():
    assert always_true_p(13) is True


def test_always_false_p():
    assert always_false_p(13) is False


def test_is_not_none_p():
    assert is_not_none_p(13) is True
    assert is_not_none_p(None) is False


def test_is_none_p():
    assert is_none_p(13) is False
    assert is_none_p(None) is True


def test_in_p():
    in_123 = in_p("1", "2", "3")

    assert in_123("1") is True
    assert in_123("0") is False


def test_ge_p():
    ge_2 = ge_p(2)

    assert ge_2(1) is False
    assert ge_2(2) is True
    assert ge_2(3) is True


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
    assert eq_true_p(True) is True
    assert eq_true_p(False) is False


def test_eq_false_p():
    assert eq_false_p(True) is False
    assert eq_false_p(False) is True


def test_is_int_p():
    assert is_int_p(None) is False
    assert is_int_p("3") is False
    assert is_int_p(3.0) is False

    assert is_int_p(3) is True


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

    assert is_str_or_int_p(None) is False
    assert is_str_or_int_p([3]) is False

    assert is_str_or_int_p(3) is True
    assert is_str_or_int_p("3") is True


def test_eq():
    eq_1 = eq_p(2)
    eq_2 = eq_p(2)
    eq_3 = eq_p(3)

    assert eq_1 == eq_1
    assert eq_1 == eq_2
    assert eq_1 != eq_3


def test_lambda():
    in_123 = FnPredicate(lambda x: str(x) in ["1", "2", "3"])
    exists_p = is_not_none_p & in_123

    assert not exists_p(None)
    assert not exists_p(4)
    assert exists_p(3) is True
