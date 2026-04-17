from dataclasses import dataclass
from itertools import takewhile
from typing import Any, Iterable, Iterator, override

from more_itertools import first, ilen

from predicate.predicate import Predicate, resolve_predicate


@dataclass
class AllPredicate[T](Predicate[T]):
    """A predicate class that models the 'all' predicate."""

    predicate: Predicate[T]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iterable)

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate in self.predicate

    def __repr__(self) -> str:
        return f"all_p({self.predicate!r})"

    @override
    @property
    def klass(self) -> type:
        return self.predicate.klass

    @override
    @property
    def count(self) -> int:
        return 1 + self.predicate.count

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        index, item = first((i, x) for i, x in enumerate(iterable) if not self.predicate(x))
        return {"index": index, "value": item} | self.predicate.explain_failure(item)

    @override
    def consumes(self, iterable: Iterable[Any]) -> Iterator[int]:
        consumed = takewhile(self.predicate, iterable)
        yield from range(0, ilen(consumed) + 1)


def all_p[T](predicate: Predicate[T]) -> AllPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return AllPredicate(predicate=resolve_predicate(predicate))
