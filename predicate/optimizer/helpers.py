from collections.abc import Callable, Iterable
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


def _bounds(left: Predicate[Any], right: Predicate[Any]) -> tuple[Any, Any, bool, bool] | None:
    """Return (lower, upper, lower is inclusive, upper is inclusive) of a gt_p / ge_p with a lt_p / le_p."""
    for low, up in ((left, right), (right, left)):
        if isinstance(low, GtPredicate | GePredicate) and isinstance(up, LtPredicate | LePredicate):
            return low.v, up.v, isinstance(low, GePredicate), isinstance(up, LePredicate)
    return None


def _ranges_cover_everything(left: Predicate[Any], right: Predicate[Any]) -> bool:
    """gt(b) | lt(a) covers everything when b < a, or when b == a and either end is inclusive."""
    if bounds := _bounds(left, right):
        lower, upper, low_incl, up_incl = bounds
        return _compare(lower, upper, low_incl or up_incl, lambda a, b: a < b)
    return False


def _ranges_are_disjoint(left: Predicate[Any], right: Predicate[Any]) -> bool:
    """gt(b) & lt(a) is empty when b > a, or when b == a and either end is exclusive."""
    if bounds := _bounds(left, right):
        lower, upper, low_incl, up_incl = bounds
        return _compare(lower, upper, not (low_incl and up_incl), lambda a, b: a > b)
    return False


def _compare(lower: Any, upper: Any, equal_counts: bool, strictly: Callable[[Any, Any], bool]) -> bool:
    try:
        return strictly(lower, upper) or (equal_counts and lower == upper)
    except TypeError:  # e.g. ge_p(0) with lt_p("a")
        return False


def is_tautology(left: Predicate[Any], right: Predicate[Any]) -> bool:
    """Whether left | right is always true, judged from the values or ranges in the two predicates."""
    return is_tautology_at_values(left, right) or _ranges_cover_everything(left, right)


def is_contradiction(left: Predicate[Any], right: Predicate[Any]) -> bool:
    """Whether left & right is always false, judged from the values or ranges in the two predicates."""
    return is_contradiction_at_values(left, right) or _ranges_are_disjoint(left, right)


def exclude_bound(left: Predicate[Any], right: Predicate[Any]) -> Predicate[Any] | None:
    """Return lt_p(v) for ne_p(v) & le_p(v) and gt_p(v) for ne_p(v) & ge_p(v), in either order, otherwise None."""
    for ne, bound in ((left, right), (right, left)):
        if isinstance(ne, NePredicate) and isinstance(bound, LePredicate | GePredicate) and ne.v == bound.v:
            return LtPredicate(v=ne.v) if isinstance(bound, LePredicate) else GtPredicate(v=ne.v)
    return None


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
