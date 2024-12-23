import inspect
from collections.abc import Iterator
from dataclasses import dataclass
from functools import cached_property

from predicate.predicate import Predicate


@dataclass
class RootPredicate[T](Predicate[T]):
    """A predicate class that lazily references the root predicate."""

    @cached_property
    def root_predicate(self) -> Predicate | None:
        return find_root_predicate(self.frame, self)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        if self.root_predicate:
            return self.root_predicate(x)
        raise ValueError(f"Could not find 'root' predicate {self}")

    def __repr__(self) -> str:
        return "root_p"


def find_root_predicate(start_frame, predicate: Predicate) -> Predicate | None:
    for frame in get_frames(start_frame):
        for key, value in reversed(frame.f_locals.items()):
            if isinstance(value, Predicate) and value != predicate and key != "self":
                if predicate in value:
                    return value
    return None


def get_frames(frame) -> Iterator:
    if frame:
        yield frame
        yield from get_frames(frame.f_back)
