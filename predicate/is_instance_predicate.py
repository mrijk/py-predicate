from dataclasses import dataclass

from predicate.predicate import Predicate


@dataclass
class IsInstancePredicate[T](Predicate[T]):
    """A predicate class that models the 'isinstance' predicate."""

    klass: type | tuple

    def __call__(self, x: object) -> bool:
        return isinstance(x, self.klass)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsInstancePredicate) and self.klass == other.klass

    def __repr__(self) -> str:
        name = self.klass[0].__name__  # type: ignore
        return f"is_{name}_p"
