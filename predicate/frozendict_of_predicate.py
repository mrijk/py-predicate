from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, override

from predicate.dict_of_predicate import DictOfPredicate, from_key_p, to_key_p
from predicate.helpers import key_value_pairs_repr
from predicate.is_instance_predicate import is_frozendict_p
from predicate.predicate import Predicate


@dataclass
class FrozenDictOfPredicate(Predicate):
    """A predicate class that models the frozendict_of predicate."""

    key_value_predicates: list[tuple[Predicate, Predicate]]

    def __init__(self, key_value_predicates: Sequence[tuple[Predicate | str, Predicate]]):
        self.key_value_predicates = [(to_key_p(key_p), value_p) for key_p, value_p in key_value_predicates]

    @property
    def dict_of_predicate(self) -> DictOfPredicate:
        return DictOfPredicate(self.key_value_predicates)

    def __call__(self, x: Any) -> bool:
        return is_frozendict_p(x) and self.dict_of_predicate(x)

    def __repr__(self) -> str:
        pairs = [(from_key_p(key_p), value_p) for key_p, value_p in self.key_value_predicates]
        return f"is_frozendict_of_p({key_value_pairs_repr(pairs)})"

    @override
    def explain_failure(self, x: Any, *args, **kwargs) -> dict:
        if not is_frozendict_p(x):
            return {"reason": f"{x} is not an instance of a frozendict"}
        return self.dict_of_predicate.explain_failure(x)


def is_frozendict_of_p(*predicates: tuple[Predicate | str, Predicate]) -> Predicate:
    """Return True if value is a frozendict, and all keys and values match the predicates, otherwise False."""
    return FrozenDictOfPredicate(list(predicates))
