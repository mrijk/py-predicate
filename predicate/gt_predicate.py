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
        return f"gt_p({self.v})"

    @override
    def explain(self, x: T) -> dict:
        if self(x):
            return {"result": True}
        return {"result": False, "reason": f"{x} is not greater than {self.v}"}
