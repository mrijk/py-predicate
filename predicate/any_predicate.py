from dataclasses import dataclass
from typing import Iterable

from predicate.predicate import Predicate


@dataclass
class AnyPredicate[T](Predicate[T]):
    """A predicate class that models the 'any' predicate."""

    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return any(self.predicate(x) for x in iter)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AnyPredicate) and self.predicate == other.predicate

    def __repr__(self) -> str:
        return f"any({repr(self.predicate)})"
