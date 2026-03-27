import sys
from dataclasses import dataclass
from typing import Final, override

if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing import TypeGuard as TypeIs  # type: ignore[assignment]  # approximation for Python < 3.13

from predicate.predicate import Predicate, and_p, predicate_partial


@dataclass
class IsNotNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is not none' predicate."""

    def __call__(self, x: object) -> TypeIs[T]:
        return x is not None

    def __repr__(self) -> str:
        return "is_not_none_p"

    @override
    def explain_failure(self, _x: T) -> dict:
        return {"reason": "Value is None"}


is_not_none_p: Final[IsNotNonePredicate] = IsNotNonePredicate()
"""Return True if value is not None, otherwise False."""


none_is_false_p = predicate_partial(and_p, is_not_none_p)
"""Return False if value is None, otherwise the result of the predicate."""
