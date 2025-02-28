from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ne_predicate import NePredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import NotPredicate


def optimize_any_predicate[T](predicate: AnyPredicate[T]) -> MaybeOptimized[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return Optimized(always_true_p)
        case AlwaysFalsePredicate():
            return Optimized(always_false_p)
        case NePredicate(v):
            return Optimized(NotPredicate(predicate=AllPredicate(predicate=EqPredicate(v))))
        case NotPredicate(not_predicate):
            return Optimized(NotPredicate(predicate=AllPredicate(predicate=optimize(not_predicate))))
        case _:
            pass

    return Optimized(AnyPredicate(predicate=optimized)) if optimized != predicate.predicate else NotOptimized()
