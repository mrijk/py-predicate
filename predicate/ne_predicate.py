from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class NePredicate[T](Predicate[T]):
    """A predicate class that models the 'ne' (!=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x != self.v

    def __repr__(self) -> str:
        return f"ne_p({self.v})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is equal to {self.v}"}
