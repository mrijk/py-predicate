from dataclasses import dataclass
from itertools import takewhile
from typing import Any, Iterable, override

from more_itertools import ilen

from predicate.predicate import Predicate, resolve_predicate


@dataclass
class AnyPredicate[T](Predicate[T]):
    """A predicate class that models the 'any' predicate."""

    predicate: Predicate[T]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return any(self.predicate(x) for x in iterable)

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate in self.predicate

    def __repr__(self) -> str:
        return f"any_p({self.predicate!r})"

    @override
    def get_klass(self) -> type:
        return self.predicate.klass

    @override
    @property
    def count(self) -> int:
        return 1 + self.predicate.count

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": f"No item matches predicate {self.predicate!r}"}

    @override
    def consumes(self, iterable: Iterable[Any]) -> Iterable[int]:
        consumed = takewhile(~self.predicate, iterable)
        len_consumed = ilen(consumed)
        len_iterable = ilen(iterable)
        if len_consumed < len_iterable:
            yield from range(len_consumed, len_iterable + 1)
        else:
            yield 0


def any_p[T](predicate: Predicate[T]) -> AnyPredicate[T]:
    """Return True if the predicate holds for any item in the iterable, otherwise False."""
    return AnyPredicate(predicate=resolve_predicate(predicate))
