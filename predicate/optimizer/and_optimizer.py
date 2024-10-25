from predicate.predicate import (
    AllPredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    Predicate,
    get_as_not_predicate,
    AlwaysFalsePredicate,
    get_as_or_predicate,
    GePredicate,
)


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

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

    match left, right:
        case EqPredicate(v1), EqPredicate(v2) if v1 == v2:
            # x = v1 & x = v2 & v1 == v2 => x = v1
            return left
        case EqPredicate(v1), EqPredicate(v2) if v1 != v2:
            # x = v1 & x = v2 & v1 != v2 => False
            return AlwaysFalsePredicate()
        case EqPredicate(v1), GePredicate(v2) if v1 == v2:
            # x = v1 & x >= v2 & v1 = v2 => x = v1
            return left
        case EqPredicate(v1), GePredicate(v2) if v1 < v2:
            # x = v1 & x >= v2 & v1 < v2 => False
            return AlwaysFalsePredicate()
        case GePredicate(v1), GePredicate(v2):
            # x >= v1 & x >= v2 => x >= max(v1, v2)
            return GePredicate(v=max(v1, v2))
        case AllPredicate(left_all), AllPredicate(right_all):
            # All(p1) & All(p2) => All(p1 & p2)
            return optimize(AllPredicate(predicate=optimize(AndPredicate(left=left_all, right=right_all))))
        case _, _:
            # TODO: complete all cases
            pass

    return predicate
