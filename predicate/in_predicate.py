from dataclasses import dataclass
from typing import Any, Iterable, override

from more_itertools import first

from predicate.predicate import Predicate


def class_from_set(v: set):
    # TODO: v could have different types
    types = (type(value) for value in v)
    return first(types, Any)  # type: ignore


@dataclass
class InPredicate[T](Predicate[T]):
    """A predicate class that models the 'in' predicate."""

    v: set[T]

    def __init__(self, v: Iterable[T]):
        self.v = set(v)

    def __call__(self, x: T) -> bool:
        return x in self.v

    def __repr__(self) -> str:
        items = ", ".join(str(item) for item in self.v)
        return f"in_p({items})"

    @override
    def get_klass(self) -> type:
        return class_from_set(self.v)


def in_p[T](*v: T) -> InPredicate[T]:
    """Return True if the values are included in the set, otherwise False."""
    return InPredicate(v=v)
