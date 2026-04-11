import pytest

from predicate import explain, ge_p, is_int_p, is_str_p, regex_p
from predicate.struct_predicate import is_struct_p


@pytest.fixture
def is_person_p():
    required = {"name": is_str_p, "age": is_int_p & ge_p(0)}
    return is_struct_p(required=required)


@pytest.fixture
def is_person_with_optional_email_p():
    required = {"name": is_str_p, "age": is_int_p & ge_p(0)}
    optional = {"email": regex_p(r".+@.+")}
    return is_struct_p(required=required, optional=optional)


@pytest.mark.parametrize(
    "value",
    [{"name": "Alice", "age": 30}],
)
def test_is_struct_p_ok(value, is_person_p):
    assert is_person_p(value)


@pytest.mark.parametrize(
    "value, description",
    [
        (42, "Not a dict"),
        ({"age": 30}, "Name missing"),
        ({"name": "Alice", "age": -1}, "Invalid age"),
        ({"name": "Alice", "age": 30, "email": "alice@test.nl"}, "Extra key/value"),
    ],
)
def test_is_struct_p_fail(value, description, is_person_p):
    assert not is_person_p(value)


@pytest.mark.parametrize(
    "value",
    [
        {
            "name": "Alice",
            "age": 30,
            "email": "alice@test.nl",
        },
        {
            "name": "Bob",
            "age": 42,
        },
    ],
)
def test_is_struct_with_optional(value, is_person_with_optional_email_p):
    assert is_person_with_optional_email_p(value)


def test_is_struct_p_explain_not_a_dict(is_person_p):
    expected = {
        "result": False,
        "reason": "42 is not an instance of a dict",
    }
    assert explain(is_person_p, 42) == expected


def test_is_struct_p_explain_required_key_missing(is_person_p):
    value = {"name": "Alice"}

    expected = {
        "result": False,
        "reason": "Required field `age` missing",
    }
    assert explain(is_person_p, value) == expected


def test_is_struct_p_explain_wrong_required_value(is_person_p):
    value = {"name": "Alice", "age": -1}

    expected = {
        "result": False,
        "key": "age",
        "value": -1,
        "reason": "Value '-1' for key 'age' doesn't satisfy predicate is_int_p & ge_p(0)",
    }
    assert explain(is_person_p, value) == expected


def test_is_struct_p_repr(is_person_p):
    assert repr(is_person_p) == 'struct_p(required={"name": is_str_p, "age": is_int_p & ge_p(0)}, optional={})'


def test_is_struct_p_explain_additional_data(is_person_p):
    value = {"name": "Alice", "age": 30, "email": "alice@test.nl"}

    expected = {
        "result": False,
        "reason": "Field `email` is unknown",
    }
    assert explain(is_person_p, value) == expected
