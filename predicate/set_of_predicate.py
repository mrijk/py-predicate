from dataclasses import dataclass

from predicate.predicate import Predicate


@dataclass
class SetOfPredicate[T](Predicate[T]):
    """A predicate class that models the set_of predicate."""

    predicate: Predicate

    def __call__(self, x: set[T]) -> bool:
        return all(self.predicate(item) for item in x)

    def __repr__(self) -> str:
        return f"is_set_of_p({repr(self.predicate)})"
