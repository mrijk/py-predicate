from collections.abc import Callable

from predicate.fn_predicate import FnPredicate
from predicate.predicate import Predicate
from predicate.standard_predicates import fn_p


def create_is_str_p(fn: Callable) -> Predicate[str]:
    return fn_p(fn=fn)


is_alnum_p = create_is_str_p(str.isalnum)
"""Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise."""

is_alpha_p = create_is_str_p(str.isalpha)
"""Return True if all characters in the string are alphabetic and there is at least one character, False otherwise."""

is_ascii_p = create_is_str_p(str.isascii)
"""Return True if the string is empty or all characters in the string are ASCII, False otherwise."""

is_decimal_p = create_is_str_p(str.isdecimal)
"""Return True if all characters in the string are decimal characters and there is at least one character, False otherwise."""

is_digit_p = create_is_str_p(str.isdigit)
"""Return True if all characters in the string are digits and there is at least one character, False otherwise."""

is_identifier_p = create_is_str_p(str.isidentifier)
"""Return True if the string is a valid identifier according to the language definition, False otherwise."""

is_lower_p = create_is_str_p(str.islower)
"""Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise."""

is_numeric_p = create_is_str_p(str.isnumeric)
"""Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise."""

is_printable_p = create_is_str_p(str.isprintable)
"""Return True if all characters in the string are printable or the string is empty, False otherwise."""

is_space_p = create_is_str_p(str.isspace)
"""Return True if there are only whitespace characters in the string and there is at least one character, False otherwise."""

is_title_p = create_is_str_p(str.istitle)
"""Return True if the string is a titlecased string and there is at least one character, False otherwise."""

is_upper_p = create_is_str_p(str.isupper)
"""Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise."""


def starts_with_p(prefix: str) -> Predicate[str]:
    """Return True if the string starts with the specified prefix, False otherwise."""
    return FnPredicate(lambda x: x.startswith(prefix))


def ends_with_p(suffix: str) -> Predicate[str]:
    """Return True if the string ends with the specified suffix, False otherwise."""
    return FnPredicate(lambda x: x.endswith(suffix))
