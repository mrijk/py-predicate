from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import NotPredicate
from predicate.standard_predicates import is_empty_p


def optimize_all_predicate[T](predicate: AllPredicate[T]) -> MaybeOptimized[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return Optimized(always_true_p)
        case AlwaysFalsePredicate():
            return Optimized(is_empty_p)
        case NotPredicate(not_predicate):
            return Optimized(NotPredicate(predicate=AnyPredicate(predicate=not_predicate)))
        case IsNotNonePredicate():
            return Optimized(NotPredicate(predicate=AnyPredicate(predicate=IsNonePredicate())))
        case _:
            pass

    return NotOptimized() if optimized == predicate.predicate else Optimized(AllPredicate(predicate=optimized))
