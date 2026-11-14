"""Hypothesis integration. Requires the optional dependency: pip install py-predicate[hypothesis]."""

from predicate.integrations.hypothesis.from_spec import from_spec, given_spec
from predicate.integrations.hypothesis.strategies import from_predicate, given_predicate

__all__ = ["from_predicate", "from_spec", "given_predicate", "given_spec"]
