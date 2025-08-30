from typing import Iterable, Sized

from more_itertools import one

from predicate.always_true_predicate import always_true_p
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized


def optimize_not_in_predicate[T](predicate: NotInPredicate[T]) -> MaybeOptimized[T]:
    if isinstance(predicate.v, Sized):
        match len(v := predicate.v):
            case 0:
                return Optimized(always_true_p)
            case 1 if isinstance(v, Iterable):
                return Optimized(NePredicate(one(v)))
    return NotOptimized()
