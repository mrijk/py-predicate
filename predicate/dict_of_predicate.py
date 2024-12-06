from dataclasses import dataclass
from typing import Any

from predicate.predicate import Predicate


@dataclass
class DictOfPredicate[T](Predicate[T]):
    """A predicate class that models the dict_of predicate."""

    key_value_predicates: list[tuple[Predicate, Predicate]]

    def __call__(self, x: Any) -> bool:
        if not isinstance(x, dict):
            return False

        if not x and self.key_value_predicates:
            return False

        # For all values, a predicate must be True
        for key, value in x.items():
            if not any(key_p(key) and value_p(value) for key_p, value_p in self.key_value_predicates):
                return False

        # All predicates must be True
        for key_p, value_p in self.key_value_predicates:
            if any(key_p(key) and not value_p(value) for key, value in x.items()):
                return False

        return True

    def __repr__(self) -> str:
        # TODO
        return "is_dict_of_p"
