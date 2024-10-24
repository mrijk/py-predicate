from predicate.predicate import (
    AllPredicate,
    Predicate,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
)


def optimize_all_predicate[T](predicate: AllPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    if isinstance(optimized, AlwaysTruePredicate):
        return AlwaysTruePredicate()

    if isinstance(optimized, AlwaysFalsePredicate):
        return Predicate(predicate_fn=lambda l: len(l) == 0)

    return predicate
