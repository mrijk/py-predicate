from itertools import filterfalse
from typing import Iterable

from more_itertools import first

from predicate.predicate import Predicate


def all_true[T](iterable: Iterable[T], predicate: Predicate[T]) -> bool:
    return all(predicate(item) for item in iterable)


def first_false[T](iterable: Iterable[T], predicate: Predicate[T]) -> T:
    return first(filterfalse(predicate, iterable))


def predicates_repr(predicates: list[Predicate]) -> str:
    return ", ".join(repr(predicate) for predicate in predicates)


def dict_predicates_repr(predicates: dict[str, Predicate]) -> str:
    items = ", ".join(f'"{k}": {v!r}' for k, v in predicates.items())
    return "{" + items + "}"


def key_value_pairs_repr(pairs: list[tuple[Predicate, Predicate]], from_key=repr) -> str:
    return ", ".join(f"({from_key(k)}, {v!r})" for k, v in pairs)


def join_with_or(s: list[str]) -> str:
    first = s[:-1]
    last = s[-1]
    if first:
        return f"{', '.join(first)} or {last}"
    return last
