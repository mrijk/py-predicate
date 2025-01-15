from dataclasses import dataclass
from typing import Any, override

from predicate.predicate import Predicate


@dataclass
class IsPredicateOfPredicate[T](Predicate[T]):
    """A predicate class that models the 'isPredicateOf' predicate."""

    predicate_klass: type

    def __call__(self, x: Any) -> bool:
        match x:
            case Predicate() as predicate:
                return predicate.klass == self.predicate_klass or predicate.klass == Any
            case _:
                return False

    def __repr__(self) -> str:
        name = self.predicate_klass.__name__  # type: ignore
        return f"is_predicate_of_p({name!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        match x:
            case Predicate():
                return {"reason": f"{x} is not a predicate of type {self.predicate_klass.__name__!r}"}
            case _:
                return {"reason": f"Value `{x}` is not a predicate"}
