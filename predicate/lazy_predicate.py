import inspect
from dataclasses import dataclass
from functools import cached_property

from predicate.predicate import Predicate


@dataclass
class LazyPredicate[T](Predicate[T]):
    """A predicate class that lazily references another predicate by name."""

    ref: str

    @cached_property
    def predicate(self) -> Predicate | None:
        return find_predicate_by_ref(self.frame, self.ref)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        if self.predicate:
            return self.predicate(x)
        raise ValueError(f"Could not find predicate with reference {self.ref}")

    def __repr__(self) -> str:
        return f'lazy_p("{self.ref}")'


def find_predicate_by_ref(frame, ref: str) -> Predicate | None:
    for key, value in frame.f_locals.items():
        if key == ref:
            return value
    if next_frame := frame.f_back:
        return find_predicate_by_ref(next_frame, ref)
    return None
