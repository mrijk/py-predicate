from dataclasses import dataclass
from typing import Callable, Iterable, override

from predicate.predicate import Predicate


@dataclass
class MatchPredicate[T](Predicate[T]):
    """A predicate class that models 'match iterable' predicate."""

    predicates: list[Predicate]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return match(self.predicates, iterable)

    def __repr__(self) -> str:
        return "match_p(TBD)"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": "Tbd"}


def match_p[T](*predicates: Predicate) -> MatchPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return MatchPredicate(predicates=list(predicates))


def match(predicates: list[Predicate], iterable: Iterable) -> bool:
    predicate, *rest_predicates = predicates
    match predicate:
        case Predicate():
            item, *rest = iterable
            if rest_predicates:
                return predicate(item) and match(rest_predicates, rest)
            return predicate(item)
        case _:
            return predicate(rest_predicates, iterable)


def repeat(m: int, n: int, predicate: Predicate) -> Callable:
    """Match exactly m to n instances of the given predicate."""

    def _repeat(predicates: list[Predicate], iterable: Iterable) -> bool:
        for n_ in range(n, m - 1, -1):
            f = exactly_n(n_, predicate)
            if f(predicates, iterable):
                return True
        return False

    return _repeat


def exactly_n(n: int, predicate: Predicate) -> Callable:
    """Match exactly n instances of the given predicate."""

    def _exactly_n(predicates: list[Predicate], iterable: Iterable) -> bool:
        rest = iterable
        for _ in range(n):
            if not rest:
                return False

            item, *rest = rest
            if not predicate(item):
                return False
        return match(predicates, rest) if predicates else True

    return _exactly_n


def optional(predicate: Predicate) -> Callable:
    """Match 0 or 1 instances of the given predicate."""

    def _optional(predicates: list[Predicate], iterable: Iterable) -> bool:
        if not iterable:
            return True
        item, *rest = iterable
        return (predicate(item) and match(predicates, rest)) or match(predicates, iterable)

    return _optional
