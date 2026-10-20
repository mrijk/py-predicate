import pytest

from predicate import explain
from predicate.is_regex_predicate import is_regex_p


@pytest.mark.parametrize("value", [r"", r"\d{3}", r"^a+b*$"])
def test_is_regex_ok(value):
    assert is_regex_p(value)


@pytest.mark.parametrize("value", ["(", "[a-", "*", 42, None])
def test_is_regex_fail(value):
    assert not is_regex_p(value)


def test_is_regex_explain():
    expected = {
        "result": False,
        "reason": "String ( is not a valid regex: missing ), unterminated subpattern at position 0",
    }
    assert explain(is_regex_p, "(") == expected


def test_is_regex_explain_not_str():
    expected = {"result": False, "reason": "42 is not a string"}
    assert explain(is_regex_p, 42) == expected
