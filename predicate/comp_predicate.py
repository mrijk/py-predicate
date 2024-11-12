from dataclasses import dataclass
from typing import Callable

from predicate import Predicate


@dataclass
class CompPredicate[S, T](Predicate[T]):
    """A predicate class that transforms the input according to a function and then evaluates the predicate."""

    fn: Callable[[S], T]
    predicate: Predicate[T]

    def __call__(self, x: S) -> bool:
        return self.predicate(self.fn(x))
