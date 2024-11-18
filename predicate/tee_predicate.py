from collections.abc import Callable
from dataclasses import dataclass

from predicate.predicate import Predicate


@dataclass
class TeePredicate[T](Predicate[T]):
    """A predicate class that captures a side effect, and always returns True."""

    fn: Callable[[T], None]

    def __call__(self, x: T) -> bool:
        self.fn(x)
        return True

    def __repr__(self) -> str:
        return "tee_p"
