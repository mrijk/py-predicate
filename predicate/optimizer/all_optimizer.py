from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AnyPredicate,
    IsEmptyPredicate,
    NotPredicate,
    Predicate,
    get_as_not_predicate,
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
        case _:
            pass

    if not_predicate := get_as_not_predicate(predicate.predicate):
        return NotPredicate(predicate=AnyPredicate(predicate=not_predicate.predicate))

    return predicate
