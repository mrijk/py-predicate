import math
from dataclasses import dataclass, field
from typing import override

from predicate.predicate import Predicate


@dataclass
class IsClosePredicate[T](Predicate[T]):
    """A predicate class that models approximate float equality."""

    target: float
    rel_tol: float = field(default=1e-9)
    abs_tol: float = field(default=0.0)

    def __call__(self, x: float) -> bool:
        return math.isclose(x, self.target, rel_tol=self.rel_tol, abs_tol=self.abs_tol)

    @override
    @property
    def klass(self) -> type:
        return float

    def __repr__(self) -> str:
        return f"is_close_p({self.target!r}, rel_tol={self.rel_tol!r}, abs_tol={self.abs_tol!r})"

    @override
    def explain_failure(self, x: float) -> dict:
        return {"reason": f"{x} is not close to {self.target!r}"}


def is_close_p(target: float, *, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> IsClosePredicate:
    """Return True if the value is approximately equal to target, otherwise False."""
    return IsClosePredicate(target=target, rel_tol=rel_tol, abs_tol=abs_tol)
