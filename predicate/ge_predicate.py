from dataclasses import dataclass
from typing import override

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class GePredicate[T](Predicate[T]):
    """A predicate class that models the 'ge' (>=) predicate."""

    v: ConstrainedT

    def __call__(self, x: T) -> bool:
        return x >= self.v

    def __repr__(self) -> str:
        return f"ge_p({self.v})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not greater or equal to {self.v}"}
