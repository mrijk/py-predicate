from collections.abc import Mapping
from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class HasKeyPredicate[T](Predicate[T]):
    """A predicate class that models the has key."""

    key_p: Predicate[T]

    def __call__(self, v: Mapping) -> bool:
        return any(self.key_p(k) for k in v.keys())

    def __repr__(self) -> str:
        return f"has_key_p({self.key_p!r})"

    @override
    def explain_failure(self, v: Mapping) -> dict:
        return {"reason": f"No key satisfying {self.key_p!r} found in {v}"}


def has_key_p[T](key_p: Predicate[T]) -> HasKeyPredicate:
    """Return True if dict contains a key satisfying key_p, otherwise False."""
    return HasKeyPredicate(key_p=key_p)
