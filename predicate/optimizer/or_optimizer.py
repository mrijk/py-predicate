from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AnyPredicate,
    GePredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    get_as_and_predicate,
    get_as_not_predicate,
)


def optimize_or_predicate[T](predicate: OrPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    # before optimization

    if optimized := optimize_or_not(left=predicate.left, right=predicate.right):
        return optimized

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    # p | p == p
    if left == right:
        return left

    if optimized := optimize_or_not(left=left, right=right):
        return optimized

    # p | (~p & q) == p | q
    if and_predicate := get_as_and_predicate(right):
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if not_predicate.predicate == left:
                return OrPredicate(left=left, right=and_predicate.right)

    match left, right:
        case _, AlwaysFalsePredicate():
            # p | False == p
            return left
        case AlwaysFalsePredicate(), _:
            # False | p == p
            return right
        case _, AlwaysTruePredicate():
            # p | True == True
            return AlwaysTruePredicate()
        case AlwaysTruePredicate(), _:
            # True | p == True
            return AlwaysTruePredicate()

        case GePredicate(v1), GePredicate(v2):
            # x >= v1 | x >= v2 => x >= min(v1, v2)
            return GePredicate(v=min(v1, v2))
        case AnyPredicate(left_any), AnyPredicate(right_any):
            return AnyPredicate(optimize(OrPredicate(left=left_any, right=right_any)))

    return predicate


def optimize_or_not[T](left: Predicate[T], right: Predicate[T]) -> Predicate[T] | None:
    match left, right:
        case NotPredicate(left_p), _ if right == left_p:  # ~p | p == True
            return AlwaysTruePredicate()
        case _, NotPredicate(right_p) if left == right_p:  # p | ~p == True
            return AlwaysTruePredicate()

    return None
