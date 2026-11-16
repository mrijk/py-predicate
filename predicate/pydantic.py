"""Short import path for the Pydantic integration. Requires: pip install py-predicate[pydantic]."""

from predicate.integrations.pydantic import PredicateValidator, predicate_to_json_schema

__all__ = ["PredicateValidator", "predicate_to_json_schema"]
