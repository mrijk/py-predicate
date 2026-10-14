from dataclasses import dataclass
from typing import Any, TypeGuard, override

from predicate.helpers import all_true, first_false
from predicate.predicate import Predicate


@dataclass
class FrozenSetOfPredicate[T](Predicate[T]):
    """A predicate class that models the frozenset_of predicate."""

    predicate: Predicate

    def __call__(self, x: Any) -> TypeGuard[frozenset[T]]:
        match x:
            case frozenset() as s:
                return all_true(s, self.predicate)
            case _:
                return False

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.predicate

    def __repr__(self) -> str:
        return f"is_frozenset_of_p({self.predicate})"

    @property
    def klass(self) -> type:
        return self.predicate.klass

    @override
    def explain_failure(self, x: frozenset[T]) -> dict:
        match x:
            case frozenset() as s:
                fail = first_false(s, self.predicate)
                return {"reason": f"Item '{fail}' didn't match predicate {self.predicate}"}
            case _:
                return {"reason": f"{x} is not an instance of a frozenset"}


def is_frozenset_of_p[T](predicate: Predicate[T]) -> "FrozenSetOfPredicate[T]":
    """Return True if value is a frozenset, and for all elements in the frozenset the predicate is True, otherwise False."""
    return FrozenSetOfPredicate(predicate)
