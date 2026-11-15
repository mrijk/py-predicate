import re

import pytest
from hypothesis import given, settings

from predicate import all_p, fn_p, is_dict_of_p, is_even_p, is_int_p, is_list_of_p, is_str_p
from predicate.hypothesis import from_predicate
from predicate.integrations.hypothesis import strings
from predicate.is_regex_predicate import is_regex_p
from predicate.regex_predicate import RegexPredicate, regex_p
from predicate.str_predicates import (
    ends_with_p,
    is_alnum_p,
    is_alpha_p,
    is_ascii_p,
    is_decimal_p,
    is_digit_p,
    is_identifier_p,
    is_lower_p,
    is_numeric_p,
    is_printable_p,
    is_space_p,
    is_title_p,
    is_upper_p,
    starts_with_p,
)

predicates = {
    "is_alnum_p": is_alnum_p,
    "is_alpha_p": is_alpha_p,
    "is_ascii_p": is_ascii_p,
    "is_decimal_p": is_decimal_p,
    "is_digit_p": is_digit_p,
    "is_identifier_p": is_identifier_p,
    "is_lower_p": is_lower_p,
    "is_numeric_p": is_numeric_p,
    "is_printable_p": is_printable_p,
    "is_space_p": is_space_p,
    "is_title_p": is_title_p,
    "is_upper_p": is_upper_p,
    "fn_p(str.isalpha)": fn_p(str.isalpha),
    "starts_with_p": starts_with_p("ab"),
    "starts_with_p empty": starts_with_p(""),
    "ends_with_p": ends_with_p("yz"),
    "regex_p": regex_p("[a-z]+[0-9]"),
    "regex_p anchored": regex_p("^abc$"),
    "regex_p flags": RegexPredicate("abc", re.IGNORECASE),
    "is_regex_p": is_regex_p,
    "is_str_p & starts_with_p": is_str_p & starts_with_p("a"),
    "is_str_p & is_alpha_p": is_str_p & is_alpha_p,
    "is_int_p & is_even_p": is_int_p & is_even_p,
    "starts_with_p | ends_with_p": starts_with_p("a") | ends_with_p("z"),
    "all_p(is_digit_p)": all_p(is_digit_p),
    "is_list_of_p(starts_with_p)": is_list_of_p(starts_with_p("x")),
    "is_dict_of_p": is_dict_of_p(("name", is_alpha_p), ("code", is_digit_p)),
}


@pytest.mark.parametrize("predicate", predicates.values(), ids=predicates.keys())
def test_from_predicate_satisfies_string_predicate(predicate):
    @settings(max_examples=50)
    @given(from_predicate(predicate))
    def check(x):
        assert predicate(x)

    check()


@pytest.mark.parametrize("name", strings._STR_METHODS)
def test_str_method_strategy_is_valid_without_the_filter(name):
    @settings(max_examples=100)
    @given(strings._STR_METHODS[name])
    def check(x):
        assert getattr(str, name)(x)

    check()


def test_starts_with_and_ends_with_use_the_given_text():
    @given(from_predicate(starts_with_p("ab")))
    def starts(x):
        assert x.startswith("ab")

    @given(from_predicate(ends_with_p("yz")))
    def ends(x):
        assert x.endswith("yz")

    starts()
    ends()


def test_str_method_strategies_cover_all_str_predicates():
    assert set(strings._STR_METHODS) == {f"is{name}" for name in "alnum alpha ascii decimal digit".split()} | {
        "isidentifier",
        "islower",
        "isnumeric",
        "isprintable",
        "isspace",
        "istitle",
        "isupper",
    }


def test_look_alike_lambda_is_not_mistaken_for_starts_with_p():
    with pytest.raises(TypeError):
        from_predicate(fn_p(lambda x: x.startswith("a")))


def test_unknown_fn_predicate_still_has_no_strategy():
    with pytest.raises(TypeError):
        from_predicate(fn_p(str.casefold))


def test_regex_with_flags_generates_matching_strings():
    @given(from_predicate(RegexPredicate("abc", re.IGNORECASE)))
    def check(x):
        assert x.lower() == "abc"

    check()
