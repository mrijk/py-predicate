from collections.abc import Iterable
from typing import Any

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy


def sampled_from(values: Iterable[Any]) -> SearchStrategy[Any]:
    """Like st.sampled_from, but an empty collection generates nothing instead of raising.

    The values are ordered by repr: set order follows the hash, which is randomized per process for strings, and
    Hypothesis needs a stable order to replay and shrink (it shrinks towards the first value).
    """
    ordered = sorted(values, key=repr)
    return st.sampled_from(ordered) if ordered else st.nothing()
