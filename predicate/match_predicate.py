from dataclasses import dataclass
from typing import Iterable, get_args, get_origin, override

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

    def __call__(self, iterable: Iterable[T]) -> bool:
        return match(iterable, predicates=self.predicates)

    def __repr__(self) -> str:
        param = ", ".join(repr(predicate) for predicate in self.predicates)
        return f"match_p({param})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": reason(iterable, predicates=self.predicates)}


def match_p[T](*predicates: Predicate) -> MatchPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return MatchPredicate(predicates=list(predicates))


def reason(iterable: Iterable, *, predicates: list[Predicate]) -> dict:
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            return predicate.explain(iterable, predicates=rest_predicates)
        case Predicate():
            item, *rest = iterable
            if not predicate(item):
                return predicate.explain(item)
            return reason(rest, predicates=rest_predicates)
        case _:
            raise NotImplementedError


def is_predicate_of_iterable(cls):
    """Return True if cls inherits from Predicate[Iterable[...]]."""
    from collections.abc import Iterable as AbcIterable

    if not hasattr(cls, "__orig_bases__"):
        return False

    for base in cls.__orig_bases__:
        origin = get_origin(base)
        args = get_args(base)
        if origin is Predicate and args:
            arg_origin = get_origin(args[0])
            if arg_origin is AbcIterable:
                return True
    return False


def match(iterable: Iterable, *, predicates: list[Predicate]) -> bool:
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            return predicate(iterable, predicates=rest_predicates)
        case Predicate() if is_predicate_of_iterable(predicate.__class__):
            raise NotImplementedError("No support for predicates on iterables yet!")
        case Predicate():
            if not iterable:
                return False
            item, *rest = iterable
            if rest_predicates:
                return predicate(item) and match(rest, predicates=rest_predicates)
            return predicate(item)
        case _:
            raise NotImplementedError
