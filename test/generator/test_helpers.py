from datetime import datetime

import pytest
from more_itertools import first, take

from predicate import (
    all_p,
    ge_le_p,
    ge_p,
    has_length_p,
    in_p,
    is_bool_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_dict_p,
    is_float_p,
    is_int_p,
    is_list_p,
    is_set_p,
    is_str_p,
    is_tuple_p,
    is_uuid_p,
)
from predicate.generator.helpers import (
    random_anys,
    random_bools,
    random_complex_numbers,
    random_containers,
    random_datetimes,
    random_dicts,
    random_floats,
    random_ints,
    random_lists,
    random_sets,
    random_strings,
    random_tuples,
    random_uuids,
)


def test_random_anys():
    anys = take(10, random_anys())

    all_any = all_p(is_bool_p | is_datetime_p | is_float_p | is_int_p | is_str_p)

    assert all_any(anys)


def test_random_bools():
    bools = take(10, random_bools())

    all_bool = all_p(is_bool_p)

    assert bools[0] is False
    assert bools[1] is True
    assert all_bool(bools)


def test_random_complex_numbers():
    complex_numbers = take(10, random_complex_numbers())

    all_complex = all_p(is_complex_p)

    assert all_complex(complex_numbers)


def test_random_containers():
    containers = take(10, random_containers())

    all_container = all_p(is_container_p)

    assert all_container(containers)


def test_random_dicts():
    dicts = take(10, random_dicts())

    all_dict = all_p(is_dict_p)

    assert first(dicts) == {}
    assert all_dict(dicts)


def test_random_dicts_with_value_p():
    value_p = in_p("foo", "bar", "foobar")
    dicts = take(10, random_dicts(value_p=value_p))

    all_dict = all_p(is_dict_p)

    assert first(dicts) == {}
    assert all_dict(dicts)


def test_random_datetimes():
    datetimes = take(10, random_datetimes())

    all_datetime = all_p(is_datetime_p)

    assert all_datetime(datetimes)


def test_random_datetimes_with_limits():
    lower = datetime(year=2025, month=1, day=1)
    upper = datetime(year=2026, month=12, day=31)

    datetimes = take(10, random_datetimes(lower=lower, upper=upper))

    all_datetime = all_p(is_datetime_p)

    assert all_datetime(datetimes)


def test_random_list():
    lists = take(10, random_lists())

    all_lists = all_p(is_list_p)

    assert first(lists) == []
    assert all_lists(lists)


def test_random_list_with_limits():
    length_p = ge_le_p(lower=3, upper=5)
    lists = take(10, random_lists(length_p=length_p))

    all_lists = all_p(is_list_p & has_length_p(length_p))

    assert all_lists(lists)


@pytest.mark.parametrize("value_p", [is_int_p])
def test_random_list_with_value_p(value_p):
    lists = take(10, random_lists(value_p=value_p))

    all_lists = all_p(is_list_p & all_p(value_p))

    assert all_lists(lists)


def test_random_sets():
    sets = take(10, random_sets())

    all_sets = all_p(is_set_p)

    assert first(sets) == set()
    assert all_sets(sets)


def test_random_sets_with_limits():
    length_p = ge_le_p(lower=3, upper=5)
    sets = take(10, random_sets(length_p=length_p))

    all_sets = all_p(is_set_p & has_length_p(length_p=length_p))

    assert all_sets(sets)


@pytest.mark.parametrize("value_p", [ge_p(2)])
def test_random_sets_with_value_p(value_p):
    sets = take(10, random_sets(value_p=value_p))

    all_sets = all_p(is_set_p & all_p(value_p))

    assert all_sets(sets)


def test_random_strings():
    strings = take(10, random_strings())

    all_str = all_p(is_str_p)

    assert all_str(strings)


def test_random_strings_with_limits():
    strings = take(10, random_strings(min_size=1, max_size=3))

    all_str = all_p(is_str_p & has_length_p(length_p=ge_le_p(lower=1, upper=3)))

    assert all_str(strings)


def test_random_tuples():
    tuples = take(10, random_tuples())

    all_tuples = all_p(is_tuple_p)

    assert first(tuples) == ()
    assert all_tuples(tuples)


def test_random_tuples_with_limits():
    length_p = ge_le_p(lower=3, upper=5)

    tuples = take(10, random_tuples(length_p=length_p))

    all_tuples = all_p(is_tuple_p & has_length_p(length_p=length_p))

    assert all_tuples(tuples)


@pytest.mark.parametrize("value_p", [ge_p(2)])
def test_random_tuples_with_value_p(value_p):
    tuples = take(10, random_tuples(value_p=value_p))

    all_tuples = all_p(is_tuple_p & all_p(value_p))

    assert all_tuples(tuples)


def test_random_floats():
    floats = take(10, random_floats())

    all_float = all_p(is_float_p)

    assert all_float(floats)


def test_random_floats_with_limits():
    floats = take(10, random_floats(lower=-1.0, upper=1.0))

    all_float = all_p(is_float_p & ge_le_p(lower=-1.0, upper=1.0))

    assert all_float(floats)


def test_random_ints():
    ints = take(10, random_ints())

    all_int = all_p(is_int_p)

    assert all_int(ints)


def test_random_ints_with_limits():
    ints = take(10, random_ints(lower=10, upper=13))

    all_int = all_p(is_int_p & ge_le_p(lower=10, upper=13))

    assert all_int(ints)


def test_random_uuids():
    uuids = take(10, random_uuids())

    all_uuid = all_p(is_uuid_p)

    assert all_uuid(uuids)
