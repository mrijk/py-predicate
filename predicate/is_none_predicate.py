from dataclasses import dataclass
from typing import Final, override

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
