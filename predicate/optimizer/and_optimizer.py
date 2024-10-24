from predicate.predicate import (
    AlwaysTruePredicate,
    AndPredicate,
    Predicate,
    get_as_not_predicate,
    AlwaysFalsePredicate,
    get_as_or_predicate,
    get_as_eq_predicate,
)


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize_predicate, optimize

    left = predicate.left
    right = predicate.right

    # p & False = False
    if isinstance(right, AlwaysFalsePredicate):
        return AlwaysFalsePredicate()

    # False & p = False
    if isinstance(left, AlwaysFalsePredicate):
        return AlwaysFalsePredicate()

    # p & True == p
    if isinstance(right, AlwaysTruePredicate):
        return optimize(left)

    # True & p == p
    if isinstance(left, AlwaysTruePredicate):
        return optimize(right)

    # p & p == p
    if left == right:
        return optimize(left)

    # ~p & p == False
    if not_predicate := get_as_not_predicate(left):
        if right == not_predicate.predicate:
            return AlwaysFalsePredicate()

    # p & ~p == False
    if not_predicate := get_as_not_predicate(right):
        if left == not_predicate.predicate:
            return AlwaysFalsePredicate()

    if or_predicate := get_as_or_predicate(right):
        # p & (~p | q) == p & q
        if not_predicate := get_as_not_predicate(or_predicate.left):
            if not_predicate.predicate == left:
                return AndPredicate(left=left, right=or_predicate.right)
        # p & (q | ~p) == p & q
        if not_predicate := get_as_not_predicate(or_predicate.right):
            if not_predicate.predicate == left:
                return AndPredicate(left=left, right=or_predicate.left)

    if or_predicate := get_as_or_predicate(left):
        # (~p | q) & p == q & p
        if not_predicate := get_as_not_predicate(or_predicate.left):
            if not_predicate.predicate == right:
                return AndPredicate(left=or_predicate.right, right=right)
        # (q | ~p) & p == q & p
        if not_predicate := get_as_not_predicate(or_predicate.right):
            if not_predicate.predicate == right:
                return AndPredicate(left=or_predicate.left, right=right)

    # x == v1 & x == v2 & v1 != v2 == False

    if (left_eq := get_as_eq_predicate(left)) and (
        right_eq := get_as_eq_predicate(right)
    ):
        if left_eq != right_eq:
            return AlwaysFalsePredicate()

    return optimize_predicate(predicate)
