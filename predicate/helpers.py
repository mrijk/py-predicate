from collections.abc import Iterable
from itertools import filterfalse

from more_itertools import first

from predicate.predicate import Predicate


def all_true[T](iterable: Iterable[T], predicate: Predicate[T]) -> bool:
    return all(predicate(item) for item in iterable)


def first_false[T](iterable: Iterable[T], predicate: Predicate[T]) -> T:
    return first(filterfalse(predicate, iterable))


def predicates_repr(predicates: list[Predicate]) -> str:
    return ", ".join(repr(predicate) for predicate in predicates)


def join_with_or(s: list[str]) -> str:
    first = s[:-1]
    last = s[-1]
    if first:
        return f"{', '.join(first)} or {last}"
    return last
