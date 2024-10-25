from predicate.predicate import (
    OrPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    NotPredicate,
    Predicate,
    get_as_not_predicate,
    get_as_and_predicate,
    AnyPredicate,
)


def optimize_or_predicate[T](predicate: OrPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    # before optimization

    if optimized := optimize_or_not(left=predicate.left, right=predicate.right):
        return optimized

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

    if optimized := optimize_or_not(left=left, right=right):
        return optimized

    # p | (~p & q) == p | q
    if and_predicate := get_as_and_predicate(right):
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if not_predicate.predicate == left:
                return OrPredicate(left=left, right=and_predicate.right)

    match left, right:
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
