from dataclasses import dataclass
from typing import Final, override

from predicate.predicate import Predicate


@dataclass
class IsTruthyPredicate[T](Predicate[T]):
    """A predicate class that the truthy (13, True, [1], "foo", etc.) predicate."""

    def __call__(self, x: T) -> bool:
        return bool(x)

    def __repr__(self) -> str:
        return "is_truthy_p"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not a truthy value"}


is_truthy_p: Final[IsTruthyPredicate] = IsTruthyPredicate()
"""Returns True if the value is truthy, otherwise False."""
