from dataclasses import dataclass
from typing import Any, Callable, override

from predicate.helpers import fn_name
from predicate.predicate import Explanation, Predicate


@dataclass
class CompPredicate[S, T](Predicate[S]):
    """A predicate class that transforms the input according to a function and then evaluates the predicate."""

    fn: Callable[[S], T]
    predicate: Predicate[T]

    @override
    def __call__(self, x: S) -> bool:
        return self.predicate(self.fn(x))

    @override
    def __repr__(self) -> str:
        return f"comp_p({fn_name(self.fn)}, {self.predicate!r})"

    @override
    def __contains__(self, predicate: Predicate[Any]) -> bool:
        return predicate in self.predicate

    @override
    def explain_failure(self, x: S) -> Explanation:
        return {"reason": self.predicate.explain(x)}


def comp_p[S, T](fn: Callable[[S], T], predicate: Predicate[T]) -> CompPredicate[S, T]:
    """Return a predicate, composed of a function and another predicate."""
    return CompPredicate(fn=fn, predicate=predicate)
