from predicate.predicate import (
    NotPredicate,
    Predicate,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
    AllPredicate,
    AnyPredicate,
    NePredicate,
    EqPredicate,
)


def optimize_any_predicate[T](predicate: AnyPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            return AlwaysTruePredicate()
        case AlwaysFalsePredicate():
            return AlwaysFalsePredicate()
        case NePredicate(v):
            return NotPredicate(predicate=AllPredicate(predicate=EqPredicate(v)))
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=AllPredicate(predicate=not_predicate))
        case _:
            pass

    return predicate
