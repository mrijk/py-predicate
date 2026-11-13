"""Hypothesis integration. Requires the optional dependency: pip install py-predicate[hypothesis]."""

from predicate.integrations.hypothesis.strategies import from_predicate, given_predicate

__all__ = ["from_predicate", "given_predicate"]
