from dataclasses import dataclass
from typing import Iterable, override

from more_itertools import ilen

from predicate.predicate import Predicate


@dataclass
class HasLengthPredicate[T](Predicate[T]):
    """A predicate class that models the 'length' predicate."""

    length_p: Predicate[int]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return self.length_p(ilen(iterable))

    def __repr__(self) -> str:
        return f"has_length_p({self.length_p!r})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": f"Expected length {self.length_p!r}, actual: {ilen(iterable)}"}
