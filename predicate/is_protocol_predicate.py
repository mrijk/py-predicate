from dataclasses import dataclass
from typing import Protocol

from predicate.predicate import Predicate


@dataclass
class IsProtocolPredicate[T](Predicate[T]):
    """A predicate class that models the 'is a protocol' predicate."""

    def __call__(self, x: type) -> bool:
        return issubclass(x, Protocol)


def is_protocol_p() -> Predicate:
    """Return True if value is Protocol, otherwise False."""
    return IsProtocolPredicate()
