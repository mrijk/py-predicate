from dataclasses import dataclass
from inspect import getmembers, isfunction, signature
from typing import Any, Protocol

from predicate.predicate import Predicate


def _signatures_match(protocol_method: Any, impl_method: Any, strict: bool = False) -> bool:
    """Compare method signatures.

    strict=False allows covariance (impl can be more permissive).
    strict=True requires exact signature match.
    """
    proto_sig = signature(protocol_method)
    impl_sig = signature(impl_method)

    # Compare parameter counts and names
    proto_params = list(proto_sig.parameters.values())[1:]  # skip self
    impl_params = list(impl_sig.parameters.values())[1:]

    if len(proto_params) != len(impl_params):
        return False

    for proto_p, impl_p in zip(proto_params, impl_params, strict=False):
        if proto_p.name != impl_p.name:
            return False
        if strict and proto_p.annotation != impl_p.annotation:
            return False

    # Compare return types if strict
    if strict:
        return proto_sig.return_annotation == impl_sig.return_annotation
    return True


@dataclass
class ImplementsProtocolPredicate[T](Predicate[T]):
    """A predicate class that models the 'implements a protocol' predicate."""

    protocol: type[Protocol]
    args_match: bool

    def __call__(self, x: type) -> bool:
        if not isinstance(x(), self.protocol):
            return False

        if self.args_match:
            # Check signatures of all protocol methods
            for name, method in getmembers(self.protocol, predicate=isfunction):
                if not hasattr(x, name):
                    return False
                if not _signatures_match(method, getattr(x, name), strict=True):
                    return False

        return True


def implements_protocol_p(protocol: type[Protocol], args_match: bool = False) -> Predicate:
    """Return True if value is Protocol, otherwise False."""
    return ImplementsProtocolPredicate(protocol=protocol, args_match=args_match)
