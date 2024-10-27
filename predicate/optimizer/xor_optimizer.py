from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
    get_as_and_predicate,
    get_as_not_predicate,
)


def optimize_xor_predicate[T](predicate: XorPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize, optimize_predicate

    if optimized := optimize_xor_not(left=predicate.left, right=predicate.right):
        return optimized

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    # False ^ False = False

    if isinstance(left, AlwaysFalsePredicate) and isinstance(right, AlwaysFalsePredicate):
        return AlwaysFalsePredicate()

    # True ^ True = False

    if isinstance(left, AlwaysTruePredicate) and isinstance(right, AlwaysTruePredicate):
        return AlwaysFalsePredicate()

    # p ^ False = p
    if isinstance(right, AlwaysFalsePredicate):
        return left

    # False ^ p = p
    if isinstance(left, AlwaysFalsePredicate):
        return right

    # p ^ True = ~p
    if isinstance(right, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=left))

    # True ^ p = ~p
    if isinstance(left, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=right))

    # p ^ p == False
    if left == right:
        return AlwaysFalsePredicate()

    if optimized := optimize_xor_not(left=left, right=right):
        return optimized

    if and_predicate := get_as_and_predicate(right):
        # p ^ (^p & q) == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if left == not_predicate.predicate:
                return NotPredicate(OrPredicate(left=left, right=and_predicate.right))
        # p ^ (q & ^p) == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.right):
            if left == not_predicate.predicate:
                return NotPredicate(OrPredicate(left=predicate.left, right=and_predicate.left))

    if and_predicate := get_as_and_predicate(left):
        # (^p & q) ^ p == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if right == not_predicate.predicate:
                return NotPredicate(OrPredicate(left=right, right=and_predicate.right))
        # (q & ^p) ^ p == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.right):
            if right == not_predicate.predicate:
                return NotPredicate(OrPredicate(left=right, right=and_predicate.left))

    return predicate


def optimize_xor_not[T](left: Predicate[T], right: Predicate[T]) -> Predicate[T] | None:
    match left, right:
        case NotPredicate(left_p), NotPredicate(right_p):
            return XorPredicate(left=left_p, right=right_p)
        case NotPredicate(left_p), _ if right == left_p:  # ~p ^ p == True
            return AlwaysTruePredicate()
        case _, NotPredicate(right_p) if left == right_p:  # p ^ ~p == True
            return AlwaysTruePredicate()

    return None
