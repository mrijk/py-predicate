from dataclasses import dataclass

from predicate import Predicate


@dataclass
class PropertyPredicate[T](Predicate[T]):
    """A predicate class that wraps a boolean property."""

    getter: property

    def __call__(self, obj: T) -> bool:
        return self.getter.fget(obj)

    def __repr__(self) -> str:
        return "todo"
