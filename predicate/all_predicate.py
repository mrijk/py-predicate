from dataclasses import dataclass
from typing import Iterable

from predicate.predicate import Predicate


@dataclass
class AllPredicate[T](Predicate[T]):
    """A predicate class that models the 'all' predicate."""

    predicate: Predicate[T]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iterable)

    def __repr__(self) -> str:
        return f"all({repr(self.predicate)})"
