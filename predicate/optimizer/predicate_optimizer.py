from predicate.all_predicate import AllPredicate
from predicate.any_predicate import AnyPredicate
from predicate.optimizer.all_optimizer import optimize_all_predicate
from predicate.optimizer.and_optimizer import optimize_and_predicate
from predicate.optimizer.any_optimizer import optimize_any_predicate
from predicate.optimizer.in_optimizer import optimize_in_predicate, optimize_not_in_predicate
from predicate.optimizer.not_optimizer import optimize_not_predicate
from predicate.optimizer.or_optimizer import optimize_or_predicate
from predicate.optimizer.xor_optimizer import optimize_xor_predicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate, XorPredicate
from predicate.set_predicates import InPredicate, NotInPredicate


def optimize[T](predicate: Predicate[T]) -> Predicate[T]:
    """Optimize the given predicate."""
    match predicate:
        case AllPredicate() as all_predicate:
            return optimize_all_predicate(all_predicate)
        case AndPredicate() as and_predicate:
            return optimize_and_predicate(and_predicate)
        case AnyPredicate() as any_predicate:
            return optimize_any_predicate(any_predicate)
        case NotPredicate() as not_predicate:
            return optimize_not_predicate(not_predicate)
        case OrPredicate() as or_predicate:
            return optimize_or_predicate(or_predicate)
        case XorPredicate() as xor_predicate:
            return optimize_xor_predicate(xor_predicate)
        case InPredicate() as in_predicate:
            return optimize_in_predicate(in_predicate)
        case NotInPredicate() as not_in_predicate:
            return optimize_not_in_predicate(not_in_predicate)
        case _:
            return predicate


def can_optimize[T](predicate: Predicate[T]) -> bool:
    """Return True if the predicate can be optimized, otherwise False."""
    return optimize(predicate) != predicate
