from predicate.optimizer.and_optimizer import optimize_and_predicate
from predicate.optimizer.not_optimizer import optimize_not_predicate
from predicate.optimizer.or_optimizer import optimize_or_predicate
from predicate.optimizer.xor_optimizer import optimize_xor_predicate
from predicate.predicate import (
    Predicate,
    NotPredicate,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
    AndPredicate,
    OrPredicate,
    XorPredicate,
)


def optimize[T](predicate: Predicate[T]) -> Predicate[T]:
    match predicate:
        case AndPredicate() as and_predicate:
            return optimize_and_predicate(and_predicate)
        case NotPredicate() as not_predicate:
            return optimize_not_predicate(not_predicate)
        case OrPredicate() as or_predicate:
            return optimize_or_predicate(or_predicate)
        case XorPredicate() as xor_predicate:
            return optimize_xor_predicate(xor_predicate)
        case _:
            return predicate


def can_optimize[T](predicate: Predicate[T]) -> bool:
    return optimize(predicate) != predicate


def optimize_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    if predicate.always_true:
        return AlwaysTruePredicate()
    if predicate.always_false:
        return AlwaysFalsePredicate()
    return predicate
