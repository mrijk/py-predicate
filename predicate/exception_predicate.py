from dataclasses import dataclass
from typing import Final

from predicate.predicate import Predicate


class PredicateError(Exception):
    """Exception that will be thrown."""

    pass


@dataclass
class ExceptionPredicate[T](Predicate[T]):
    """A predicate class always throws an exception."""

    def __call__(self, _x: T) -> bool:
        raise PredicateError()

    def __repr__(self) -> str:
        return "exception_p"


exception_p: Final[ExceptionPredicate] = ExceptionPredicate()
"""Always throw an exception."""
