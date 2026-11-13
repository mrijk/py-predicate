import inspect
from dataclasses import dataclass
from functools import cached_property
from types import FrameType
from typing import Any, cast

from predicate.predicate import Predicate


@dataclass
class LazyPredicate[T](Predicate[T]):
    """A predicate class that lazily references another predicate by name."""

    ref: str

    @cached_property
    def predicate(self) -> Predicate[Any] | None:
        return find_predicate_by_ref(self.frame, self.ref)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        if self.predicate:
            return self.predicate(x)
        raise ValueError(f"Could not find predicate with reference {self.ref}")

    def __repr__(self) -> str:
        return f'lazy_p("{self.ref}")'


def find_predicate_by_ref(frame: FrameType | None, ref: str) -> Predicate[Any] | None:
    if frame is None:
        return None
    for key, value in frame.f_locals.items():
        if key == ref:
            return cast(Predicate[Any], value)
    return find_predicate_by_ref(frame.f_back, ref)


def lazy_p(ref: str) -> LazyPredicate[Any]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return LazyPredicate(ref=ref)
