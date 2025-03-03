from more_itertools import one

from predicate.always_false_predicate import always_false_p
from predicate.always_true_predicate import always_true_p
from predicate.eq_predicate import EqPredicate
from predicate.ne_predicate import NePredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.set_predicates import InPredicate, NotInPredicate


def optimize_in_predicate[T](predicate: InPredicate[T]) -> MaybeOptimized[T]:
    match len(v := predicate.v):
        case 0:
            return Optimized(always_false_p)
        case 1:
            return Optimized(EqPredicate(one(v)))
        case _:
            return NotOptimized()


def optimize_not_in_predicate[T](predicate: NotInPredicate[T]) -> MaybeOptimized[T]:
    match len(v := predicate.v):
        case 0:
            return Optimized(always_true_p)
        case 1:
            return Optimized(NePredicate(one(v)))
        case _:
            return NotOptimized()
