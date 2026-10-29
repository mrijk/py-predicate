import random
import string
from typing import Callable, Iterator

from predicate import fn_p
from predicate.predicate import Predicate


def create_is_str_p(fn: Callable, alphabet: str | None = None) -> Predicate[str]:
    """Return a predicate for a str method such as str.isdigit; with an alphabet, it generates strings from it."""
    if alphabet is None:
        return fn_p(fn=fn)
    return fn_p(fn=fn, generate_true_fn=lambda: _random_strings_from(alphabet))


def _random_strings_from(alphabet: str) -> Iterator[str]:
    # ponytail: ASCII only, though e.g. str.isdigit also accepts digits from other scripts
    while True:
        yield "".join(random.choices(alphabet, k=random.randint(1, 10)))


is_alnum_p = create_is_str_p(str.isalnum, string.ascii_letters + string.digits)
"""Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise."""

is_alpha_p = create_is_str_p(str.isalpha, string.ascii_letters)
"""Return True if all characters in the string are alphabetic and there is at least one character, False otherwise."""

is_ascii_p = create_is_str_p(str.isascii, string.printable)
"""Return True if the string is empty or all characters in the string are ASCII, False otherwise."""

is_decimal_p = create_is_str_p(str.isdecimal, string.digits)
"""Return True if all characters in the string are decimal characters and there is at least one character, False otherwise."""

is_digit_p = create_is_str_p(str.isdigit, string.digits)
"""Return True if all characters in the string are digits and there is at least one character, False otherwise."""

is_identifier_p = create_is_str_p(str.isidentifier)
"""Return True if the string is a valid identifier according to the language definition, False otherwise."""

is_lower_p = create_is_str_p(str.islower, string.ascii_lowercase)
"""Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise."""

is_numeric_p = create_is_str_p(str.isnumeric, string.digits)
"""Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise."""

is_printable_p = create_is_str_p(str.isprintable, string.printable.strip())
"""Return True if all characters in the string are printable or the string is empty, False otherwise."""

is_space_p = create_is_str_p(str.isspace, string.whitespace)
"""Return True if there are only whitespace characters in the string and there is at least one character, False otherwise."""

is_title_p = create_is_str_p(str.istitle)
"""Return True if the string is a titlecased string and there is at least one character, False otherwise."""

is_upper_p = create_is_str_p(str.isupper, string.ascii_uppercase)
"""Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise."""


def starts_with_p(prefix: str) -> Predicate[str]:
    """Return True if the string starts with the specified prefix, False otherwise."""
    return fn_p(fn=lambda x: x.startswith(prefix))


def ends_with_p(suffix: str) -> Predicate[str]:
    """Return True if the string ends with the specified suffix, False otherwise."""
    return fn_p(fn=lambda x: x.endswith(suffix))
