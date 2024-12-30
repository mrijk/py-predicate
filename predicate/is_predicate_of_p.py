from dataclasses import dataclass
from typing import Any, TypeVar, override

from more_itertools import first

from predicate.predicate import Predicate


@dataclass
class IsPredicateOfPredicate[T](Predicate[T]):
    """A predicate class that models the 'isPredicateOf' predicate."""

    klass: type | tuple

    def __call__(self, x: Any) -> bool:
        match x:
            case Predicate() as predicate:
                annotations = predicate.__annotations__
                predicate_var = first(k for k, v in annotations.items() if type(v) is TypeVar)
                return type(getattr(predicate, predicate_var)) is self.klass
            case _:
                return False

    def __repr__(self) -> str:
        name = self.klass[0].__name__  # type: ignore
        return f"is_predicate_of_p({name!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not a predicate of type {self.klass!r}"}
