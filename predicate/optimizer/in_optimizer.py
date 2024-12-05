from more_itertools import one

from predicate.predicate import EqPredicate, NePredicate, Predicate, always_false_p, always_true_p
from predicate.set_predicates import InPredicate, NotInPredicate


def optimize_in_predicate[T](predicate: InPredicate[T]) -> Predicate[T]:
    match len(v := predicate.v):
        case 0:
            return always_false_p
        case 1:
            return EqPredicate(one(v))
        case _:
            return predicate


def optimize_not_in_predicate[T](predicate: NotInPredicate[T]) -> Predicate[T]:
    match len(v := predicate.v):
        case 0:
            return always_true_p
        case 1:
            return NePredicate(one(v))
        case _:
            return predicate
