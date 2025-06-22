from dataclasses import dataclass
from typing import Iterable, override

from predicate.in_predicate import class_from_set
from predicate.predicate import Predicate


@dataclass
class NotInPredicate[T](Predicate[T]):
    """A predicate class that models the 'not in' predicate."""

    v: set[T]

    def __init__(self, v: Iterable[T]):
        self.v = set(v)

    def __call__(self, x: T) -> bool:
        return x not in self.v

    def __repr__(self) -> str:
        items = ", ".join(str(item) for item in self.v)
        return f"not_in_p({items})"

    @override
    def get_klass(self) -> type:
        return class_from_set(self.v)


def not_in_p[T](*v: T) -> NotInPredicate[T]:
    """Return True if the values are not in the set, otherwise False."""
    return NotInPredicate(v=v)
