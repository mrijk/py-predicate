from predicate.all_predicate import AllPredicate
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.not_predicate import NotPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.or_predicate import OrPredicate
from predicate.xor_predicate import XorPredicate


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> MaybeOptimized[T]:  # noqa: C901
    from predicate.negate import negate
    from predicate.optimizer.predicate_optimizer import optimize

    # ~~p == p
    match predicate.predicate:
        case NotPredicate(not_predicate):
            return Optimized(optimize(not_predicate))

    optimized = optimize(predicate.predicate)

    match optimized:
        # ~all_p(p) == any_p(~p), only when ~p simplifies: optimize_any_predicate turns any_p(~p) back into ~all_p(p)
        case AllPredicate(all_predicate) if negate(all_predicate) != NotPredicate(all_predicate):
            return Optimized(AnyPredicate(predicate=negate(all_predicate)))

        case AndPredicate(left, right):
            match left, right:
                case _, NotPredicate(not_predicate):
                    return Optimized(OrPredicate(left=negate(left), right=not_predicate))  # ~(p & ~q) => ~p | q
                case NotPredicate(not_predicate), _:
                    return Optimized(OrPredicate(left=not_predicate, right=negate(right)))  # ~(~p & q) => p | ~q
                case _:
                    return Optimized(negate(optimized)) if optimized != predicate.predicate else NotOptimized()

        # ~any_p(p) == all_p(~p), only when ~p simplifies: optimize_all_predicate turns all_p(~p) back into ~any_p(p)
        case AnyPredicate(any_predicate) if negate(any_predicate) != NotPredicate(any_predicate):
            return Optimized(AllPredicate(predicate=negate(any_predicate)))
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
