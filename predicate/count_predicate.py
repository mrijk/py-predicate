from dataclasses import dataclass
from typing import Iterable, override

from more_itertools import ilen

from predicate.eq_predicate import eq_p
from predicate.predicate import Explanation, Predicate


@dataclass
class CountPredicate[T](Predicate[T]):
    """A predicate class that models the 'count' predicate."""

    predicate: Predicate[T]
    length_p: Predicate[int]

    def _count(self, iterable: Iterable[T]) -> int:
        return ilen(x for x in iterable if self.predicate(x))

    def __call__(self, iterable: Iterable[T]) -> bool:
        return self.length_p(self._count(iterable))

    def __repr__(self) -> str:
        return f"count_p({self.predicate!r}, {self.length_p!r})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> Explanation:
        return {"reason": f"Expected count {self.length_p!r}, actual: {self._count(iterable)}"}


def count_p[T](predicate: Predicate[T], length_p: Predicate[int]) -> CountPredicate[T]:
    """Return True if the number of items matching predicate satisfies length_p, otherwise False."""
    return CountPredicate(predicate=predicate, length_p=length_p)


def exactly_zero_p[T](predicate: Predicate[T]) -> CountPredicate[T]:
    """Return True if no item of the iterable matches the predicate, otherwise False."""
    return count_p(predicate, eq_p(0))


def exactly_one_p[T](predicate: Predicate[T]) -> CountPredicate[T]:
    """Return True if exactly one item of the iterable matches the predicate, otherwise False."""
    return count_p(predicate, eq_p(1))
