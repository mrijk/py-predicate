"""A Hypothesis strategy that generates predicates, for property-testing code that takes predicates."""

import operator
from typing import Any

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate import (
    always_false_p,
    always_true_p,
    eq_p,
    ge_p,
    gt_p,
    in_p,
    is_even_p,
    is_odd_p,
    le_p,
    lt_p,
    ne_p,
)
from predicate.predicate import Predicate

_ints = st.integers(-5, 5)


def _int_leaves() -> SearchStrategy[Predicate[Any]]:
    constants = st.sampled_from([always_true_p, always_false_p, is_even_p, is_odd_p])
    compared = (st.builds(p, _ints) for p in (eq_p, ne_p, ge_p, gt_p, le_p, lt_p))
    return st.one_of(constants, *compared, st.builds(in_p, st.frozensets(_ints)))


def predicates(
    leaves: SearchStrategy[Predicate[Any]] | None = None, max_leaves: int = 8
) -> SearchStrategy[Predicate[Any]]:
    """Return a strategy that generates predicates: leaves combined with ``&``, ``|``, ``^`` and ``~``.

    The default leaves are predicates over small integers (comparisons, ``in_p``, even and odd), so every generated
    predicate can be called with an int. Pass ``leaves`` for another domain.
    """

    def extend(inner: SearchStrategy[Predicate[Any]]) -> SearchStrategy[Predicate[Any]]:
        binary = (st.builds(op, inner, inner) for op in (operator.and_, operator.or_, operator.xor))
        return st.one_of(*binary, st.builds(operator.invert, inner))

    return st.recursive(leaves or _int_leaves(), extend, max_leaves=max_leaves)
