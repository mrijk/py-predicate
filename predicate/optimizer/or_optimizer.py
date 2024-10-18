from predicate.predicate import (
    OrPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    Predicate,
    get_as_not_predicate,
    get_as_and_predicate,
)


def optimize_or_predicate[T](predicate: OrPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize_predicate, optimize

    # p | False == p
    if isinstance(predicate.right, AlwaysFalsePredicate):
        return optimize(predicate.left)

    # False | p == p
    if isinstance(predicate.left, AlwaysFalsePredicate):
        return optimize(predicate.right)

    # p | p == p
    if predicate.left == predicate.right:
        return optimize(predicate.left)

    # ~p | p == True
    if not_predicate := get_as_not_predicate(predicate.left):
        if predicate.right == not_predicate.predicate:
            return AlwaysTruePredicate()

    # p | ~p == True
    if not_predicate := get_as_not_predicate(predicate.right):
        if predicate.left == not_predicate.predicate:
            return AlwaysTruePredicate()

    # p | (~p & q) == p | q
    if and_predicate := get_as_and_predicate(predicate.right):
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if not_predicate.predicate == predicate.left:
                return OrPredicate(left=predicate.left, right=and_predicate.right)

    return optimize_predicate(predicate)
