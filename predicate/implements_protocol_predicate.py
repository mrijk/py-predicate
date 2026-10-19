from dataclasses import dataclass
from inspect import getmembers, isfunction
from typing import override

from predicate.predicate import Predicate
from predicate.same_signature_predicate import same_signature_p


def protocol_members(protocol: type) -> set[str]:
    # ponytail: __protocol_attrs__ is private API (3.12+); typing.get_protocol_members once we require 3.13
    return protocol.__protocol_attrs__  # type: ignore[attr-defined]


@dataclass
class ImplementsProtocolPredicate[T](Predicate[T]):
    """A predicate class that models the 'implements a protocol' predicate."""

    protocol: type
    args_match: bool

    def __call__(self, x: type) -> bool:
        return self._failure(x) is None

    def _failure(self, x: type) -> str | None:
        protocol_attrs = protocol_members(self.protocol)

        # Check the class itself, so x is never instantiated. Data members count when set or annotated on the class
        # ponytail: attributes only assigned in __init__ are missed, and annotations aren't inherited
        if not all(hasattr(x, name) or name in getattr(x, "__annotations__", {}) for name in protocol_attrs):
            return f"{x} does not implement {self.protocol.__name__}"

        if self.args_match:
            reasons = (
                (name, same_signature_p(method).explain_failure(getattr(x, name, None))["reason"])
                for name, method in getmembers(self.protocol, isfunction)
                if name in protocol_attrs
            )
            return next((f"Method '{name}': {reason}" for name, reason in reasons if reason), None)

        return None

    def __repr__(self) -> str:
        args_match = ", args_match=True" if self.args_match else ""
        return f"implements_protocol_p({self.protocol.__name__}{args_match})"

    @override
    def explain_failure(self, x: type) -> dict:
        return {"reason": self._failure(x)}


def implements_protocol_p(protocol: type, args_match: bool = False) -> Predicate:
    """Return True if value is Protocol, otherwise False."""
    return ImplementsProtocolPredicate(protocol=protocol, args_match=args_match)
