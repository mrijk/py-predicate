from functools import singledispatch

from predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    Predicate,
)


@singledispatch
def negate[T](predicate: Predicate[T]) -> Predicate[T]:
    return NotPredicate(predicate=predicate)


@negate.register
def negate_is_not(predicate: NotPredicate) -> Predicate:
    return predicate.predicate


@negate.register
def negate_is_false(_predicate: AlwaysFalsePredicate) -> Predicate:
    return AlwaysTruePredicate()


@negate.register
def negate_is_true(_predicate: AlwaysTruePredicate) -> Predicate:
    return AlwaysFalsePredicate()


@negate.register
def negate_eq(predicate: EqPredicate) -> Predicate:
    return NePredicate(v=predicate.v)


@negate.register
def negate_ne(predicate: NePredicate) -> Predicate:
    return EqPredicate(v=predicate.v)


@negate.register
def negate_gt(predicate: GtPredicate) -> Predicate:
    return LePredicate(v=predicate.v)


@negate.register
def negate_ge(predicate: GePredicate) -> Predicate:
    return LtPredicate(v=predicate.v)


@negate.register
def negate_in(predicate: InPredicate) -> Predicate:
    return NotInPredicate(v=predicate.v)


@negate.register
def negate_not_in(predicate: NotInPredicate) -> Predicate:
    return InPredicate(v=predicate.v)


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
