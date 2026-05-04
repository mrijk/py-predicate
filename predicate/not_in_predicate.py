from dataclasses import dataclass
from typing import Any, Container, Iterable, override

from predicate.helpers import join_as_str
from predicate.in_predicate import class_from_set
from predicate.predicate import Predicate


@dataclass
class NotInPredicate[T](Predicate[T]):
    """A predicate class that models the 'not in' predicate."""

    v: Container[T]

    def __init__(self, v: Container[T]):
        self.v = v

    def __call__(self, x: T) -> bool:
        return x not in self.v

    def __repr__(self) -> str:
        if isinstance(self.v, Iterable):
            return f"not_in_p({join_as_str(self.v)})"
        return f"not_in_p({self.v.__class__.__name__}())"

    @override
    def explain_failure(self, x: Any) -> dict:
        return {"reason": f"{x} is in {self!r}"}

    @override
    @property
    def klass(self) -> type:
        if isinstance(self.v, Iterable):
            return class_from_set(self.v)
        return Any


def not_in_p[T](v: Container[T]) -> NotInPredicate[T]:
    """Return True if the values are not in the set, otherwise False."""
    return NotInPredicate(v=v)
