from predicate.always_false_predicate import always_false_p
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.set_predicates import IntersectsPredicate


def optimize_intersects_predicate[T](predicate: IntersectsPredicate[T]) -> MaybeOptimized[T]:
    if not predicate.v:
        return Optimized(always_false_p)
    return NotOptimized()
