from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.has_length_predicate import is_not_empty_p
from predicate.not_predicate import NotPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized


def optimize_any_predicate[T](predicate: AnyPredicate[T]) -> MaybeOptimized[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return Optimized(is_not_empty_p)  # any_p(always_true_p) is False for an empty iterable (#369)
        case AlwaysFalsePredicate():
            return Optimized(always_false_p)
        case NotPredicate(not_predicate):
            return Optimized(NotPredicate(predicate=AllPredicate(predicate=optimize(not_predicate))))
        case _:
            pass

    return Optimized(AnyPredicate(predicate=optimized)) if optimized != predicate.predicate else NotOptimized()
