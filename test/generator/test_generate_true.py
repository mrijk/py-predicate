import uuid
from datetime import datetime, timedelta
from ipaddress import IPv4Network

import pytest
from more_itertools import take

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_p,
    eq_true_p,
    fn_p,
    generate_true,
    in_p,
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_datetime_p,
    is_empty_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_iterable_of_p,
    is_list_of_p,
    is_none_p,
    is_not_empty_p,
    is_not_none_p,
    is_set_of_p,
    is_str_p,
    is_truthy_p,
    is_tuple_of_p,
    is_uuid_p,
    ne_p,
    not_in_p,
)
from predicate.property_predicate import property_p
from predicate.set_predicates import is_real_subset_p, is_subset_p
from predicate.standard_predicates import (
    eq_false_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    is_container_p,
    is_dict_of_p,
    is_dict_p,
    is_instance_p,
    is_iterable_p,
    is_list_p,
    is_set_p,
    is_tuple_p,
    le_p,
    lt_p,
    neg_p,
    pos_p,
    regex_p,
    zero_p,
)


def foo(self) -> bool:
    return True


@pytest.mark.parametrize(
    "predicate",
    [
        any_p(is_uuid_p),
        eq_false_p,
        eq_true_p,
        has_key_p("foo"),
        has_length_p(3),
        in_p(2, 3, 4),
        is_bool_p,
        is_callable_p,
        is_complex_p,
        is_container_p,
        is_datetime_p,
        is_dict_p,
        is_falsy_p,
        is_empty_p,
        is_float_p,
        is_iterable_p,
        is_list_p,
        is_none_p,
        is_not_empty_p,
        is_not_none_p,
        is_truthy_p,
        is_int_p,
        # is_predicate_p,
        is_set_p,
        is_str_p,
        is_tuple_p,
        is_int_p | is_str_p,
        ~is_int_p,
        is_int_p ^ is_str_p,
        is_uuid_p,
        ne_p(2),
        not_in_p(2, "foo", uuid.uuid4()),
        regex_p("^foo"),
        neg_p,
        pos_p,
        property_p(property(fget=foo)),
        zero_p,
        is_real_subset_p({1, 2, 3}),
        is_subset_p({1, 2, 3}),
    ],
)
def test_generate_true(predicate):
    assert_generated_true(predicate)


@pytest.mark.parametrize("all_predicate", [ge_p(2), is_str_p, property_p(property(fget=foo))])
def test_generate_all(all_predicate):
    predicate = all_p(all_predicate)

    assert_generated_true(predicate, min_size=0)


@pytest.mark.parametrize("value", [2, "foo", "3.14", "complex(1, 2)"])
def test_generate_eq(value):
    predicate = eq_p(value)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_ge(value):
    predicate = ge_p(value)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_gt(value):
    predicate = gt_p(value)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_le(value):
    predicate = le_p(value)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_lt(value):
    predicate = lt_p(value)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_ge_le(lower, upper):
    predicate = ge_le_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_ge_lt(lower, upper):
    predicate = ge_lt_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_gt_le(lower, upper):
    predicate = gt_le_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_gt_lt(lower, upper):
    predicate = gt_lt_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "key_value_predicates",
    [
        ([(is_str_p, is_int_p)]),
    ],
)
def test_dict_of(key_value_predicates):
    predicate = is_dict_of_p(*key_value_predicates)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "iterable_of_p",
    [
        is_int_p,
    ],
)
def test_iterable_of(iterable_of_p):
    predicate = is_iterable_of_p(iterable_of_p)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "list_type_p",
    [
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_int_p | is_str_p,
        is_bool_p | is_datetime_p | is_str_p,
    ],
)
def test_list_of(list_type_p):
    predicate = is_list_of_p(list_type_p)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "tuple_types_p",
    [
        (is_bool_p,),
        (is_int_p,),
        (is_str_p,),
        (is_int_p, is_int_p),
    ],
)
def test_tuple_of(tuple_types_p):
    predicate = is_tuple_of_p(*tuple_types_p)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "set_type_p",
    [
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_int_p | is_str_p,
        is_bool_p | is_datetime_p | is_str_p,
    ],
)
def test_set_of(set_type_p):
    predicate = is_set_of_p(set_type_p)

    assert_generated_true(predicate)


def test_generate_always_false_p():
    predicate = always_false_p

    assert not list(generate_true(predicate))


def test_generate_xor_always_false():
    predicate = always_true_p ^ always_true_p

    assert not list(generate_true(predicate))


def test_generate_always_true_p():
    predicate = always_true_p

    assert_generated_true(predicate)


def test_generate_fn_p():
    predicate = fn_p(lambda _x: True)

    with pytest.raises(ValueError):
        generate_true(predicate)


def assert_generated_true(predicate, **kwargs):
    values = take(5, generate_true(predicate, **kwargs))
    assert values

    for value in values:
        assert predicate(value)


def test_generate_false_unknown(unknown_p):
    with pytest.raises(ValueError):
        take(5, generate_true(unknown_p))


@pytest.mark.parametrize(
    "compare_predicate",
    [
        ge_p,
        gt_p,
        le_p,
        lt_p,
    ],
)
def test_generate_true_unknown_compare(compare_predicate):
    predicate = compare_predicate(v=None)
    with pytest.raises(ValueError):
        take(5, generate_true(predicate))


@pytest.mark.parametrize(
    "range_predicate",
    [
        ge_le_p,
        ge_lt_p,
        gt_le_p,
        gt_lt_p,
    ],
)
def test_generate_true_unknown_range(range_predicate):
    predicate = range_predicate(lower="bar", upper="foo")
    with pytest.raises(ValueError):
        take(5, generate_true(predicate))


def test_generate_true_not_in_p_unknown():
    predicate = not_in_p(None)
    with pytest.raises(ValueError):
        take(5, generate_true(predicate))


def test_generate_true_is_instance_unknown():
    predicate = is_instance_p(IPv4Network)
    with pytest.raises(ValueError, match="No generator found"):
        take(5, generate_true(predicate))
