from predicate.predicate import (
    AndPredicate,
    Predicate,
    get_as_not_predicate,
    AlwaysFalsePredicate,
)


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize_predicate, optimize

    # p & p == p
    if predicate.left == predicate.right:
        return optimize(predicate.left)

    # ~p & p == False
    if not_predicate := get_as_not_predicate(predicate.left):
        if predicate.right == not_predicate.predicate:
            return AlwaysFalsePredicate()

    # p & ~p == False
    if not_predicate := get_as_not_predicate(predicate.right):
        if predicate.left == not_predicate.predicate:
            return AlwaysFalsePredicate()

    return optimize_predicate(predicate)
