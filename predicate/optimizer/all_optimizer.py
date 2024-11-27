from predicate.all_predicate import AllPredicate
from predicate.any_predicate import AnyPredicate
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    IsEmptyPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    NotPredicate,
    Predicate,
    always_true_p,
)


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
