import math
from datetime import datetime, timedelta
from unittest.mock import Mock
from uuid import UUID, uuid4

import pytest

from predicate import (
    Predicate,
    always_false_p,
    always_true_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    fn_p,
    ge_p,
    gt_p,
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_datetime_p,
    is_dict_p,
    is_instance_p,
    is_int_p,
    is_iterable_p,
    is_list_p,
    is_not_none_p,
    is_predicate_p,
    is_set_p,
    is_str_p,
    is_tuple_p,
    is_uuid_p,
    le_p,
    lt_p,
    ne_p,
)
from predicate.named_predicate import NamedPredicate
from predicate.predicate import is_empty_p, is_not_empty_p
from predicate.standard_predicates import (
    all_p,
    ge_le_p,
    ge_lt_p,
    gt_le_p,
    gt_lt_p,
    has_length_p,
    is_container_p,
    is_falsy_p,
    is_finite_p,
    is_hashable_p,
    is_inf_p,
    is_iterable_of_p,
    is_list_of_p,
    is_range_p,
    is_single_or_iterable_of_p,
    is_single_or_list_of_p,
    is_truthy_p,
    neg_p,
    pos_p,
    tee_p,
    zero_p,
)


def test_always_true_p():
    assert always_true_p(13)


def test_always_false_p():
    assert not always_false_p(13)


@pytest.mark.parametrize("value", [False, None, 0, {}, "", (), []])
def test_is_falsy_p(value):
    assert is_falsy_p(value)


@pytest.mark.parametrize("value", [True, not None, 13, {1}, "foo", (1,), [1]])
def test_is_truthy_p(value):
    assert is_truthy_p(value)


def test_ge_p():
    ge_2 = ge_p(2)

    assert not ge_2(1)
    assert ge_2(2)
    assert ge_2(3)


def test_ge_le_p():
    ge_2_le_3 = ge_le_p(2, 3)

    assert not ge_2_le_3(1)
    assert not ge_2_le_3(4)
    assert ge_2_le_3(2)
    assert ge_2_le_3(3)


def test_ge_lt_p():
    ge_2_lt_3 = ge_lt_p(2, 3)

    assert not ge_2_lt_3(1)
    assert not ge_2_lt_3(3)
    assert ge_2_lt_3(2)


def test_gt_le_p():
    gt_2_le_3 = gt_le_p(2, 3)

    assert not gt_2_le_3(2)
    assert not gt_2_le_3(4)
    assert gt_2_le_3(3)


def test_gt_lt_p():
    gt_2_lt_3 = gt_lt_p(2, 4)

    assert not gt_2_lt_3(2)
    assert not gt_2_lt_3(4)
    assert gt_2_lt_3(3)


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

    assert not gt_2(2)
    assert gt_2(3)


def test_le_p():
    le_2 = le_p(2)

    assert not le_2(3)
    assert le_2(1)
    assert le_2(2)


def test_lt_p():
    lt_2 = lt_p(2)

    assert not lt_2(2)
    assert lt_2(1)


def test_eq_p_int():
    eq_2 = eq_p(2)

    assert eq_2(1) is False
    assert eq_2(2) is True


def test_eq_p_str():
    eq_foo = eq_p("foo")

    assert eq_foo("bar") is False
    assert eq_foo("foo") is True


def test_ne_p_int():
    ne_2 = ne_p(2)

    assert not ne_2(2)
    assert ne_2(1)


def test_ne_p_str():
    ne_foo = ne_p("foo")

    assert not ne_foo("foo")
    assert ne_foo("bar")


def test_eq_true_p():
    assert eq_true_p(True)
    assert not eq_true_p(False)


def test_eq_false_p():
    assert not eq_false_p(True)
    assert eq_false_p(False)


def test_is_bool_p():
    assert not is_bool_p(0)
    assert not is_bool_p("1")

    assert is_bool_p(False)
    assert is_bool_p(True)


def test_is_callable_p():
    assert not is_callable_p(None)

    def foo():
        pass

    assert is_callable_p(foo)

    assert is_callable_p(lambda x: x)

    predicate = always_false_p
    assert is_callable_p(predicate)


def test_is_complex():
    assert not is_complex_p(1)

    assert is_complex_p(complex(2, 1))


def test_is_datetime_p():
    now = datetime.now()

    assert is_datetime_p(now)
    assert not is_datetime_p("foo")


def test_is_int_p():
    assert not is_int_p(None)
    assert not is_int_p("3")
    assert not is_int_p(3.0)

    assert is_int_p(3)


