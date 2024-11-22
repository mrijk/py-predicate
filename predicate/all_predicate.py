from dataclasses import dataclass
from typing import Iterable

from predicate.predicate import Predicate


@dataclass
class AllPredicate[T](Predicate[T]):
    """A predicate class that models the 'all' predicate."""

    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iter)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AllPredicate) and self.predicate == other.predicate

    def __repr__(self) -> str:
        return f"all({repr(self.predicate)})"
