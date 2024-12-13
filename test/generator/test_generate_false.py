import uuid
from datetime import datetime

import pytest
from more_itertools import take

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    ge_p,
    generate_false,
    has_key_p,
    has_length_p,
    in_p,
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_dict_of_p,
    is_dict_p,
    is_empty_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_iterable_of_p,
    is_iterable_p,
    is_list_of_p,
    is_list_p,
    is_none_p,
    is_not_empty_p,
    is_not_none_p,
    is_set_of_p,
    is_set_p,
    is_str_p,
    is_truthy_p,
    is_tuple_of_p,
    is_uuid_p,
    pos_p,
    zero_p,
)


@pytest.mark.parametrize(
    "predicate",
    [
        all_p(is_int_p),
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
        is_empty_p,
        is_falsy_p,
        is_float_p,
        is_iterable_p,
        is_list_p,
        is_none_p,
        is_not_empty_p,
        is_not_none_p,
        is_truthy_p,
        is_int_p,
        is_uuid_p,
        is_set_p,
        is_str_p,
        is_int_p | is_str_p,
        pos_p,
        zero_p,
    ],
)
def test_generate_false(predicate):
    assert_generated_false(predicate)


@pytest.mark.parametrize("value", [2, "foo", "3.14", "complex(1, 2)"])
def test_generate_eq(value):
    predicate = eq_p(value)

    assert_generated_false(predicate)


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

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "key_value_predicates",
    [
        ([(is_str_p, is_int_p)]),
    ],
)
def test_dict_of(key_value_predicates):
    predicate = is_dict_of_p(*key_value_predicates)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "iterable_of_p",
    [
        is_int_p,
    ],
)
def test_iterable_of(iterable_of_p):
    predicate = is_iterable_of_p(iterable_of_p)

    assert_generated_false(predicate)


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

    assert_generated_false(predicate)


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

    assert_generated_false(predicate)


def test_generate_always_false_p():
    predicate = always_false_p

    assert_generated_false(predicate)


def test_generate_always_true_p():
    predicate = always_true_p

    assert not list(generate_false(predicate))


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

    assert_generated_false(predicate)


def assert_generated_false(predicate):
    values = take(5, generate_false(predicate))
    assert values

    for value in values:
        assert not predicate(value)
