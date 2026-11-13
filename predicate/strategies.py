"""Hypothesis integration: turn predicates into Hypothesis search strategies.

Requires the optional dependency: pip install py-predicate[hypothesis]
"""

from functools import reduce
from typing import Any, Literal

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate.all_predicate import AllPredicate
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.negate import negate
from predicate.not_predicate import NotPredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate

type _Constraint = tuple[Literal["lo", "hi"], Any, bool]  # (side, value, exclusive)
type _Bounds = dict[str, tuple[Any, bool]]


def from_predicate(predicate: Predicate[Any]) -> SearchStrategy[Any]:
    """Return a Hypothesis strategy that generates values satisfying the predicate.

    Numeric bounds are merged into a single native strategy; anything else is generated from the
    predicate's type and filtered, so the result is correct for every predicate that knows its type.
    """
    leaves = _leaves(predicate)
    constraints = [c for leaf in leaves for c in _constraints(leaf)]
    others = [leaf for leaf in leaves if not _constraints(leaf)]

    base, filters = (_numeric(constraints), others) if constraints else (_from_leaf(others[0]), others[1:])
    return reduce(lambda strategy, p: strategy.filter(p), filters, base)


def _leaves(predicate: Predicate[Any]) -> list[Predicate[Any]]:
    match predicate:
        case AndPredicate(left, right):
            return [*_leaves(left), *_leaves(right)]
        case _:
            return [predicate]


def _from_leaf(predicate: Predicate[Any]) -> SearchStrategy[Any]:
    match predicate:
        case EqPredicate(v):
            return st.just(v)
        case OrPredicate(left, right):
            return st.one_of(from_predicate(left), from_predicate(right))
        case AllPredicate(inner):
            return st.lists(from_predicate(inner))
        case AnyPredicate(inner):
            # ponytail: every element matches; add non-matching filler elements if diversity matters
            return st.lists(from_predicate(inner), min_size=1)
        case NotPredicate(inner):
            return _from_not(predicate, inner)
        case IsInstancePredicate(klasses):
            return st.one_of(*(st.from_type(klass) for klass in klasses))
        case _:
            return _from_type(predicate).filter(predicate)


def _from_type(predicate: Predicate[Any]) -> SearchStrategy[Any]:
    try:
        return st.from_type(predicate.klass)
    except NotImplementedError:
        raise TypeError(f"Can't derive a strategy for {predicate!r}") from None


def _from_not(predicate: NotPredicate[Any], inner: Predicate[Any]) -> SearchStrategy[Any]:
    """Push the negation inwards where possible (De Morgan, negate), otherwise generate and filter."""
    match inner:
        case AndPredicate(left, right):
            return from_predicate(OrPredicate(negate(left), negate(right)))
        case OrPredicate(left, right):
            return from_predicate(AndPredicate(negate(left), negate(right)))
        case IsInstancePredicate():
            return st.from_type(object).filter(predicate)
        case _:
            negated = negate(inner)
            return _from_type(predicate).filter(predicate) if negated == predicate else from_predicate(negated)


def _constraints(predicate: Predicate[Any]) -> list[_Constraint]:
    """Return the numeric bounds a predicate expresses, or [] if it is not a numeric bound."""
    found: list[_Constraint]
    match predicate:
        case GePredicate(v):
            found = [("lo", v, False)]
        case GtPredicate(v):
            found = [("lo", v, True)]
        case LePredicate(v):
            found = [("hi", v, False)]
        case LtPredicate(v):
            found = [("hi", v, True)]
        case GeLePredicate(lower, upper):
            found = [("lo", lower, False), ("hi", upper, False)]
        case GeLtPredicate(lower, upper):
            found = [("lo", lower, False), ("hi", upper, True)]
        case GtLePredicate(lower, upper):
            found = [("lo", lower, True), ("hi", upper, False)]
        case GtLtPredicate(lower, upper):
            found = [("lo", lower, True), ("hi", upper, True)]
        case _:
            return []
    return found if all(isinstance(value, int | float) for _, value, _ in found) else []


def _tighten(bounds: _Bounds, constraint: _Constraint) -> _Bounds:
    side, v, exclusive = constraint
    current, _ = bounds[side]
    tighter = current is None or (v > current if side == "lo" else v < current) or (v == current and exclusive)
    return bounds | {side: (v, exclusive)} if tighter else bounds


def _numeric(constraints: list[_Constraint]) -> SearchStrategy[Any]:
    bounds = reduce(_tighten, constraints, {"lo": (None, False), "hi": (None, False)})
    (lo, lo_x), (hi, hi_x) = bounds["lo"], bounds["hi"]
    is_int = all(isinstance(bound, int) for bound in (lo, hi) if bound is not None)
    return _integers(lo, lo_x, hi, hi_x) if is_int else _floats(lo, lo_x, hi, hi_x)


def _integers(lo: Any, lo_x: bool, hi: Any, hi_x: bool) -> SearchStrategy[Any]:
    lo = None if lo is None else lo + lo_x
    hi = None if hi is None else hi - hi_x
    empty = lo is not None and hi is not None and lo > hi
    return st.nothing() if empty else st.integers(min_value=lo, max_value=hi)


def _floats(lo: Any, lo_x: bool, hi: Any, hi_x: bool) -> SearchStrategy[Any]:
    empty = lo is not None and hi is not None and (lo > hi or (lo == hi and (lo_x or hi_x)))
    return st.nothing() if empty else st.floats(lo, hi, exclude_min=lo_x, exclude_max=hi_x, allow_nan=False)
