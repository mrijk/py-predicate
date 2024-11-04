from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AnyPredicate,
    IsEmptyPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    NotPredicate,
    Predicate,
)


def optimize_all_predicate[T](predicate: AllPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return AlwaysTruePredicate()
        case AlwaysFalsePredicate():
            return IsEmptyPredicate()
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=AnyPredicate(predicate=not_predicate))
        case IsNotNonePredicate():
            return NotPredicate(predicate=AnyPredicate(predicate=IsNonePredicate()))
        case _:
            pass

    return AllPredicate(predicate=optimized)
