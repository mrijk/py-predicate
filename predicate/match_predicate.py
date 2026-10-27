from dataclasses import dataclass
from itertools import islice, tee
from typing import Iterable, override

from predicate.consumes import consumes
from predicate.exactly_predicate import ExactlyPredicate
from predicate.optional_predicate import OptionalPredicate
from predicate.plus_predicate import PlusPredicate
from predicate.predicate import Predicate
from predicate.repeat_predicate import RepeatPredicate
from predicate.star_predicate import StarPredicate


@dataclass
class MatchPredicate[T](Predicate[T]):
    """A predicate class that models 'match iterable' predicate."""

    predicates: list[Predicate]
    full_match: bool = False

    def __call__(self, iterable: Iterable[T]) -> bool:
        return match(iterable, predicates=self.predicates, full_match=self.full_match)

    def __repr__(self) -> str:
        param = ", ".join(repr(predicate) for predicate in self.predicates)
        return f"match_p({param})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": reason(iterable, predicates=self.predicates, full_match=self.full_match)}


def match_p[T](*predicates: Predicate, full_match: bool = False) -> MatchPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return MatchPredicate(predicates=list(predicates), full_match=full_match)


def reason(iterable: Iterable, *, predicates: list[Predicate], full_match: bool) -> dict:
    if not predicates:
        return {"reason": "Iterable has more items than predicates to match", "result": False}
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            return predicate.explain(iterable, predicates=rest_predicates, full_match=full_match)
        case Predicate():
            if not (items := list(iterable)):
                return {"reason": f"Iterable has no item left to match against {predicate!r}", "result": False}
            item, *rest = items
            if not predicate(item):
                return predicate.explain(item)
            return reason(rest, predicates=rest_predicates, full_match=full_match)
        case _:
            raise NotImplementedError


def match(iterable: Iterable, *, predicates: list[Predicate], full_match: bool) -> bool:
    if not predicates:
        # Nothing left to match: a partial match succeeds, a full match only if the iterable is exhausted
        return not full_match or not list(iterable)
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            return predicate(iterable, predicates=rest_predicates, full_match=full_match)
        case Predicate():
            consumed = list(consumes(predicate, iterable))

            end = consumed[-1]

            if end >= 1 and rest_predicates:
                it1, it2 = tee(iterable)
                rest = list(islice(it2, end, None))
                return match(rest, predicates=rest_predicates, full_match=full_match)
            if end >= 1:
                if full_match:
                    it1, it2 = tee(iterable)
                    rest = list(islice(it2, end, None))
                    return not rest
                return True
            return False
        case _:
            raise NotImplementedError
