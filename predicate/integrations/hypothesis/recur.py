"""Strategies for recur_p and mutual_recur_p: sequences where each element is constrained by the one before it."""

from collections.abc import Callable
from typing import Any

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from predicate.mutual_recur_predicate import MutualRecurPredicate
from predicate.predicate import Predicate
from predicate.recur_predicate import RecurPredicate

# ponytail: chains of 1..5 elements (no empty ones), seeded with an int or str; add seeds if a predicate needs others
_MAX_LENGTH = 5
_seeds = st.integers() | st.text()


def from_recur(predicate: Predicate[Any]) -> SearchStrategy[list[Any]] | None:
    """Return a strategy for a recursive predicate, or None if the predicate isn't one."""
    match predicate:
        case RecurPredicate(_, predicate_1, predicate_n):
            return _chains(predicate_1, predicate_n, _recur_step)
        case MutualRecurPredicate(_, predicate_1, predicate_n):
            return _chains(predicate_1, predicate_n, _mutual_step)
        case _:
            return None


def _recur_step(fn: Callable[..., Any], x: Any) -> tuple[Predicate[Any], Callable[..., Any]]:
    return fn(x), fn


def _mutual_step(fn: Callable[..., Any], x: Any) -> tuple[Predicate[Any], Callable[..., Any]]:
    predicate, recur_predicate = fn(x)
    return predicate, recur_predicate.predicate_n


def _is_seed(predicate_1: Predicate[Any], predicate_n: Callable[..., Any]) -> Callable[[Any], bool]:
    """Return a check that a value satisfies predicate_1 and can start the chain, without raising for its type."""

    def check(x: Any) -> bool:
        try:
            predicate_n(x)
            return bool(predicate_1(x))
        except Exception:  # noqa: BLE001
            return False

    return check


@st.composite
def _chains(
    draw: st.DrawFn, predicate_1: Predicate[Any], predicate_n: Callable[..., Any], step: Callable[..., Any]
) -> list[Any]:
    from predicate.integrations.hypothesis.strategies import from_predicate  # circular import

    chain = [draw(_seeds.filter(_is_seed(predicate_1, predicate_n)))]
    state = predicate_n
    for _ in range(draw(st.integers(0, _MAX_LENGTH - 1))):
        predicate, state = step(state, chain[-1])
        chain.append(draw(from_predicate(predicate)))
    return chain