def test_is_predicate_p():
    assert not is_predicate_p(None)
    assert is_predicate_p(always_false_p)


def test_is_range_p():
    assert not is_range_p(None)
    assert is_range_p(range(10))


def test_is_str_p():
    assert not is_str_p(None)
    assert not is_str_p(3)

    assert is_str_p("3")


def test_is_dict_p():
    assert not is_dict_p(None)
    assert not is_dict_p({3})

    assert is_dict_p({})
    assert is_dict_p({"x": 3})


def test_is_iterable_p():
    assert not is_iterable_p(1)

    assert is_iterable_p([])
    assert is_iterable_p(())
    assert is_iterable_p("foobar")
    assert is_iterable_p({1, 2, 3})
    assert is_iterable_p(range(5))


def test_is_iterable_of_p():
    is_iterable_of_str = is_iterable_of_p(is_str_p)

    assert not is_iterable_of_str(None)
    assert not is_iterable_of_str([1])

    assert is_iterable_of_str([])
    assert is_iterable_of_str(["foo"])


def test_is_single_or_iterable_of_p():
    is_single_or_iterable_of_str = is_single_or_iterable_of_p(is_str_p)

    assert not is_single_or_iterable_of_str(None)
    assert not is_single_or_iterable_of_str([1])

    assert is_single_or_iterable_of_str("foo")
    assert is_single_or_iterable_of_str([])
    assert is_single_or_iterable_of_str(["foo"])


def test_is_list_p():
    assert not is_list_p(None)
    assert not is_list_p((3,))
    assert not is_list_p(3)

    assert is_list_p([])
    assert is_list_p([3])


def test_is_list_of_p():
    is_list_of_str = is_list_of_p(is_str_p)

    assert not is_list_of_str(None)
    assert not is_list_of_str([1])
    assert not is_list_of_str("foo")

    assert is_list_of_str([])
    assert is_list_of_str(["foo"])


def test_is_single_or_list_of_p():
    is_single_or_list_of_str = is_single_or_list_of_p(is_str_p)

    assert not is_single_or_list_of_str(None)
    assert not is_single_or_list_of_str([1])

    assert is_single_or_list_of_str("foo")
    assert is_single_or_list_of_str([])
    assert is_single_or_list_of_str(["foo"])


def test_is_set_p():
    assert not is_set_p(None)

    assert is_set_p(set())
    assert is_set_p({3})


def test_is_tuple_p():
    assert not is_tuple_p(None)

    assert is_tuple_p((3,))


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


def test_is_empty():
    assert not is_empty_p([1])
    assert is_empty_p([])
    assert is_empty_p(())


def test_is_not_empty():
    assert not is_not_empty_p([])
    assert not is_not_empty_p(())
    assert is_not_empty_p([1])


def test_has_length():
    of_length_1 = has_length_p(1)

    assert not of_length_1([])
    assert of_length_1([1])


def test_lambda():
    in_123 = fn_p(lambda x: str(x) in ["1", "2", "3"])
    exists_p = is_not_none_p & in_123

    assert not exists_p(None)
    assert not exists_p(4)
    assert exists_p(3)


def test_tee():
    log_fn = Mock()
    log = tee_p(fn=log_fn)

    ge_2 = ge_p(2)

    predicate = all_p(log & ge_2)

    assert predicate(range(2, 5))

    assert log_fn.call_count == 3


@pytest.mark.parametrize(
    "value",
    [
        set(),
        (),
        [],
        {"foo", "bar"},
    ],
)
def test_is_container_p(value):
    assert is_container_p(value)


@pytest.mark.parametrize("value", [1, 3.14, True, "foo", datetime.now()])
def test_is_hashable_p(value):
    assert is_hashable_p(value)


@pytest.mark.parametrize(
    "value",
    [
        {},
        {1, 2, 3},
    ],
)
def test_is_not_hashable_p(value):
    assert not is_hashable_p(value)


def test_zero_p(p):
    assert not zero_p(1)
    assert zero_p(0.0)


def test_neg_p(p):
    assert not neg_p(1)
    assert not neg_p(0)
    assert neg_p(-1)
    assert neg_p(-3.14)


def test_pos_p(p):
    assert not pos_p(-1)
    assert not pos_p(-3.14)
    assert not pos_p(0)
    assert pos_p(1)


def test_is_finite_p():
    assert not is_finite_p(math.inf)
    assert is_finite_p(13)
    assert is_finite_p(3.14)


def test_is_inf_p():
    assert not is_inf_p(13)

    assert is_inf_p(-math.inf)
    assert is_inf_p(math.inf)
