from dataclasses import dataclass
from typing import Final, override

from predicate import exception_p
from predicate.predicate import Predicate


@dataclass
class IsNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is none' predicate."""

    def __call__(self, x: T) -> bool:
        return x is None

    def __repr__(self) -> str:
        return "is_none_p"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not None"}


is_none_p: Final[IsNonePredicate] = IsNonePredicate()
"""Return True if value is None, otherwise False."""


def none_is_true_p[T](predicate: Predicate[T]) -> Predicate[T]:
    """Return True if value is None, otherwise the result of the predicate."""
    return is_none_p | predicate


def none_is_false_p[T](predicate: Predicate[T]) -> Predicate[T]:
    """Return False if value is None, otherwise the result of the predicate."""
    from predicate import is_not_none_p

    return is_not_none_p & predicate


def none_is_exception_p[T](predicate: Predicate[T]) -> Predicate[T]:
    """Raise an exception if value is None, otherwise returns the result of the predicate."""
    return (is_none_p & exception_p) | predicate
