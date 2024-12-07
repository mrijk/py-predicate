from dataclasses import dataclass

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class LePredicate[T](Predicate[T]):
    """A predicate class that models the 'le' (<=) predicate."""

    v: ConstrainedT

    def __call__(self, x: T) -> bool:
        return x <= self.v

    def __repr__(self) -> str:
        return f"le_p({self.v})"
