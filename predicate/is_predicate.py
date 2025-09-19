from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class IsPredicate[T](Predicate[T]):
    """A predicate class that models the 'is' predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x is self.v

    def __repr__(self) -> str:
        return f"is_p({self.v!r})"

    @override
    def get_klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} does not refer to {self.v!r}"}


def is_p[T](v: T) -> IsPredicate[T]:
    """Return True if the value is equal to the constant, otherwise False."""
    return IsPredicate(v=v)
