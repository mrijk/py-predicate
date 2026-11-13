from dataclasses import dataclass
from typing import Any, Final, override

from predicate.predicate import Predicate, SupportsComparison


@dataclass
class GtPredicate[T: SupportsComparison](Predicate[T]):
    """A predicate class that models the 'gt' (>) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x > self.v

    def __repr__(self) -> str:
        return f"gt_p({self.v!r})"

    @override
    @property
    def klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict[str, Any]:
        return {"reason": f"{x} is not greater than {self.v!r}"}


def gt_p[T: SupportsComparison](v: T) -> GtPredicate[T]:
    """Return True if the value is greater than the constant, otherwise False."""
    return GtPredicate(v=v)


pos_p: Final[GtPredicate[Any]] = gt_p(0)
"""Returns True of the value is positive, otherwise False."""
