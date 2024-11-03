from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    InPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)


def optimize_xor_predicate[T](predicate: XorPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    if optimized := optimize_xor_not(left=predicate.left, right=predicate.right):
        return optimized

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    match left, right:
        case AlwaysFalsePredicate(), AlwaysFalsePredicate():  # False ^ False = False
            return AlwaysFalsePredicate()
        case AlwaysTruePredicate(), AlwaysTruePredicate():  # True ^ True = False
            return AlwaysFalsePredicate()
        case _, AlwaysFalsePredicate():  # p ^ False = p
            return left
        case AlwaysFalsePredicate(), _:  # False ^ p = p
            return right
        case _, AlwaysTruePredicate():  # p ^ True = ~p
            return optimize(NotPredicate(predicate=left))
        case AlwaysTruePredicate(), _:  # True ^ p = ~p
            return optimize(NotPredicate(predicate=right))
        case _, _ if left == right:  # p ^ p == False
            return AlwaysFalsePredicate()

    if optimized := optimize_xor_not(left=left, right=right):
        return optimized

    match left, right:
        case InPredicate(v1), InPredicate(v2):
            v = v1 ^ v2
            if not v:
                return AlwaysFalsePredicate()
            if len(v) == 1:
                return EqPredicate(v=v.pop())
            return InPredicate(v=v)

        case Predicate(), AndPredicate(and_left, and_right):
            match and_left, and_right:
                case NotPredicate(not_predicate), _ if left == not_predicate:
                    return NotPredicate(OrPredicate(left=left, right=and_right))  # p ^ (^p & q) == ~(p | q)
                case _, NotPredicate(not_predicate) if left == not_predicate:
                    return NotPredicate(OrPredicate(left=left, right=and_left))  # p ^ (q & ^p) == ~(p | q)
                case _:
                    pass
        case AndPredicate(and_left, and_right), Predicate():
            match and_left, and_right:
                case NotPredicate(not_predicate), _ if right == not_predicate:
                    return NotPredicate(OrPredicate(left=right, right=and_right))  # (^p & q) ^ p == ~(p | q)
                case _, NotPredicate(not_predicate) if right == not_predicate:
                    return NotPredicate(OrPredicate(left=right, right=and_left))  # (q & ^p) ^ p == ~(p | q)
                case _:
                    pass
        case XorPredicate(xor_left, xor_right), Predicate() if right == xor_left:
            return xor_right  # p ^ q ^ p = q
        case XorPredicate(xor_left, xor_right), Predicate() if right == xor_right:
            return xor_left  # p ^ q ^ q = p

    return predicate


def optimize_xor_not[T](left: Predicate[T], right: Predicate[T]) -> Predicate[T] | None:
    match left, right:
        case NotPredicate(left_p), NotPredicate(right_p):  # ~p ^ ~q == p ^ q
            return XorPredicate(left=left_p, right=right_p)
        case NotPredicate(left_p), _ if right == left_p:  # ~p ^ p == True
            return AlwaysTruePredicate()
        case _, NotPredicate(right_p) if left == right_p:  # p ^ ~p == True
            return AlwaysTruePredicate()

    return None
