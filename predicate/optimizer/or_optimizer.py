from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    GePredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
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

        case AndPredicate(and_left_left, and_left_right), AndPredicate(and_right_left, and_right_right):
            match and_left_left, and_left_right, and_right_left, and_right_right:
                case (
                    NotPredicate(left_not),
                    Predicate() as q,
                    Predicate() as p,
                    NotPredicate(right_not),
                ) if left_not == p and right_not == q:
                    # (~p & q) | (p & ~q) == p ^ q
                    return p ^ q
                case (
                    Predicate() as p,
                    NotPredicate(left_not),
                    NotPredicate(right_not),
                    Predicate() as q,
                ) if left_not == q and right_not == p:
                    # (p & ~q) | (~p & q) == p ^ q
                    return p ^ q

        case _, AndPredicate(and_left, and_right):
            match and_left:
                case NotPredicate(not_predicate) if not_predicate == left:  # p | (~p & q) == p | q
                    return OrPredicate(left=left, right=and_right)

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
