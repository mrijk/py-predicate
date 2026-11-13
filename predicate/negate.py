from functools import singledispatch
from typing import Any

from predicate import (
    always_false_p,
    always_true_p,
    is_falsy_p,
    is_none_p,
    is_not_none_p,
    is_truthy_p,
)
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.has_length_predicate import HasLengthPredicate, is_empty_p, is_not_empty_p
from predicate.in_predicate import InPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.not_predicate import NotPredicate
from predicate.predicate import Predicate


@singledispatch
def negate[T](predicate: Predicate[T]) -> Predicate[T]:
    """Return the negation of a predicate."""
    return NotPredicate(predicate=predicate)


@negate.register(NotPredicate)
def negate_is_not(predicate: NotPredicate[Any]) -> Predicate[Any]:
    return predicate.predicate


@negate.register
def negate_is_false(_predicate: AlwaysFalsePredicate) -> Predicate[Any]:
    return always_true_p


@negate.register
def negate_is_true(_predicate: AlwaysTruePredicate) -> Predicate[Any]:
    return always_false_p


@negate.register(IsFalsyPredicate)
def negate_is_falsy(_predicate: IsFalsyPredicate[Any]) -> Predicate[Any]:
    return is_truthy_p


@negate.register(IsTruthyPredicate)
def negate_is_truthy(_predicate: IsTruthyPredicate[Any]) -> Predicate[Any]:
    return is_falsy_p


@negate.register(EqPredicate)
def negate_eq(predicate: EqPredicate[Any]) -> Predicate[Any]:
    return NePredicate(v=predicate.v)


@negate.register(NePredicate)
def negate_ne(predicate: NePredicate[Any]) -> Predicate[Any]:
    return EqPredicate(v=predicate.v)


@negate.register(GtPredicate)
def negate_gt(predicate: GtPredicate[Any]) -> Predicate[Any]:
    return LePredicate(v=predicate.v)


@negate.register(GePredicate)
def negate_ge(predicate: GePredicate[Any]) -> Predicate[Any]:
    return LtPredicate(v=predicate.v)


@negate.register(InPredicate)
def negate_in(predicate: InPredicate[Any]) -> Predicate[Any]:
    return NotInPredicate(v=predicate.v)


@negate.register(NotInPredicate)
def negate_not_in(predicate: NotInPredicate[Any]) -> Predicate[Any]:
    return InPredicate(v=predicate.v)


@negate.register(LtPredicate)
def negate_lt(predicate: LtPredicate[Any]) -> Predicate[Any]:
    return GePredicate(v=predicate.v)


@negate.register(LePredicate)
def negate_le(predicate: LePredicate[Any]) -> Predicate[Any]:
    return GtPredicate(v=predicate.v)


@negate.register(IsNonePredicate)
def negate_is_none(_predicate: IsNonePredicate[Any]) -> Predicate[Any]:
    return is_not_none_p


@negate.register(IsNotNonePredicate)
def negate_is_not_none(_predicate: IsNotNonePredicate[Any]) -> Predicate[Any]:
    return is_none_p


@negate.register(HasLengthPredicate)
def negate_has_length(predicate: HasLengthPredicate[Any]) -> Predicate[Any]:
    match predicate.length_p:
        case EqPredicate(v) if v == 0:
            return is_not_empty_p
        case GePredicate(v) if v == 1:
            return is_empty_p
        case GtPredicate(v) if v == 0:
            return is_empty_p
        case _:
            return NotPredicate(predicate=predicate)
