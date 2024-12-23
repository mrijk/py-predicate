from dataclasses import dataclass
from typing import override

from predicate.helpers import all_true, first_false
from predicate.predicate import Predicate


@dataclass
class SetOfPredicate[T](Predicate[T]):
    """A predicate class that models the set_of predicate."""

    predicate: Predicate

    def __call__(self, x: set[T]) -> bool:
        return all_true(x, self.predicate)

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.predicate

    def __repr__(self) -> str:
        return f"is_set_of_p({self.predicate})"

    @override
    def explain_failure(self, x: set[T]) -> dict:
        fail = first_false(x, self.predicate)

        return {"reason": f"Item '{fail}' didn't match predicate {self.predicate}"}
