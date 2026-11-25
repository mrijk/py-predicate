from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.in_predicate import InPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.predicate import Predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate

# The predicates that only look at the value: unlike a NamedPredicate (its truth value is set from outside) or an
# fn_p (any function), evaluating one of these at a value always gives the same answer
_VALUE_PREDICATES = (
    EqPredicate,
    NePredicate,
    InPredicate,
    NotInPredicate,
    GePredicate,
    GtPredicate,
    LePredicate,
    LtPredicate,
    GeLePredicate,
    GeLtPredicate,
    GtLePredicate,
    GtLtPredicate,
)


def holds_at(predicate: Predicate[Any], value: Any) -> bool | None:
    """Return whether predicate is true for value, or None if that can't be told (not a value predicate, or it raises)."""
    if not isinstance(predicate, _VALUE_PREDICATES):
        return None
    try:
        return bool(predicate(value))
    except Exception:  # noqa: BLE001  e.g. ge_p(0) applied to a str
        return None


def _values_of(predicate: Predicate[Any]) -> Iterable[Any] | None:
    """Return the only values an eq_p or in_p can be true for, or ne_p / not_in_p can be false for."""
    match predicate:
        case EqPredicate(v) | NePredicate(v):
            return [v]
        case InPredicate(v) | NotInPredicate(v) if isinstance(v, Iterable):
            return v
    return None


def is_contradiction_at_values(left: Predicate[Any], right: Predicate[Any]) -> bool:
    """Whether left & right is false: one is an eq_p / in_p and the other fails at all of its values."""
    for one, other in ((left, right), (right, left)):
        values = _values_of(one) if isinstance(one, EqPredicate | InPredicate) else None
        if values is not None and all(holds_at(other, v) is False for v in values):
            return True
    return False


def is_tautology_at_values(left: Predicate[Any], right: Predicate[Any]) -> bool:
    """Whether left | right is true: one is a ne_p / not_in_p and the other holds at all of its values."""
    for one, other in ((left, right), (right, left)):
        values = _values_of(one) if isinstance(one, NePredicate | NotInPredicate) else None
        if values is not None and all(holds_at(other, v) for v in values):
            return True
    return False


@dataclass
class MaybeOptimized[T]:
    """Base class to hold optimized predicate."""

    predicate: Predicate[T] | None = None


@dataclass
class Optimized[T](MaybeOptimized[Any]):
    """Contains predicate if optimized."""

    predicate: Predicate[T]


@dataclass
class NotOptimized(MaybeOptimized[Any]):
    """Not optimized."""
