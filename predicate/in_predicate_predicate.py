from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class InPredicatePredicate[T](Predicate[T]):
    """A predicate class that models the 'in predicate tree'  predicate."""

    predicate: Predicate

    def __call__(self, predicate: Predicate) -> bool:
        return predicate in self.predicate

    def __repr__(self) -> str:
        return f"in_predicate_p({self.predicate})"

    @override
    def explain_failure(self, predicate: Predicate) -> dict:
        return {"reason": f"{predicate} is not part of predicate {self.predicate}"}


def in_predicate_p(predicate: Predicate) -> InPredicatePredicate:
    return InPredicatePredicate(predicate)
