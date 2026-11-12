from dataclasses import dataclass
from typing import Any, override

from predicate.implies import implies
from predicate.predicate import Predicate


@dataclass
class ImpliesPredicate[T](Predicate[T]):
    """A predicate class that models the 'implies' (=>) predicate."""

    predicate: Predicate[Any]

    def __call__(self, predicate: Predicate[Any]) -> bool:
        return implies(predicate, self.predicate)

    def __repr__(self) -> str:
        return f"implies_p({self.predicate})"

    @override
    def explain_failure(self, predicate: Predicate[Any]) -> dict[str, Any]:
        return {"reason": f"{predicate} doesn't imply {self.predicate}"}


def implies_p(predicate: Predicate[Any]) -> ImpliesPredicate[Any]:
    return ImpliesPredicate(predicate)
