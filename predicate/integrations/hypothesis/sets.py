"""Strategies for the set predicates: subset, superset and intersects."""

from collections.abc import Set as AbstractSet
from typing import Any

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate.integrations.hypothesis.helpers import sampled_from
from predicate.predicate import Predicate
from predicate.set_predicates import (
    IntersectsPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)


def from_set(predicate: Predicate[Any]) -> SearchStrategy[set[Any]] | None:
    """Return a strategy for a set predicate, or None if the predicate isn't one."""
    match predicate:
        case IsSubsetPredicate(v):
            strategy = _subsets(v)
        case IsRealSubsetPredicate(v):
            strategy = _subsets(v) if v else st.nothing()
        case IsSupersetPredicate(v):
            strategy = _supersets(v, min_extra=0)
        case IsRealSupersetPredicate(v):
            strategy = _supersets(v, min_extra=1)
        case IntersectsPredicate(v):
            strategy = _intersecting(v) if v else st.nothing()
        case _:
            return None
    return strategy.filter(predicate)


def _subsets(v: AbstractSet[Any]) -> SearchStrategy[set[Any]]:
    return st.sets(sampled_from(v))


def _supersets(v: AbstractSet[Any], min_extra: int) -> SearchStrategy[set[Any]]:
    return st.sets(_elements(v), min_size=min_extra).map(lambda extra: set(v) | extra)


def _intersecting(v: AbstractSet[Any]) -> SearchStrategy[set[Any]]:
    return st.builds(set.union, st.sets(sampled_from(v), min_size=1), st.sets(_elements(v)))


def _elements(v: AbstractSet[Any]) -> SearchStrategy[Any]:
    """Elements of the same type(s) as v, for the extra elements of a superset; any simple value if v is empty."""
    types = {type(element) for element in v}
    return st.one_of(*(st.from_type(klass) for klass in types)) if types else st.integers() | st.text()
