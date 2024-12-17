from dataclasses import dataclass
from typing import Iterable, override

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

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": f"Expected length {self.length}, actual: {ilen(iterable)}"}
