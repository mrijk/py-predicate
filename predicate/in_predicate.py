from collections.abc import Sized
from dataclasses import dataclass
from typing import Any, Container, Iterable, override

from predicate.predicate import Predicate


def class_from_set(v: Iterable):
    types = {type(value) for value in v}
    if len(types) == 1:
        return next(iter(types))
    return Any


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
                if isinstance(self.v, Sized) and isinstance(v, Sized) and (len(self.v) > 1000 or len(v) > 1000):
                    return self.v == v
                return set(self.v) == set(v)
            case _:
                return False

    @override
    def explain_failure(self, x: Any) -> dict:
        return {"reason": f"{x} is not in {self!r}"}

    @override
    @property
    def klass(self) -> type:
        if isinstance(self.v, Iterable):
            return class_from_set(self.v)
        return Any


def in_p[T](v: Container[T]) -> InPredicate[T]:
    """Return True if the values are included in the set, otherwise False."""
    return InPredicate(v=v)
