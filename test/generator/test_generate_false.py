import uuid
from datetime import datetime

import pytest
from more_itertools import take

from predicate import (
    all_p,
    eq_p,
    ge_p,
    generate_false,
    in_p,
    is_bool_p,
    is_complex_p,
    is_datetime_p,
    is_dict_p,
    is_empty_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_none_p,
    is_not_none_p,
    is_set_of_p,
    is_set_p,
    is_str_p,
    is_truthy_p,
    is_uuid_p,
    pos_p,
    zero_p,
)


@pytest.mark.parametrize(
    "predicate",
    [
        all_p(is_int_p),
        # any_p(is_uuid_p),
        in_p(2, 3, 4),
        is_bool_p,
        is_complex_p,
        is_datetime_p,
        is_dict_p,
        is_empty_p,
        is_falsy_p,
        is_float_p,
        is_none_p,
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
