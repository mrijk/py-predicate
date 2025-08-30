from typing import Iterable, Sized

from more_itertools import one

from predicate.always_false_predicate import always_false_p
from predicate.eq_predicate import EqPredicate
from predicate.in_predicate import InPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized


def optimize_in_predicate[T](predicate: InPredicate[T]) -> MaybeOptimized[T]:
    if isinstance(predicate.v, Sized):
        match len(v := predicate.v):
            case 0:
                return Optimized(always_false_p)
            case 1 if isinstance(v, Iterable):
                return Optimized(EqPredicate(one(v)))
    return NotOptimized()
