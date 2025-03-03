from predicate.all_predicate import AllPredicate
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.implies import implies
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate
from predicate.set_predicates import InPredicate, NotInPredicate
from predicate.standard_predicates import is_empty_p


def optimize_or_predicate[T](predicate: OrPredicate[T]) -> MaybeOptimized[T]:
    from predicate.negate import negate
    from predicate.optimizer.predicate_optimizer import optimizations, optimize

    match left := optimize(predicate.left), right := optimize(predicate.right):
        case _, AlwaysTruePredicate():
            return Optimized(always_true_p)  # p | True == True
        case AlwaysTruePredicate(), _:
            return Optimized(always_true_p)  # True | p == True
        case _, _ if left == right:  # p | p == p
            return Optimized(predicate=left)
        case _, _ if left == negate(right):
            return Optimized(predicate=always_true_p)  # p | ~p == True

        #
        case InPredicate(v1), EqPredicate(v2) if v2 not in v1:
            return Optimized(InPredicate((*v1, v2)))
        case EqPredicate(v1), InPredicate(v2) if v1 not in v2:
            return Optimized(InPredicate((*v2, v1)))
        case EqPredicate(v1), EqPredicate(v2) if v1 != v2:
            return Optimized(InPredicate((v1, v2)))
        case EqPredicate(v1), NotInPredicate(v2) if v1 in v2:
            return Optimized(optimize(NotInPredicate(v2 - {v1})))

        case InPredicate(v1), InPredicate(v2) if v := v1 | v2:
            return Optimized(optimize(InPredicate(v=v)))

        case InPredicate(v1), NotInPredicate(v2):
            if v := v2 - (v1 & v2):
                return Optimized(optimize(NotInPredicate(v=v)))
            return Optimized(always_true_p)

        #
        case AllPredicate(left_all), AnyPredicate(right_any) if left_all == right_any:
            return Optimized(OrPredicate(left=is_empty_p, right=right))

        case AnyPredicate(left_any), AllPredicate(right_all) if left_any == right_all:
            return Optimized(OrPredicate(left=is_empty_p, right=left))

        case AnyPredicate(left_any), AnyPredicate(right_any):
            return Optimized(AnyPredicate(optimize(OrPredicate(left=left_any, right=right_any))))

        # recursive & optimizations
        case OrPredicate(or_left, or_right), _:
            match optimizations(or_left | right):
                case Optimized(optimized):
                    return Optimized(predicate=optimize(optimized | or_right))
                case _:
                    match optimizations(or_right | right):
                        case Optimized(optimized):
                            return Optimized(optimize(optimized | or_left))
                        case _:
                            return NotOptimized()
        case _, OrPredicate():
            return optimize_or_predicate(OrPredicate(right, left))

        #
        case AndPredicate(and_left_left, and_left_right), AndPredicate(and_right_left, and_right_right):
            match and_left_left, and_left_right, and_right_left, and_right_right:
                case (
                    NotPredicate(left_not),
                    Predicate() as q,
                    Predicate() as p,
                    NotPredicate(right_not),
                ) if (
                    left_not == p and right_not == q
                ):
                    return Optimized(p ^ q)  # (~p & q) | (p & ~q) == p ^ q
                case (
                    Predicate() as p,
                    NotPredicate(left_not),
                    NotPredicate(right_not),
                    Predicate() as q,
                ) if (
                    left_not == q and right_not == p
                ):
                    return Optimized(p ^ q)  # (p & ~q) | (~p & q) == p ^ q
                case _:
                    return (
                        Optimized(OrPredicate(left=left, right=right))
                        if (left != predicate.left or right != predicate.right)
                        else NotOptimized()
                    )

        case _, AndPredicate(and_left, and_right):
            match and_left:
                case NotPredicate(not_predicate) if not_predicate == left:  # p | (~p & q) == p | q
                    return Optimized(left | and_right)

        #
        case _, _ if implies(left, right):
            return Optimized(right)
        case _, _ if implies(right, left):
            return Optimized(left)

    return Optimized(left | right) if (left != predicate.left or right != predicate.right) else NotOptimized()
