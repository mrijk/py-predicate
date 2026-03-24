from dataclasses import dataclass
from typing import Iterable

from predicate.helpers import predicates_repr
from predicate.predicate import Predicate


@dataclass
class JuxtPredicate[T](Predicate[T]):
    """A predicate class that models the juxtaposition predicate."""

    predicates: list[Predicate[T]]
    evaluate: Predicate[Iterable[bool]]

    def __call__(self, x: T) -> bool:
        result = (predicate(x) for predicate in self.predicates)
        return self.evaluate(result)

    def __repr__(self) -> str:
        return f"juxt_p({predicates_repr(self.predicates)})"


def juxt_p(*predicates: Predicate, evaluate: Predicate[Iterable[bool]]) -> Predicate:
    """Apply each predicate to the same value, then evaluate the boolean results with the evaluate predicate."""
    return JuxtPredicate(predicates=list(predicates), evaluate=evaluate)
