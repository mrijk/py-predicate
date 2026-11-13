from dataclasses import dataclass
from typing import Any, override

from predicate.predicate import Predicate, SupportsComparison


@dataclass
class GePredicate[T: SupportsComparison](Predicate[T]):
    """A predicate class that models the 'ge' (>=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x >= self.v

    def __repr__(self) -> str:
        return f"ge_p({self.v!r})"

    @override
    @property
    def klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict[str, Any]:
        return {"reason": f"{x} is not greater or equal to {self.v!r}"}


def ge_p[T: SupportsComparison](v: T) -> GePredicate[T]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GePredicate(v=v)
