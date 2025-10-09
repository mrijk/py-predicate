from dataclasses import dataclass
from typing import override

from predicate.named_predicate import to_named_predicate
from predicate.predicate import Predicate
from predicate.truth_table import get_named_predicates, truth_table


@dataclass
class IsSamePredicate[T](Predicate[T]):
    """A predicate class that checks if two predicates are equivalent by comparing the truth tables."""

    predicate: Predicate[T]

    def __call__(self, predicate: Predicate) -> bool:
        return is_same(self.predicate, predicate)

    def __repr__(self) -> str:
        return "is_same_p"

    @override
    def explain_failure(self, predicate: Predicate[T]) -> dict:
        if get_named_predicates(self.predicate) != get_named_predicates(predicate):
            return {"reason": "Predicates are not equivalent."}

        return {"reason": "Predicates have different truth tables."}


def is_same(p1: Predicate, p2: Predicate) -> bool:
    named_p1 = to_named_predicate(p1)
    named_p2 = to_named_predicate(p2)

    if get_named_predicates(named_p1) != get_named_predicates(named_p2):
        return False

    table1 = truth_table(named_p1)
    table2 = truth_table(named_p2)

    return list(table1) == list(table2)


def is_same_p[T](predicate: Predicate[T]) -> IsSamePredicate[T]:
    """Return True if the predicate is the same, otherwise False."""
    return IsSamePredicate(predicate=predicate)
