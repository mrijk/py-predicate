from dataclasses import dataclass
from typing import override

from predicate.implies import implies
from predicate.predicate import Predicate


@dataclass
class ImpliesPredicate[T](Predicate[T]):
    """A predicate class that models the 'implies' (=>) predicate."""

    predicate: Predicate

    def __call__(self, predicate: Predicate) -> bool:
        return implies(predicate, self.predicate)

    def __repr__(self) -> str:
        return f"implies_p({self.predicate})"

    @override
    def explain_failure(self, predicate: Predicate) -> dict:
        return {"reason": f"{predicate} doesn't imply {self.predicate}"}


def implies_p(predicate: Predicate) -> ImpliesPredicate:
    return ImpliesPredicate(predicate)
