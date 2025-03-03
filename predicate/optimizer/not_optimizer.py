from predicate.all_predicate import AllPredicate
from predicate.any_predicate import AnyPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, XorPredicate


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> MaybeOptimized[T]:
    from predicate.negate import negate
    from predicate.optimizer.predicate_optimizer import optimize

    # ~~p == p
    match predicate.predicate:
        case NotPredicate(not_predicate):
            return Optimized(optimize(not_predicate))

    optimized = optimize(predicate.predicate)

    match optimized:
        case AllPredicate(all_predicate):
            match negate(all_predicate):
                case _ as inverted:
                    return Optimized(AnyPredicate(predicate=inverted))

        case AndPredicate(left, right):
            match left, right:
                case _, NotPredicate(not_predicate):
                    return Optimized(OrPredicate(left=negate(left), right=not_predicate))  # ~(p & ~q) => ~p | q
                case NotPredicate(not_predicate), _:
                    return Optimized(OrPredicate(left=not_predicate, right=negate(right)))  # ~(~p & q) => p | ~q
                case _:
                    return Optimized(negate(optimized)) if optimized != predicate.predicate else NotOptimized()

        case AnyPredicate(any_predicate):
            match negate(any_predicate):
                case _ as inverted:
                    return Optimized(AllPredicate(predicate=inverted))
        case OrPredicate(left, right):
            match left, right:
                case _, NotPredicate(not_predicate):
                    return Optimized(AndPredicate(left=negate(left), right=not_predicate))  # ~(p | ~q) => ~p & q
                case NotPredicate(not_predicate), _:
                    return Optimized(AndPredicate(left=not_predicate, right=negate(right)))  # ~(~p | q) => p & ~q
                case _:
                    return Optimized(negate(optimized)) if optimized != predicate.predicate else NotOptimized()

        case XorPredicate(left, right):
            match left, right:
                case NotPredicate(not_predicate), _:  # ~(~p ^ q) == p ^ q
                    return Optimized(XorPredicate(left=not_predicate, right=right))
                case _, NotPredicate(not_predicate):  # ~(p ^ ~q) == p ^ q
                    return Optimized(XorPredicate(left=left, right=not_predicate))
                case _:  # ~(p ^ q) == ~p ^ q
                    return Optimized(XorPredicate(left=NotPredicate(predicate=left), right=right))

    return Optimized(negate(optimized))
