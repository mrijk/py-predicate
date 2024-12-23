from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class IsFalsyPredicate[T](Predicate[T]):
    """A predicate class that the falsy (0, False, [], "", etc.) predicate."""

    def __call__(self, x: T) -> bool:
        return not bool(x)

    def __repr__(self) -> str:
        return "is_falsy_p"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not a falsy value"}
