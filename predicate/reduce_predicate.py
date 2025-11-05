from dataclasses import dataclass
from typing import Callable, Iterable

from predicate.predicate import Predicate


@dataclass
class ReducePredicate[T](Predicate[T]):
    """A predicate class that models the 'reduce' predicate."""

    fn: Callable
    initial: T

    def __call__(self, iterable: Iterable[T]) -> bool:
        acc = self.initial
        for x in iterable:
            acc, predicate = self.fn(acc, x)
            if not predicate(x):
                return False
        return True


def reduce_p[T](fn: Callable, initial: T) -> Predicate[T]:
    """Return True if length of iterable is equal to value, otherwise False."""
    return ReducePredicate(fn=fn, initial=initial)
