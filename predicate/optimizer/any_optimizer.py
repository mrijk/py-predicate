from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import NotPredicate, Predicate


def optimize_any_predicate[T](predicate: AnyPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return always_true_p
        case AlwaysFalsePredicate():
            return always_false_p
        case NePredicate(v):
            return NotPredicate(predicate=AllPredicate(predicate=EqPredicate(v)))
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=AllPredicate(predicate=optimize(not_predicate)))
        case _:
            pass

    return AnyPredicate(predicate=optimized)
