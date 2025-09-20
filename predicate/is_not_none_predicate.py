from dataclasses import dataclass
from functools import partial
from typing import Final, override

from predicate.predicate import Predicate, and_p


@dataclass
class IsNotNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is not none' predicate."""

    def __call__(self, x: T) -> bool:
        return x is not None

    def __repr__(self) -> str:
        return "is_not_none_p"

    @override
    def explain_failure(self, _x: T) -> dict:
        return {"reason": "Value is None"}


is_not_none_p: Final[IsNotNonePredicate] = IsNotNonePredicate()
"""Return True if value is not None, otherwise False."""


none_is_false_p = partial(and_p, is_not_none_p)
"""Return False if value is None, otherwise the result of the predicate."""
