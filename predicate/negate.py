from functools import singledispatch

from predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsEmptyPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    Predicate,
    always_false_p,
    always_true_p,
    is_empty_p,
    is_none_p,
    is_not_none_p,
)
from predicate.predicate import IsFalsyPredicate, IsNotEmptyPredicate, IsTruthyPredicate, is_not_empty_p
from predicate.standard_predicates import is_falsy_p, is_truthy_p


@singledispatch
def negate[T](predicate: Predicate[T]) -> Predicate[T]:
    """Return the negation of a predicate."""
    return NotPredicate(predicate=predicate)


@negate.register
def negate_is_not(predicate: NotPredicate) -> Predicate:
    return predicate.predicate


@negate.register
def negate_is_false(_predicate: AlwaysFalsePredicate) -> Predicate:
    return always_true_p


@negate.register
def negate_is_true(_predicate: AlwaysTruePredicate) -> Predicate:
    return always_false_p


@negate.register
def negate_is_falsy(_predicate: IsFalsyPredicate) -> Predicate:
    return is_truthy_p


@negate.register
def negate_is_truthy(_predicate: IsTruthyPredicate) -> Predicate:
    return is_falsy_p


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
    return is_not_none_p


@negate.register
def negate_is_not_none(_predicate: IsNotNonePredicate) -> Predicate:
    return is_none_p


@negate.register
def negate_is_empty(_predicate: IsEmptyPredicate) -> Predicate:
    return is_not_empty_p


@negate.register
def negate_is_not_empty(_predicate: IsNotEmptyPredicate) -> Predicate:
    return is_empty_p
