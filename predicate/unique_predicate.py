from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any, Final, override

from predicate.predicate import Explanation, Predicate


@dataclass
class UniquePredicate[T](Predicate[Iterable[T]]):
    """Check whether all elements have distinct hashable keys."""

    key: Callable[[T], object] | None = None

    def __call__(self, values: Iterable[T]) -> bool:
        return self._failure_reason(values) is None

    def __repr__(self) -> str:
        return "unique_p" if self.key is None else f"unique_by_p({self.key_name})"

    @property
    def key_name(self) -> str:
        return getattr(self.key, "__name__", str(self.key))

    def _failure_reason(self, values: Iterable[T]) -> str | None:
        seen: dict[object, int] = {}
        for index, value in enumerate(values):
            key = value if self.key is None else self.key(value)
            try:
                first = seen.setdefault(key, index)
            except TypeError:
                return f"Unhashable key {key!r} at index {index}"
            if first != index:
                return f"Duplicate key {key!r} at indices {first} and {index}"
        return None

    @override
    def _explain(self, values: Iterable[T]) -> Explanation:
        reason = self._failure_reason(values)
        return {"result": True} if reason is None else {"result": False, "reason": reason}

    @override
    def explain_failure(self, values: Iterable[T]) -> Explanation:
        return {"reason": self._failure_reason(values)}


unique_p: Final[UniquePredicate[Any]] = UniquePredicate()
"""Predicate that checks for distinct hashable elements."""


def unique_by_p[T](key: Callable[[T], object]) -> UniquePredicate[T]:
    """Return a predicate that checks for distinct hashable keys."""
    return UniquePredicate(key)
