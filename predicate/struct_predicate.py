from collections.abc import Iterator, Mapping
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

        return not any(self._failures(x))

    def _failures(self, x: Mapping) -> Iterator[dict]:
        if additional := set(x) - set(self.required) - set(self.optional):
            yield {"reason": f"Field `{first(additional)}` is unknown"}

        for key, predicate in self.required.items():
            if key not in x:
                yield {"reason": f"Required field `{key}` missing"}
            elif not predicate(value := x[key]):
                yield value_failure(key, value, predicate)

        for key, predicate in self.optional.items():
            if key in x and not predicate(value := x[key]):
                yield value_failure(key, value, predicate)

    def __repr__(self) -> str:
        return (
            f"struct_p(required={dict_predicates_repr(self.required)}, optional={dict_predicates_repr(self.optional)})"
        )

    @override
    def explain_failure(self, x: Any, *args, **kwargs) -> dict:
        if not isinstance(x, Mapping):
            return {"reason": f"{x} is not an instance of a Mapping"}

        return first(self._failures(x), {"reason": "Unknown"})


def value_failure(key: str, value: Any, predicate: Predicate) -> dict:
    return {
        "key": key,
        "value": value,
        "reason": f"Value '{value}' for key '{key}' doesn't satisfy predicate {predicate!r}",
    }


def is_struct_p(
    required: dict[str, Predicate] | None = None, optional: dict[str, Predicate] | None = None
) -> Predicate:
    """Return True if value matches the defined struct, otherwise False."""
    return StructPredicate(required=required or {}, optional=optional or {})
