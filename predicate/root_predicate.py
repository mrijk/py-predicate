import inspect
from dataclasses import dataclass
from functools import cached_property
from types import FrameType
from typing import Any, Iterator

from predicate.predicate import Predicate
from predicate.this_predicate import find_in_locals


@dataclass
class RootPredicate[T](Predicate[T]):
    """A predicate class that lazily references the root predicate."""

    @cached_property
    def root_predicate(self) -> Predicate[Any]:
        return find_root_predicate(self.frame, self)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        return self.root_predicate(x)

    def __repr__(self) -> str:
        return "root_p"


def find_root_predicate(start_frame: FrameType | None, predicate: Predicate[Any]) -> Predicate[Any]:
    for frame in _get_frames(start_frame):
        locals = reversed(frame.f_locals.items())
        if found := find_in_locals(locals, predicate):
            return found
    raise ValueError("Could not find 'root' predicate")


def _get_frames(frame: FrameType | None) -> Iterator[Any]:
    if frame:
        yield frame
        yield from _get_frames(frame.f_back)
