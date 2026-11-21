from dataclasses import dataclass
from typing import Any, override

from predicate.predicate import Predicate


@dataclass
class AcceptsPredicate[T](Predicate[type]):
    """A predicate class that models the 'accept type' predicate."""

    predicate: Predicate[T]

    @override
    def __call__(self, x: type) -> bool:
        try:
            klass = self.predicate.klass
        except NotImplementedError:
            return True
        if klass is type(Any):
            return True
        if isinstance(klass, tuple):
            return True
        if x is bool and klass is int:
            return False
        return issubclass(x, klass)

    @override
    def __repr__(self) -> str:
        return f"accepts_p({self.predicate!r})"


def accepts_p[T](predicate: Predicate[T]) -> AcceptsPredicate[T]:
    """Return True if the predicate accepts the type, otherwise False."""
    return AcceptsPredicate(predicate=predicate)
