from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class HasKeyPredicate[T](Predicate[T]):
    """A predicate class that models the has key."""

    key: T

    def __call__(self, v: dict) -> bool:
        return self.key in v.keys()

    def __repr__(self) -> str:
        return f'has_key_p("{self.key}")'

    @override
    def explain_failure(self, v: dict) -> dict:
        return {"reason": f"Key '{self.key}' is missing in {v}"}
