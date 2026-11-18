import random
import re
import string
from typing import Any, Callable, Iterator

from predicate import fn_p
from predicate.predicate import Predicate


def create_is_str_p(fn: Callable[..., Any], alphabet: str | None = None) -> Predicate[str]:
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


def _word() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))


def _words(sep: str) -> str:
    return sep.join(_word() for _ in range(random.randint(1, 3)))


def _camel() -> str:
    return _word() + "".join(_word().capitalize() for _ in range(random.randint(0, 2)))


def _forever(make: Callable[[], str]) -> Callable[[], Iterator[str]]:
    return lambda: iter(make, None)


def _str_p(fn: Callable[[str], bool], true: Callable[[], str], false: Callable[[], str]) -> Predicate[str]:
    return fn_p(fn=fn, generate_true_fn=_forever(true), generate_false_fn=_forever(false))


def _matches(pattern: str) -> Callable[[str], bool]:
    regex = re.compile(pattern)
    return lambda x: regex.fullmatch(x) is not None


is_stripped_p = _str_p(
    lambda x: x == x.strip(), _word, lambda: random.choice([" ", "\t", "\n"]) + _word() + random.choice([" ", "\n"])
)
"""Return True if the string has no leading or trailing whitespace, False otherwise."""

is_blank_p = _str_p(lambda x: not x.strip(), lambda: random.choice(string.whitespace) * random.randint(0, 5), _word)
"""Return True if the string is empty or only contains whitespace, False otherwise."""

is_single_line_p = _str_p(lambda x: "\n" not in x, _word, lambda: _word() + "\n" + _word())
"""Return True if the string contains no newline, False otherwise."""

is_capitalized_p = _str_p(lambda x: x[:1].isupper() and x[1:] == x[1:].lower(), lambda: _word().capitalize(), _word)
"""Return True if the first character is uppercase and the rest is lowercase, False otherwise."""

# ponytail: ASCII only, no leading/trailing/double separators; loosen the patterns if that turns out too strict
is_snake_case_p = _str_p(_matches(r"[a-z0-9]+(_[a-z0-9]+)*"), lambda: _words("_"), lambda: _words("_").upper())
"""Return True if the string is snake_case, False otherwise."""

is_kebab_case_p = _str_p(_matches(r"[a-z0-9]+(-[a-z0-9]+)*"), lambda: _words("-"), lambda: _words("-").upper())
"""Return True if the string is kebab-case, False otherwise."""

is_camel_case_p = _str_p(_matches(r"[a-z][a-zA-Z0-9]*"), _camel, lambda: _camel().capitalize())
"""Return True if the string is camelCase (starts lowercase, no separators), False otherwise."""
