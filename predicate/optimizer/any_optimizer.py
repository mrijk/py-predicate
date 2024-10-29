from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AnyPredicate,
    EqPredicate,
    NePredicate,
    NotPredicate,
    Predicate,
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
            return NotPredicate(predicate=AllPredicate(predicate=optimize(not_predicate)))
        case _:
            pass

    return AnyPredicate(predicate=optimized)
