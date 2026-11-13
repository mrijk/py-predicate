"""Hypothesis integration: turn predicates into Hypothesis search strategies.

Requires the optional dependency: pip install py-predicate[hypothesis]
"""

import builtins
from collections.abc import Callable, Iterable
from functools import reduce
from typing import Any, Literal

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.frozendict_of_predicate import FrozenDictOfPredicate
from predicate.frozenset_of_predicate import FrozenSetOfPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.in_predicate import InPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.negate import negate
from predicate.not_predicate import NotPredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.tuple_of_predicate import TupleOfPredicate
from predicate.xor_predicate import XorPredicate

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


def given_predicate(
    *args: Predicate[Any], **kwargs: Predicate[Any]
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Like hypothesis.given, but takes predicates instead of strategies."""
    return given(*(from_predicate(p) for p in args), **{k: from_predicate(p) for k, p in kwargs.items()})


def _leaves(predicate: Predicate[Any]) -> list[Predicate[Any]]:
    match predicate:
        case AndPredicate(left, right):
            return [*_leaves(left), *_leaves(right)]
        case _:
            return [predicate]


def _anything() -> SearchStrategy[Any]:
    return st.from_type(object)


def _falsy() -> SearchStrategy[Any]:
    empties = (st.none(), st.just(0), st.just(0.0), st.just(False), st.just(""), st.just(b""), st.just(()))
    return st.one_of(*empties, st.builds(list), st.builds(dict), st.builds(set))


# Parameterless predicates: a base strategy; the predicate itself is applied as a filter on top
_BASE: dict[type, Callable[[], SearchStrategy[Any]]] = {
    AlwaysTruePredicate: _anything,
    AlwaysFalsePredicate: st.nothing,
    IsNonePredicate: st.none,
    IsNotNonePredicate: _anything,
    IsTruthyPredicate: _anything,
    IsFalsyPredicate: _falsy,
}


def _from_leaf(predicate: Predicate[Any]) -> SearchStrategy[Any]:
    match predicate:
        case EqPredicate(v):
            return st.just(v)
        case OrPredicate(left, right):
            return st.one_of(from_predicate(left), from_predicate(right))
        case NotPredicate(inner):
            return _from_not(predicate, inner)
        case IsInstancePredicate(klasses):
            return st.one_of(*(st.from_type(klass) for klass in klasses))
        case InPredicate(v) if isinstance(v, Iterable):
            return _sampled_from(list(v))
        case XorPredicate(left, right):
            return from_predicate(OrPredicate(AndPredicate(left, negate(right)), AndPredicate(negate(left), right)))
        case _:
            return _from_base(predicate)


def _sampled_from(values: list[Any]) -> SearchStrategy[Any]:
    return st.sampled_from(values) if values else st.nothing()


def _from_base(predicate: Predicate[Any]) -> SearchStrategy[Any]:
    base = _BASE.get(type(predicate))
    return base().filter(predicate) if base else _from_collection(predicate)


def _from_collection(predicate: Predicate[Any]) -> SearchStrategy[Any]:
    match predicate:
        case AllPredicate(inner) | ListOfPredicate(inner):
            return st.lists(from_predicate(inner))
        case AnyPredicate(inner):
            # ponytail: every element matches; add non-matching filler elements if diversity matters
            return st.lists(from_predicate(inner), min_size=1)
        case SetOfPredicate(inner):
            return st.sets(from_predicate(inner))
        case FrozenSetOfPredicate(inner):
            return st.frozensets(from_predicate(inner))
        case TupleOfPredicate(predicates):
            return st.tuples(*(from_predicate(p) for p in predicates))
        case DictOfPredicate(pairs):
            return _from_dict_of(predicate, pairs)
        case FrozenDictOfPredicate(pairs):
            return _from_frozendict_of(predicate, pairs)
        case _:
            return _from_type(predicate).filter(predicate)


def _from_dict_of(
    predicate: DictOfPredicate, pairs: list[tuple[Predicate[Any], Predicate[Any]]]
) -> SearchStrategy[Any]:
    """Merge one small dict per (key, value) pair; the filter drops empty dicts and key/value clashes."""
    parts = [st.dictionaries(from_predicate(key_p), from_predicate(value_p)) for key_p, value_p in pairs]
    return st.tuples(*parts).map(lambda ds: {k: v for d in ds for k, v in d.items()}).filter(predicate)


def _from_frozendict_of(
    predicate: FrozenDictOfPredicate, pairs: list[tuple[Predicate[Any], Predicate[Any]]]
) -> SearchStrategy[Any]:
    # frozendict is only a builtin from Python 3.15; before that is_frozendict_p is never true
    if (frozendict := getattr(builtins, "frozendict", None)) is None:
        return st.nothing()
    return _from_dict_of(predicate.dict_of_predicate, pairs).map(frozendict).filter(predicate)


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
