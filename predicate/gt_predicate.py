from dataclasses import dataclass
from typing import override

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class GtPredicate[T](Predicate[T]):
    """A predicate class that models the 'gt' (>) predicate."""

    v: ConstrainedT

    def __call__(self, x: T) -> bool:
        return x > self.v

    def __repr__(self) -> str:
        return f"gt_p({self.v!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not greater than {self.v!r}"}
