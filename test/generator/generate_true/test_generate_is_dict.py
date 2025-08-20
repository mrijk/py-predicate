import pytest
from more_itertools import first, take

from predicate import all_p, fn_p, ge_le_p, generate_true, has_length_p, in_p, is_dict_p, is_int_p, zero_p


def test_generate_is_dict():
    predicate = is_dict_p

    values = take(5, generate_true(predicate))

    assert first(values) == {}


def test_generate_is_dict_with_keys_p():
    predicate = is_dict_p
    key_p = is_int_p

    values = take(5, generate_true(predicate, key_p=key_p))

    values_p = all_p(fn_p(fn=lambda d: all_p(key_p)(d.keys())))

    assert values_p(values)


def test_generate_is_dict_with_value_p():
    predicate = is_dict_p
    value_p = in_p({"foo", "bar", "foobar"})

    values = take(5, generate_true(predicate, value_p=value_p))

    values_p = all_p(fn_p(fn=lambda d: all_p(value_p)(d.values())))

    assert values_p(values)


@pytest.mark.parametrize("size_p", [zero_p, ge_le_p(lower=3, upper=5)])
def test_generate_is_dict_with_size_p(size_p):
    predicate = is_dict_p

    values = take(5, generate_true(predicate, size_p=size_p))

    sizes_p = all_p(has_length_p(length_p=size_p))

    assert sizes_p(values)
