from dataclasses import dataclass
from typing import Any, Callable, Iterable, Iterator, override

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

    @override
    def consumes(self, iterable: Iterable[Any]) -> Iterator[int]:
        yield 0


def tee_p[T](fn: Callable[[T], None]) -> Predicate[T]:
    """Execute fn as a side effect and always return True."""
    return TeePredicate(fn=fn)
