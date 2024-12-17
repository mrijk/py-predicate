from dataclasses import dataclass
from typing import Final, Iterable, override

from predicate.predicate import Predicate


@dataclass
class IsEmptyPredicate[T](Predicate[T]):
    """A predicate class that models the 'empty' predicate."""

    def __call__(self, iter: Iterable[T]) -> bool:
        return len(list(iter)) == 0

    def __repr__(self) -> str:
        return "is_empty_p"

    @override
    def explain_failure(self, x: Iterable[T]) -> dict:
        return {"reason": f"Iterable {x} is not empty"}


@dataclass
class IsNotEmptyPredicate[T](Predicate[T]):
    """A predicate class that models the 'not empty' predicate."""

    def __call__(self, iter: Iterable[T]) -> bool:
        return len(list(iter)) > 0

    def __repr__(self) -> str:
        return "is_not_empty_p"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"Iterable {x} is empty"}


is_empty_p: Final[IsEmptyPredicate] = IsEmptyPredicate()
"""Predicate that returns True if the iterable is empty, otherwise False."""

is_not_empty_p: Final[IsNotEmptyPredicate] = IsNotEmptyPredicate()
"""Predicate that returns True if the iterable is not empty, otherwise False."""
