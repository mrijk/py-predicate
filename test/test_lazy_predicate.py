from datetime import datetime

import pytest

from predicate.standard_predicates import (
    all_p,
    fn_p,
    is_dict_p,
    is_float_p,
    is_int_p,
    is_list_p,
    is_none_p,
    is_str_p,
    lazy_p,
)


def test_lazy_predicate():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str")))

    assert not str_or_list_of_str(1)
    assert not str_or_list_of_str([1])

    assert str_or_list_of_str("foo")
    assert str_or_list_of_str([])
    assert str_or_list_of_str(["foo"])
    assert str_or_list_of_str(["foo", ["foo", ["foo"], "bar"]])


def test_lazy_predicate_ref_not_found():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str_no_ref")))

    with pytest.raises(ValueError):
        assert str_or_list_of_str(["foo"])


def test_is_json():
    valid_json_p = lazy_p("is_json_p")
    valid_list_p = is_list_p & lazy_p("valid_values")

    valid_keys_p = all_p(is_str_p)

    valid_values = all_p(is_str_p | is_int_p | is_float_p | valid_list_p | valid_json_p | is_none_p)
    valid_values_p = fn_p(lambda x: valid_values(x.values()))

    is_json_p = (is_dict_p & valid_keys_p & valid_values_p) | valid_list_p

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
