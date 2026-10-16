from dataclasses import dataclass
from typing import Protocol, override

from predicate.predicate import Predicate


@dataclass
class IsProtocolPredicate[T](Predicate[T]):
    """A predicate class that models the 'is a protocol' predicate."""

    def __call__(self, x: type) -> bool:
        return issubclass(x, Protocol)

    def __repr__(self) -> str:
        return "is_protocol_p"

    @override
    def explain_failure(self, x: type) -> dict:
        return {"reason": f"{x} is not a Protocol"}


def is_protocol_p() -> Predicate:
    """Return True if value is Protocol, otherwise False."""
    return IsProtocolPredicate()
