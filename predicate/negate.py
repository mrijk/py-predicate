from functools import singledispatch

from predicate import (
    always_false_p,
    always_true_p,
    is_empty_p,
    is_none_p,
    is_not_none_p,
)
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.is_empty_predicate import IsEmptyPredicate, IsNotEmptyPredicate, is_not_empty_p
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import (
    NotPredicate,
    Predicate,
)
from predicate.set_predicates import InPredicate, NotInPredicate
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
