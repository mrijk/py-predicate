"""Strategies for the string predicates: str methods, starts_with_p/ends_with_p and regular expressions."""

from typing import Any

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate.function_predicate import FnPredicate
from predicate.is_regex_predicate import IsRegexPredicate
from predicate.predicate import Predicate
from predicate.regex_predicate import RegexPredicate

# Each strategy only has to generate values the str method accepts; from_text filters on the predicate anyway
_STR_METHODS: dict[str, SearchStrategy[str]] = {
    "isalnum": st.text(st.characters(categories=["L", "N"]), min_size=1),
    "isalpha": st.text(st.characters(categories=["L"]), min_size=1),
    "isascii": st.text(st.characters(codec="ascii")),
    "isdecimal": st.text(st.characters(categories=["Nd"]), min_size=1),
    "isdigit": st.text(st.characters(categories=["Nd"]), min_size=1),
    "isidentifier": st.from_regex(r"[A-Za-z_][A-Za-z0-9_]*", fullmatch=True),
    "islower": st.text(st.characters(categories=["Ll"]), min_size=1),
    "isnumeric": st.text(st.characters(categories=["N"]), min_size=1),
    "isprintable": st.text(st.characters(exclude_categories=["C", "Zl", "Zp", "Zs"], include_characters=" ")),
    "isspace": st.text(st.sampled_from(" \t\n\r\x0b\x0c"), min_size=1),
    "istitle": st.from_regex(r"[A-Z][a-z]*( [A-Z][a-z]*)*", fullmatch=True),
    "isupper": st.text(st.characters(categories=["Lu"]), min_size=1),
}


def from_text(predicate: Predicate[Any]) -> SearchStrategy[str] | None:
    """Return a strategy for a string predicate, or None if the predicate isn't one."""
    match predicate:
        case RegexPredicate():
            # ponytail: no trailing text after the match, though re.match allows it
            strategy: SearchStrategy[str] | None = st.from_regex(predicate.regex, fullmatch=True)
        case IsRegexPredicate():
            strategy = st.text()
        case FnPredicate(fn):
            strategy = _from_fn(fn)
        case _:
            strategy = None
    return None if strategy is None else strategy.filter(predicate)


def _from_fn(fn: Any) -> SearchStrategy[str] | None:
    name = getattr(fn, "__name__", None)
    if name in _STR_METHODS and fn is getattr(str, name):
        return _STR_METHODS[name]
    if (prefix := _closed_over_str(fn, "starts_with_p")) is not None:
        return st.text().map(lambda text: prefix + text)
    if (suffix := _closed_over_str(fn, "ends_with_p")) is not None:
        return st.text().map(lambda text: text + suffix)
    return None


def _closed_over_str(fn: Any, owner: str) -> str | None:
    """Return the str that the lambda inside owner (starts_with_p or ends_with_p) closes over, otherwise None.

    ponytail: this reads a closure cell, because those predicates are plain fn_p lambdas that hold no data. If
    str_predicates changes, this stops matching and the predicate falls back to the usual TypeError; give them a
    real predicate class to replace it.
    """
    from_owner = getattr(fn, "__module__", None) == "predicate.str_predicates" and getattr(
        fn, "__qualname__", ""
    ).startswith(f"{owner}.")
    cells: tuple[Any, ...] = getattr(fn, "__closure__", None) or ()
    value = cells[0].cell_contents if from_owner and len(cells) == 1 else None
    return value if isinstance(value, str) else None
