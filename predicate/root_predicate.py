import inspect
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from predicate.predicate import Predicate
from predicate.this_predicate import find_in_locals


@dataclass
class RootPredicate[T](Predicate[T]):
    """A predicate class that lazily references the root predicate."""

    @cached_property
    def root_predicate(self) -> Predicate:
        return find_root_predicate(self.frame, self)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        return self.root_predicate(x)

    def __repr__(self) -> str:
        return "root_p"


def find_root_predicate(start_frame, predicate: Predicate) -> Predicate:
    for frame in get_frames(start_frame):
        locals = reversed(frame.f_locals.items())
        if found := find_in_locals(locals, predicate):  # type: ignore
            return found
    raise ValueError("Could not find 'root' predicate")


def get_frames(frame) -> Iterator:
    if frame:
        yield frame
        yield from get_frames(frame.f_back)
