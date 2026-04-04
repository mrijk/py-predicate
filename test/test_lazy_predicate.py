from datetime import datetime

import pytest

from predicate import (
    all_p,
    comp_p,
    is_bool_p,
    is_dict_p,
    is_float_p,
    is_int_p,
    is_list_of_p,
    is_none_p,
    is_str_p,
    lazy_p,
)


def test_lazy_predicate():
    str_or_list_of_str = is_str_p | is_list_of_p(lazy_p("str_or_list_of_str"))

    assert not str_or_list_of_str(1)
    assert not str_or_list_of_str([1])

    assert str_or_list_of_str("foo")
    assert str_or_list_of_str([])
    assert str_or_list_of_str(["foo"])
    assert str_or_list_of_str(["foo", ["foo", ["foo"], "bar"]])


def test_lazy_predicate_ref_not_found():
    str_or_list_of_str = is_str_p | is_list_of_p(lazy_p("str_or_list_of_str_no_ref"))

    with pytest.raises(ValueError):
        assert str_or_list_of_str(["foo"])


def test_is_json():
    _valid_json_p = lazy_p("is_json_p")
    json_list_p = is_list_of_p(lazy_p("_valid_value"))

    json_keys_p = all_p(is_str_p)

    _valid_value = is_str_p | is_int_p | is_bool_p | is_float_p | json_list_p | _valid_json_p | is_none_p
    json_values_p = comp_p(lambda x: x.values(), all_p(_valid_value))

    is_json_p = (is_dict_p & json_keys_p & json_values_p) | json_list_p

    assert not is_json_p(1)
    assert not is_json_p({1: "one"})
    assert not is_json_p({"one": datetime.now()})

    assert is_json_p({})
    assert is_json_p([])
    assert is_json_p([1, "foo", 3.14])
    assert is_json_p({"one": 1})
    assert is_json_p({"one": 3.14})
    assert is_json_p({"one": False})
    assert is_json_p({"one": None})
    assert is_json_p({"one": {"two": {"three": 3}}})
