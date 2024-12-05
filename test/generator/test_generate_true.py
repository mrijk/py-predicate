import uuid
from datetime import datetime

import pytest
from more_itertools import take

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_p,
    fn_p,
    in_p,
    is_bool_p,
    is_complex_p,
    is_datetime_p,
    is_empty_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_list_of_p,
    is_none_p,
    is_not_none_p,
    is_set_of_p,
    is_str_p,
    is_truthy_p,
    is_tuple_of_p,
    is_uuid_p,
    ne_p,
    not_in_p,
)
from predicate.generator.generate_true import generate_true
from predicate.set_predicates import is_real_subset_p, is_subset_p
from predicate.standard_predicates import (
    ge_p,
    gt_p,
    has_key_p,
    is_dict_p,
    is_set_p,
    le_p,
    lt_p,
    neg_p,
    pos_p,
    regex_p,
    zero_p,
)


@pytest.mark.parametrize(
    "predicate",
    [
        all_p(is_int_p),
        any_p(is_uuid_p),
        has_key_p("foo"),
        in_p(2, 3, 4),
        is_bool_p,
        is_complex_p,
        is_datetime_p,
        is_dict_p,
        is_falsy_p,
        is_empty_p,
        is_float_p,
        is_none_p,
        is_not_none_p,
        is_truthy_p,
        is_int_p,
        is_uuid_p,
        is_set_p,
        is_str_p,
        is_int_p | is_str_p,
        le_p(2),
        lt_p(2),
        ne_p(2),
        not_in_p(2, "foo", 4),
        regex_p("^foo"),
        neg_p,
        pos_p,
        zero_p,
        is_real_subset_p({1, 2, 3}),
        is_subset_p({1, 2, 3}),
    ],
)
def test_generate_true(predicate):
    assert_generated_true(predicate)


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


def test_generate_false():
    predicate = always_false_p

    assert not list(generate_true(predicate))


def test_generate_true_p():
    predicate = always_true_p

    assert_generated_true(predicate)


def test_generate_fn_p():
    predicate = fn_p(lambda _x: True)

    with pytest.raises(ValueError):
        generate_true(predicate)


def assert_generated_true(predicate):
    values = take(5, generate_true(predicate))
    assert values

    for value in values:
        assert predicate(value)
