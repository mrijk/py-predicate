from dataclasses import dataclass
from functools import partial
from typing import Final, Iterable, override

from more_itertools import ilen

from predicate.eq_predicate import eq_p
from predicate.predicate import Predicate


@dataclass
class CountPredicate[T](Predicate[T]):
    """A predicate class that models the 'length' predicate."""

    predicate: Predicate[T]
    length_p: Predicate[int]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return self.length_p(ilen(x for x in iterable if self.predicate(x)))

    def __repr__(self) -> str:
        return f"count_p({self.predicate!r}, {self.length_p!r})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        actual_length = ilen(x for x in iterable if self.predicate(x))
        return {"reason": f"Expected count {self.length_p!r}, actual: {actual_length}"}


def count_p[T](predicate: Predicate[T], length_p: Predicate[int]) -> Predicate[T]:
    """Return True if length of iterable is equal to value, otherwise False."""
    return CountPredicate(predicate=predicate, length_p=length_p)


exactly_zero_p: Final[Predicate] = partial(count_p, length_p=eq_p(0))  # type: ignore
"""Predicate that returns True if the iterable doesn't match the predicate, otherwise False."""

exactly_one_p: Final[Predicate] = partial(count_p, length_p=eq_p(1))  # type: ignore
"""Predicate that returns True if the iterable matches the predicate exactly once, otherwise False."""
