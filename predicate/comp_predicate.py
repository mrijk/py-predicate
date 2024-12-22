from dataclasses import dataclass
from typing import Callable, override

from predicate.predicate import Predicate


@dataclass
class CompPredicate[S, T](Predicate[T]):
    """A predicate class that transforms the input according to a function and then evaluates the predicate."""

    fn: Callable[[S], T]
    predicate: Predicate[T]

    def __call__(self, x: S) -> bool:
        return self.predicate(self.fn(x))

    def __repr__(self) -> str:
        return f"comp_p({repr(self.predicate)})"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate in self.predicate

    @override
    def explain_failure(self, x: S) -> dict:
        return {"reason": self.predicate.explain(x)}
