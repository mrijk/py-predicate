from dataclasses import dataclass
from typing import Iterable, override

from predicate.predicate import Predicate


@dataclass
class RepeatPredicate[T](Predicate[T]):
    """Match exactly m to n instances of the given predicate."""

    m: int
    n: int
    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
        from predicate import exactly_n

        for n in range(self.n, self.m - 1, -1):
            f = exactly_n(n, self.predicate)
            if f(iterable, predicates=predicates):
                return True
        return False

    def __repr__(self) -> str:
        return f"repeat({self.m}, {self.n}, {self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        return {"reason": f"Expected between {self.m} and {self.n} matches of predicate `{self.predicate!r}`"}


def repeat(m: int, n: int, predicate: Predicate) -> Predicate:
    """Match exactly m to n instances of the given predicate."""
    return RepeatPredicate(m=m, n=n, predicate=predicate)
