from predicate.predicate import EqPredicate, NePredicate, Predicate
from predicate.set_predicates import InPredicate, NotInPredicate


def optimize_in_predicate[T](predicate: InPredicate[T]) -> Predicate[T]:
    if len(v := predicate.v) == 1:
        return EqPredicate(v=v.pop())
    return predicate


def optimize_not_in_predicate[T](predicate: NotInPredicate[T]) -> Predicate[T]:
    if len(v := predicate.v) == 1:
        return NePredicate(v=v.pop())
    return predicate
