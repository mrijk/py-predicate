from dataclasses import dataclass
from datetime import datetime
from typing import Annotated, Any, Final, override
from uuid import UUID

from predicate.in_predicate import in_p
from predicate.predicate import Explanation, Predicate

# The classes random predicates can be generated for, see random_predicates
_generatable_klass_p: Final = in_p((bool, datetime, float, int, str, UUID, Any))


@dataclass
class IsPredicateOfPredicate[T](Predicate[T]):
    """A predicate class that models the 'isPredicateOf' predicate."""

    predicate_klass: Annotated[type, _generatable_klass_p]

    def __call__(self, x: Any) -> bool:
        match x:
            case Predicate() as predicate:
                return self.predicate_klass is Any or predicate.klass in (self.predicate_klass, Any)
            case _:
                return False

    def __repr__(self) -> str:
        name = self.predicate_klass.__name__
        return f"is_predicate_of_p({name!r})"

    @override
    def explain_failure(self, x: T) -> Explanation:
        match x:
            case Predicate():
                return {"reason": f"{x} is not a predicate of type {self.predicate_klass.__name__!r}"}
            case _:
                return {"reason": f"Value `{x}` is not a predicate"}


def is_predicate_of_p(klass: type) -> Predicate[Any]:
    return IsPredicateOfPredicate(predicate_klass=klass)
