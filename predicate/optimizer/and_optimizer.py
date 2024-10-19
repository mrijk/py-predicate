from predicate.predicate import (
    AlwaysTruePredicate,
    AndPredicate,
    Predicate,
    get_as_not_predicate,
    AlwaysFalsePredicate,
    get_as_or_predicate,
)


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize_predicate, optimize

    # p & True == p
    if isinstance(predicate.right, AlwaysTruePredicate):
        return optimize(predicate.left)

    # True & p == p
    if isinstance(predicate.left, AlwaysTruePredicate):
        return optimize(predicate.right)

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

    if or_predicate := get_as_or_predicate(predicate.right):
        # p & (~p | q) == p & q
        if not_predicate := get_as_not_predicate(or_predicate.left):
            if not_predicate.predicate == predicate.left:
                return AndPredicate(left=predicate.left, right=or_predicate.right)
        # p & (q | ~p) == p & q
        if not_predicate := get_as_not_predicate(or_predicate.right):
            if not_predicate.predicate == predicate.left:
                return AndPredicate(left=predicate.left, right=or_predicate.left)

    if or_predicate := get_as_or_predicate(predicate.left):
        # (~p | q) & p == q & p
        if not_predicate := get_as_not_predicate(or_predicate.left):
            if not_predicate.predicate == predicate.right:
                return AndPredicate(left=or_predicate.right, right=predicate.right)
        # (q | ~p) & p == q & p
        if not_predicate := get_as_not_predicate(or_predicate.right):
            if not_predicate.predicate == predicate.right:
                return AndPredicate(left=or_predicate.left, right=predicate.right)

    return optimize_predicate(predicate)
