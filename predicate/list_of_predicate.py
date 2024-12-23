from dataclasses import dataclass
from typing import Any, override

from predicate.helpers import first_false
from predicate.predicate import Predicate, resolve_predicate


@dataclass
class ListOfPredicate[T](Predicate[T]):
    """A predicate class that models the list_of predicate."""

    predicate: Predicate[T]

    def __init__(self, predicate: Predicate[T]):
        self.predicate = resolve_predicate(predicate)

    def __call__(self, x: Any) -> bool:
        match x:
            case list() as l:
                return all(self.predicate(item) for item in l)
            case _:
                return False

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.predicate

    def __repr__(self) -> str:
        return f"is_list_of_p({self.predicate})"

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case list() as l:
                fail = first_false(l, self.predicate)
                return {"reason": f"Item '{fail}' didn't match predicate {self.predicate}"}
            case _:
                return {"reason": f"{x} is not an instance of a list"}
