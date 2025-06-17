from dataclasses import dataclass
from typing import Final, Iterable, override

from more_itertools import ilen

from predicate.eq_predicate import zero_p
from predicate.gt_predicate import pos_p
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


def has_length_p(length_p: Predicate[int]) -> Predicate[Iterable]:
    """Return True if length of iterable is equal to value, otherwise False."""
    return HasLengthPredicate(length_p=length_p)


is_empty_p: Final[Predicate[Iterable]] = has_length_p(zero_p)
"""Predicate that returns True if the iterable is empty, otherwise False."""

is_not_empty_p: Final[Predicate[Iterable]] = has_length_p(pos_p)
"""Predicate that returns True if the iterable is not empty, otherwise False."""
