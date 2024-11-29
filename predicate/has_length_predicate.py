from dataclasses import dataclass
from typing import Iterable

from more_itertools import ilen

from predicate.predicate import Predicate


@dataclass
class HasLengthPredicate[T](Predicate[T]):
    """A predicate class that models the 'length' predicate."""

    length: int

    def __call__(self, iterable: Iterable[T]) -> bool:
        return ilen(iterable) == self.length

    def __repr__(self) -> str:
        return f"has_length_p({self.length})"
