from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.is_empty_predicate import IsEmptyPredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.predicate import NotPredicate, Predicate


def optimize_all_predicate[T](predicate: AllPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return always_true_p
        case AlwaysFalsePredicate():
            return IsEmptyPredicate()
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=AnyPredicate(predicate=not_predicate))
        case IsNotNonePredicate():
            return NotPredicate(predicate=AnyPredicate(predicate=IsNonePredicate()))
        case _:
            pass

    return AllPredicate(predicate=optimized)
