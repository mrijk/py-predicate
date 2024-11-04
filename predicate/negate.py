from functools import singledispatch

from predicate import AlwaysTruePredicate, EqPredicate, NePredicate, NotPredicate, Predicate
from predicate.predicate import (
    AlwaysFalsePredicate,
    GePredicate,
    GtPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    LePredicate,
    LtPredicate,
)


@singledispatch
def negate[T](predicate: Predicate[T]) -> Predicate[T]:
    return NotPredicate(predicate=predicate)


@negate.register
def negate_is_false(_predicate: AlwaysFalsePredicate) -> Predicate:
    return AlwaysTruePredicate()


@negate.register
def negate_is_true(_predicate: AlwaysTruePredicate) -> Predicate:
    return AlwaysFalsePredicate()


@negate.register
def negate_eq(predicate: EqPredicate) -> Predicate:
    return NotPredicate(predicate=NePredicate(v=predicate.v))


@negate.register
def negate_ne(predicate: NePredicate) -> Predicate:
    return NotPredicate(predicate=EqPredicate(v=predicate.v))


@negate.register
def negate_gt(predicate: GtPredicate) -> Predicate:
    return LePredicate(v=predicate.v)


@negate.register
def negate_ge(predicate: GePredicate) -> Predicate:
    return LtPredicate(v=predicate.v)


@negate.register
def negate_lt(predicate: LtPredicate) -> Predicate:
    return GePredicate(v=predicate.v)


@negate.register
def negate_le(predicate: LePredicate) -> Predicate:
    return GtPredicate(v=predicate.v)


@negate.register
def negate_is_none(_predicate: IsNonePredicate) -> Predicate:
    return IsNotNonePredicate()


@negate.register
def negate_is_not_none(_predicate: IsNotNonePredicate) -> Predicate:
    return IsNonePredicate()
