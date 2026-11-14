"""Short import path for the Hypothesis integration. Requires: pip install py-predicate[hypothesis]."""

from predicate.integrations.hypothesis import from_predicate, from_spec, given_predicate, given_spec

__all__ = ["from_predicate", "from_spec", "given_predicate", "given_spec"]
