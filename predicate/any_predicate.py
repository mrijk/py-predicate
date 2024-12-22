from dataclasses import dataclass
from typing import Iterable, override

from predicate.predicate import Predicate


@dataclass
class AnyPredicate[T](Predicate[T]):
    """A predicate class that models the 'any' predicate."""

    predicate: Predicate[T]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return any(self.predicate(x) for x in iterable)

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate in self.predicate

    def __repr__(self) -> str:
        return f"any({repr(self.predicate)})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": f"No item matches predicate {repr(self.predicate)}"}
