from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, override

from more_itertools import first

from predicate.helpers import dict_predicates_repr
from predicate.predicate import Predicate


@dataclass
class StructPredicate[T](Predicate[T]):
    """A predicate class that models the struct_p predicate."""

    required: dict[str, Predicate]
    optional: dict[str, Predicate]

    def __call__(self, x: Any) -> bool:
        if not isinstance(x, Mapping):
            return False

        if set(x) - set(self.required) - set(self.optional):
            return False

        for key, predicate in self.required.items():
            if key not in x:
                return False
            if not predicate(x[key]):
                return False

        for key, predicate in self.optional.items():
            if value := x.get(key, None):
                if not predicate(value):
                    return False

        return True

    def __repr__(self) -> str:
        return (
            f"struct_p(required={dict_predicates_repr(self.required)}, optional={dict_predicates_repr(self.optional)})"
        )

    @override
    def explain_failure(self, x: Any, *args, **kwargs) -> dict:
        if not isinstance(x, Mapping):
            return {"reason": f"{x} is not an instance of a Mapping"}

        if additional := first(set(x) - set(self.required) - set(self.optional), None):
            return {"reason": f"Field `{additional}` is unknown"}

        for key, predicate in self.required.items():
            if key not in x:
                return {"reason": f"Required field `{key}` missing"}
            value = x[key]
            if not predicate(value):
                return {
                    "key": key,
                    "value": value,
                    "reason": f"Value '{value}' for key '{key}' doesn't satisfy predicate {predicate!r}",
                }

        return {"reason": "Unknown"}


def is_struct_p(
    required: dict[str, Predicate] | None = None, optional: dict[str, Predicate] | None = None
) -> Predicate:
    """Return True if value matches the defined struct, otherwise False."""
    return StructPredicate(required=required or {}, optional=optional or {})
