import pytest

from predicate import eq_p, is_dict_of_p, is_int_p, is_str_p


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ({}, False),
        ({1: "foo"}, False),
        ({"y": "foo"}, False),
        ({"x": "foo"}, True),
    ],
)
def test_is_dict_of_p(value, expected):
    predicate = is_dict_of_p((eq_p("x"), is_str_p))

    assert predicate(value) is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ({}, False),
        ({"x": "foo"}, False),
        ({1: "foo"}, False),
        ({"x": 1}, True),
    ],
)
def test_is_dict_of_str_int(value, expected):
    predicate = is_dict_of_p((is_str_p, is_int_p))

    assert predicate(value) is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ({}, False),
        ({"x": "foo"}, False),
        ({1: "foo"}, False),
        ({"foo": {"x": "one", "z": "two"}}, False),
        ({"foo": {"x": "one", "y": "two"}}, True),
    ],
)
def test_is_dict_of_dict_p(value, expected):
    is_xy_dict = is_dict_of_p((eq_p("x"), is_str_p), (eq_p("y"), is_str_p))
    predicate = is_dict_of_p((is_str_p, is_xy_dict))

    assert predicate(value) is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ({}, False),
        ({"x": "foo"}, False),
        ({1: "foo"}, False),
        ({"x": 1, "y": 2}, True),
    ],
)
def test_is_dict_str_key(value, expected):
    predicate = is_dict_of_p(("x", is_int_p), (eq_p("y"), is_int_p))

    assert predicate(value) is expected
