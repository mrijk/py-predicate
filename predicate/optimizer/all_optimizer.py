from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AnyPredicate,
    IsEmptyPredicate,
    NotPredicate,
    Predicate,
)


def optimize_all_predicate[T](predicate: AllPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    match predicate.predicate:
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=AnyPredicate(predicate=not_predicate))

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return AlwaysTruePredicate()
        case AlwaysFalsePredicate():
            return IsEmptyPredicate()
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=AnyPredicate(predicate=not_predicate))
        case _:
            pass

    return predicate
