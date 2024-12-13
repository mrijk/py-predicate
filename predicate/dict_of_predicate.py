from dataclasses import dataclass
from typing import Any, override

from predicate.predicate import Predicate


@dataclass
class DictOfPredicate[T](Predicate[T]):
    """A predicate class that models the dict_of predicate."""

    key_value_predicates: list[tuple[Predicate, Predicate]]

    def __init__(self, key_value_predicates: list[tuple[Predicate | str, Predicate]]):
        def to_key_p(key_p: Predicate | str) -> Predicate:
            from predicate.standard_predicates import eq_p

            match key_p:
                case str(s):
                    return eq_p(s)
                case _:
                    return key_p

        self.key_value_predicates = [(to_key_p(key_p), value_p) for key_p, value_p in key_value_predicates]

    def __call__(self, x: Any) -> bool:
        if not isinstance(x, dict):
            return False

        if not x:
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
        # TODO: show predicates
        return "is_dict_of_p"

    @override
    def explain_failure(self, x: Any) -> dict:
        # TODO: finish
        return {"result": False, "key_value_predicates": []}
