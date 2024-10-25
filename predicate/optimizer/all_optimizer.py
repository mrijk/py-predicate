from predicate.predicate import (
    AllPredicate,
    FnPredicate,
    NotPredicate,
    Predicate,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
    get_as_not_predicate,
    AnyPredicate,
)


def optimize_all_predicate[T](predicate: AllPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    if isinstance(optimized, AlwaysTruePredicate):
        return AlwaysTruePredicate()

    if isinstance(optimized, AlwaysFalsePredicate):
        return FnPredicate(predicate_fn=lambda l: len(l) == 0)

    # not all => any

    if not_predicate := get_as_not_predicate(predicate.predicate):
        return NotPredicate(predicate=AnyPredicate(predicate=not_predicate.predicate))

    return predicate
