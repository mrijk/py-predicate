from dataclasses import dataclass
from typing import Any, override

from predicate.predicate import Predicate, SupportsComparison


@dataclass
class LePredicate[T: SupportsComparison](Predicate[T]):
    """A predicate class that models the 'le' (<=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x <= self.v

    def __repr__(self) -> str:
        return f"le_p({self.v!r})"

    @override
    @property
    def klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict[str, Any]:
        return {"reason": f"{x} is not less than or equal to {self.v!r}"}


def le_p[T: SupportsComparison](v: T) -> LePredicate[T]:
    """Return True if the value is less than or equal to the constant, otherwise False."""
    return LePredicate(v=v)
