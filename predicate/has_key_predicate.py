from dataclasses import dataclass
from typing import Any

from predicate.predicate import Predicate


@dataclass
class HasKeyPredicate[T](Predicate[dict[T, Any]]):
    """A predicate class that models the has key."""

    key: T

    def __call__(self, v: dict) -> bool:
        return self.key in v.keys()

    def __repr__(self) -> str:
        return f'has_key_p("{self.key}")'
