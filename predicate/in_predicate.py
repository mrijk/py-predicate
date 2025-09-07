from dataclasses import dataclass
from typing import Any, Container, Iterable, override

from more_itertools import first

from predicate.predicate import Predicate


def class_from_set(v: Iterable):
    # TODO: v could have different types
    types = (type(value) for value in v)
    return first(types, Any)  # type: ignore


@dataclass
class InPredicate[T](Predicate[T]):
    """A predicate class that models the 'in' predicate."""

    v: Container[T]

    def __init__(self, v: Container[T]):
        self.v = v

    def __call__(self, x: T) -> bool:
        return x in self.v

    def __repr__(self) -> str:
        if isinstance(self.v, Iterable):
            items = ", ".join(str(item) for item in self.v)
            return f"in_p({items})"
        return f"in_p({self.v.__class__.__name__}())"

    def __eq__(self, other: object) -> bool:
        match other:
            case InPredicate(v) if isinstance(self.v, Iterable) and isinstance(v, Iterable):
                # TODO: don't do this when self.v or v are large!
                return set(self.v) == set(v)
            case _:
                return False

    @override
    def get_klass(self) -> type:
        if isinstance(self.v, Iterable):
            return class_from_set(self.v)
        return Any


def in_p[T](v: Container[T]) -> InPredicate[T]:
    """Return True if the values are included in the set, otherwise False."""
    return InPredicate(v=v)
