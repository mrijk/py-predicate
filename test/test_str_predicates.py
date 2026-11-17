import pytest
from generator.generate_false.helpers import assert_generated_false
from generator.generate_true.helpers import assert_generated_true

from predicate import (
    contains_p,
    ends_with_p,
    generate_false,
    is_alnum_p,
    is_alpha_p,
    is_blank_p,
    is_camel_case_p,
    is_capitalized_p,
    is_decimal_p,
    is_digit_p,
    is_kebab_case_p,
    is_lower_p,
    is_numeric_p,
    is_printable_p,
    is_single_line_p,
    is_snake_case_p,
    is_space_p,
    is_stripped_p,
    is_title_p,
    is_upper_p,
    starts_with_p,
)
from predicate.str_predicates import create_is_str_p


def test_contains_p():
    predicate = contains_p("café")
    assert predicate("un café noir")
    assert predicate("café")
    assert not predicate("CAFÉ")
    assert not predicate("cafe")
    assert repr(predicate) == "contains_p('café')"
    assert predicate.klass is str
    assert predicate.explain("tea") == {"result": False, "reason": "'tea' does not contain 'café'"}


@pytest.mark.parametrize("substring", ["a", "café", "a long substring"])
def test_contains_p_generators(substring):
    predicate = contains_p(substring)
    assert_generated_true(predicate)
    assert_generated_false(predicate)


def test_contains_p_empty_substring():
    predicate = contains_p("")
    assert predicate("")
    assert predicate("any text")
    assert_generated_true(predicate)
    assert list(generate_false(predicate)) == []


def test_is_alnum_p():
    assert not is_alnum_p("foo-1")
    assert is_alnum_p("foo1")
    assert is_alnum_p("foo")


def test_is_alpha_p():
    assert not is_alpha_p("foo1")
    assert is_alpha_p("foo")


def test_is_decimal_p():
    assert not is_decimal_p("foo")
    assert is_decimal_p("123")


def test_is_digit_p():
    assert not is_digit_p("Foo")
    assert is_digit_p("123")


def test_is_lower_p():
    assert not is_lower_p("Foo")
    assert is_lower_p("foo")


def test_is_space_p():
    assert is_space_p(" ")
    assert is_space_p("\t")


def test_is_title_p():
    assert not is_title_p("foo")
    assert not is_title_p("FOO")
    assert is_title_p("Foo")


def test_is_upper_p():
    assert not is_upper_p("Foo")
    assert is_upper_p("FOO")


def test_is_numeric_p():
    assert not is_numeric_p("foo")
    assert is_numeric_p("123")


def test_is_printable_p():
    assert not is_printable_p("hello\x00")
    assert is_printable_p("hello")
    assert is_printable_p("")


def test_ends_with_p():
    predicate = ends_with_p("foo")

    assert not predicate("foobar")
    assert predicate("barfoo")


def test_starts_with_p():
    predicate = starts_with_p("foo")

    assert not predicate("bar")
    assert predicate("foobar")


def test_create_is_str_p():
    pred = create_is_str_p(str.isupper)
    assert pred("ABC")
    assert not pred("abc")


def test_is_stripped_p():
    assert is_stripped_p("")
    assert is_stripped_p("a b")
    assert not is_stripped_p(" a")
    assert not is_stripped_p("a\n")


def test_is_blank_p():
    assert is_blank_p("")
    assert is_blank_p(" \t\n")
    assert not is_blank_p(" a ")


def test_is_single_line_p():
    assert is_single_line_p("")
    assert is_single_line_p("a b")
    assert not is_single_line_p("a\nb")


def test_is_capitalized_p():
    assert is_capitalized_p("Hello world")
    assert is_capitalized_p("H")
    assert not is_capitalized_p("")
    assert not is_capitalized_p("hello")
    assert not is_capitalized_p("Hello World")
    assert not is_capitalized_p("HELLO")
    assert not is_capitalized_p("1abc")


def test_is_snake_case_p():
    assert is_snake_case_p("foo")
    assert is_snake_case_p("foo_bar2")
    assert not is_snake_case_p("")
    assert not is_snake_case_p("Foo_bar")
    assert not is_snake_case_p("foo__bar")
    assert not is_snake_case_p("_foo")
    assert not is_snake_case_p("foo-bar")


def test_is_kebab_case_p():
    assert is_kebab_case_p("foo")
    assert is_kebab_case_p("foo-bar2")
    assert not is_kebab_case_p("")
    assert not is_kebab_case_p("Foo-bar")
    assert not is_kebab_case_p("foo--bar")
    assert not is_kebab_case_p("foo_bar")


def test_is_camel_case_p():
    assert is_camel_case_p("foo")
    assert is_camel_case_p("fooBar2")
    assert not is_camel_case_p("")
    assert not is_camel_case_p("FooBar")
    assert not is_camel_case_p("foo_bar")


@pytest.mark.parametrize(
    "predicate",
    [
        is_stripped_p,
        is_blank_p,
        is_single_line_p,
        is_capitalized_p,
        is_snake_case_p,
        is_kebab_case_p,
        is_camel_case_p,
    ],
)
def test_generators(predicate):
    assert_generated_true(predicate)
    assert_generated_false(predicate)
