from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class EqPredicate[T](Predicate[T]):
    """A predicate class that models the 'eq' (=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x == self.v

    def __repr__(self) -> str:
        return f"eq_p({self.v})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not equal to {self.v}"}
