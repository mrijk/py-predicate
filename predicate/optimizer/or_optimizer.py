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

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    # p | False == p
    if isinstance(right, AlwaysFalsePredicate):
        return left

    # False | p == p
    if isinstance(left, AlwaysFalsePredicate):
        return right

    # p | True == True
    if isinstance(right, AlwaysTruePredicate):
        return AlwaysTruePredicate()

    # True | p == p
    if isinstance(left, AlwaysTruePredicate):
        return AlwaysTruePredicate()

    # p | p == p
    if left == right:
        return left

    # ~p | p == True
    if not_predicate := get_as_not_predicate(left):
        if right == not_predicate.predicate:
            return AlwaysTruePredicate()

    # p | ~p == True
    if not_predicate := get_as_not_predicate(right):
        if left == not_predicate.predicate:
            return AlwaysTruePredicate()

    # p | (~p & q) == p | q
    if and_predicate := get_as_and_predicate(right):
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if not_predicate.predicate == left:
                return OrPredicate(left=left, right=and_predicate.right)

    return optimize_predicate(predicate)
