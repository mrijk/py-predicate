from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.eq_predicate import EqPredicate
from predicate.optimizer.in_optimizer import optimize_in_predicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.set_predicates import InPredicate


def optimize_xor_predicate[T](predicate: XorPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    if optimized := optimize_xor_not(left=predicate.left, right=predicate.right):
        return optimized

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    if optimized := optimize_xor_not(left=left, right=right):
        return optimized

    match left, right:
        case _, AlwaysFalsePredicate():  # p ^ False = p
            return left
        case AlwaysFalsePredicate(), _:  # False ^ p = p
            return right
        case _, AlwaysTruePredicate():  # p ^ True = ~p
            return optimize(NotPredicate(predicate=left))
        case AlwaysTruePredicate(), _:  # True ^ p = ~p
            return optimize(NotPredicate(predicate=right))
        case _, _ if left == right:  # p ^ p == False
            return always_false_p

        case InPredicate(v1), InPredicate(v2):
            return optimize_in_predicate(InPredicate(v=v1 ^ v2))

        case InPredicate(v1), EqPredicate(v2):
            return optimize_in_predicate(InPredicate(v=v1 ^ {v2}))

        case _, AndPredicate(and_left, and_right):
            match and_left, and_right:
                case NotPredicate(not_predicate), _ if left == not_predicate:
                    return NotPredicate(OrPredicate(left=left, right=and_right))  # p ^ (^p & q) == ~(p | q)
                case _, NotPredicate(not_predicate) if left == not_predicate:
                    return NotPredicate(OrPredicate(left=left, right=and_left))  # p ^ (q & ^p) == ~(p | q)
                case _:
                    return AndPredicate(left=left, right=NotPredicate(and_right))  # p ^ (p & q) = p & ~q
        case AndPredicate(), _:
            return optimize_xor_predicate(XorPredicate(left=right, right=left))

        case _, OrPredicate(or_left, or_right) if left == or_left:
            # TODO: this is not correct!
            return or_right
        case _, OrPredicate(or_left, or_right) if left == or_right:
            return or_left
        case OrPredicate(or_left, or_right), _ if right == or_left:
            return or_right
        case OrPredicate(or_left, or_right), _ if right == or_right:
            return or_left

        case XorPredicate(xor_left, xor_right), _ if right == xor_left:
            return xor_right  # p ^ q ^ p = q
        case XorPredicate(xor_left, xor_right), _ if right == xor_right:
            return xor_left  # p ^ q ^ q = p

        case _:
            return XorPredicate(left=left, right=right)


def optimize_xor_not[T](left: Predicate[T], right: Predicate[T]) -> Predicate[T] | None:
    from predicate.negate import negate

    match left, right:
        case NotPredicate(left_p), NotPredicate(right_p):  # ~p ^ ~q == p ^ q
            return XorPredicate(left=left_p, right=right_p)
        case _, _ if left == negate(right):  # ~p ^ p == True
            return always_true_p

    return None
