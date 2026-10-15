from collections.abc import Iterator, Mapping, Sequence
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
        if not isinstance(x, Mapping):
            return False

        return bool(x) and not any(self._failing(x)) and not any(self._unmatched(x))

    def _failing(self, x: Mapping) -> Iterator[tuple[Any, Any, Predicate]]:
        return (
            (key, value, value_p)
            for key_p, value_p in self.key_value_predicates
            for key, value in x.items()
            if key_p(key) and not value_p(value)
        )

    def _unmatched(self, x: Mapping) -> Iterator[tuple[Any, Any]]:
        return (
            (key, value) for key, value in x.items() if not any(key_p(key) for key_p, _ in self.key_value_predicates)
        )

    def __repr__(self) -> str:
        pairs = [(from_key_p(key_p), value_p) for key_p, value_p in self.key_value_predicates]
        return f"is_dict_of_p({key_value_pairs_repr(pairs)})"

    @override
    def explain_failure(self, x: Any, *args, **kwargs) -> dict:
        if not isinstance(x, Mapping):
            return {"reason": f"{x} is not an instance of a Mapping"}
        if not x:
            return {"reason": "empty dict"}
        if failing := first(self._failing(x), None):
            key, value, value_p = failing
            return {"key": key, "value": value} | value_p.explain_failure(value)
        if unmatched := first(self._unmatched(x), None):
            key, value = unmatched
            return {"key": key, "value": value, "reason": "no matching predicate for key"}
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
