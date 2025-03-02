from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.eq_predicate import EqPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    XorPredicate,
)
from predicate.set_predicates import InPredicate


def optimize_xor_predicate[T](predicate: XorPredicate[T]) -> MaybeOptimized[T]:
    from predicate.negate import negate
    from predicate.optimizer.predicate_optimizer import optimizations, optimize

    match left := optimize(predicate.left), right := optimize(predicate.right):
        case _, AlwaysFalsePredicate():  # p ^ False = p
            return Optimized(left)
        case AlwaysFalsePredicate(), _:  # False ^ p = p
            return Optimized(right)
        case _, AlwaysTruePredicate():  # p ^ True = ~p
            return Optimized(optimize(~left))
        case AlwaysTruePredicate(), _:  # True ^ p = ~p
            return Optimized(optimize(~right))
        case _, _ if left == right:  # p ^ p == False
            return Optimized(always_false_p)

        case InPredicate(v1), InPredicate(v2):
            return Optimized(optimize(InPredicate(v=v1 ^ v2)))
        case InPredicate(v1), EqPredicate(v2):
            return Optimized(optimize(InPredicate(v=v1 ^ {v2})))

        # recursive & optimizations
        case XorPredicate(xor_left, xor_right), _:
            match optimizations(xor_left ^ right):
                case Optimized(optimized):
                    return Optimized(predicate=optimize(optimized ^ xor_right))
                case _:
                    match optimizations(xor_right ^ right):
                        case Optimized(optimized):
                            return Optimized(optimize(optimized ^ xor_left))
                        case _:
                            return NotOptimized()
        case _, XorPredicate():
            return optimize_xor_predicate(XorPredicate(right, left))

        case _, AndPredicate(and_left, and_right):
            match and_left, and_right:
                case NotPredicate(not_predicate), _ if left == not_predicate:
                    return Optimized(NotPredicate(OrPredicate(left=left, right=and_right)))  # p ^ (^p & q) == ~(p | q)
                case _, NotPredicate(not_predicate) if left == not_predicate:
                    return Optimized(NotPredicate(OrPredicate(left=left, right=and_left)))  # p ^ (q & ^p) == ~(p | q)
                case _:
                    return Optimized(AndPredicate(left=left, right=NotPredicate(and_right)))  # p ^ (p & q) = p & ~q
        case AndPredicate(), _:
            return optimize_xor_predicate(XorPredicate(left=right, right=left))

        #

        case _, OrPredicate(or_left, or_right) if left == or_left:
            # TODO: this is not correct!
            return Optimized(or_right)
        case _, OrPredicate(or_left, or_right) if left == or_right:
            return Optimized(or_left)
        case OrPredicate(or_left, or_right), _ if right == or_left:
            return Optimized(or_right)
        case OrPredicate(or_left, or_right), _ if right == or_right:
            return Optimized(or_left)

        #

        case NotPredicate(left_p), NotPredicate(right_p):  # ~p ^ ~q == p ^ q
            return Optimized(left_p ^ right_p)
        case _, _ if left == negate(right):  # ~p ^ p == True
            return Optimized(always_true_p)
        case _:
            return Optimized(left ^ right) if (left != predicate.left or right != predicate.right) else NotOptimized()
