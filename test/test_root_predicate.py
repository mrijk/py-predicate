import pytest

from predicate import is_int_p, is_list_of_p, is_str_p, root_p


def test_root_predicate():
    str_or_list_of_str = is_str_p | is_list_of_p(root_p)

    assert not str_or_list_of_str([13])
    assert not str_or_list_of_str([1])


def test_root_predicate_with_different_root():
    str_or_list_of_str = is_str_p | is_list_of_p(root_p)

    _ = str_or_list_of_str | is_int_p

    assert str_or_list_of_str([13])
    assert str_or_list_of_str("foo")
    assert str_or_list_of_str([])
    assert str_or_list_of_str(["foo"])
    assert str_or_list_of_str(["foo", ["foo", ["foo"], "bar"]])


def test_root_predicate_dont_call():
    with pytest.raises(ValueError):
        root_p(13)
