from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, override

from more_itertools import first

from predicate.eq_predicate import EqPredicate
from predicate.helpers import key_value_pairs_repr
from predicate.predicate import Predicate


@dataclass
class DictOfPredicate(Predicate):
    """A predicate class that models the dict_of predicate."""

    key_value_predicates: list[tuple[Predicate, Predicate]]

    def __init__(self, key_value_predicates: Sequence[tuple[Predicate | str, Predicate]]):
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
        pairs = [(from_key_p(key_p), value_p) for key_p, value_p in self.key_value_predicates]
        return f"is_dict_of_p({key_value_pairs_repr(pairs)})"

    @override
    def explain_failure(self, x: Any, *args, **kwargs) -> dict:
        if not isinstance(x, dict):
            return {"reason": f"{x} is not an instance of a dict"}
        if not x:
            return {"reason": "empty dict"}
        if failing := first(
            (
                ({"key": key, "value": value} | value_p.explain_failure(value))
                for key_p, value_p in self.key_value_predicates
                for key, value in x.items()
                if key_p(key) and not value_p(value)
            ),
            None,
        ):
            return failing
        if unmatched := first(
            (
                {"key": key, "value": value, "reason": "no matching predicate for key"}
                for key, value in x.items()
                if not any(key_p(key) for key_p, _ in self.key_value_predicates)
            ),
            None,
        ):
            return unmatched
        return {}


def to_key_p(key_p: Predicate | str) -> Predicate:
    from predicate import eq_p

    match key_p:
        case str(s):
            return eq_p(s)
        case _:
            return key_p


def from_key_p(key_p: Predicate) -> Predicate | str:
    match key_p:
        case EqPredicate(v):
            return v
        case _:
            return key_p


def is_dict_of_p(*predicates: tuple[Predicate | str, Predicate]) -> Predicate:
    """Return True if value is a set, and for all elements in the set the predicate is True, otherwise False."""
    # return is_set_p & all_p(predicate)
    return DictOfPredicate(list(predicates))
