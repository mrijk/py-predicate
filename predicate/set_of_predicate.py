from dataclasses import dataclass
from typing import override

from predicate.helpers import all_true, first_false
from predicate.predicate import Predicate


@dataclass
class SetOfPredicate[T](Predicate[T]):
    """A predicate class that models the set_of predicate."""

    predicate: Predicate

    def __call__(self, x: set[T]) -> bool:
        match x:
            case set() as s:
                return all_true(s, self.predicate)
            case _:
                return False

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.predicate

    def __repr__(self) -> str:
        return f"is_set_of_p({self.predicate})"

    def get_klass(self) -> type:
        return self.predicate.klass

    @override
    def explain_failure(self, x: set[T]) -> dict:
        match x:
            case set() as s:
                fail = first_false(s, self.predicate)
                return {"reason": f"Item '{fail}' didn't match predicate {self.predicate}"}
            case _:
                return {"reason": f"{x} is not an instance of a set"}
