from dataclasses import dataclass
from typing import Iterable, override

from predicate.predicate import Predicate


@dataclass
class ExactlyPredicate[T](Predicate[T]):
    """Match exactly n instances of the given predicate."""

    n: int
    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate], full_match: bool) -> bool:
        from predicate.match_predicate import match

        rest = iterable
        for _ in range(self.n):
            if not rest:
                return False

            item, *rest = rest
            if not self.predicate(item):
                return False
        return match(rest, predicates=predicates, full_match=full_match) if predicates else True

    def __repr__(self) -> str:
        return f"exactly({self.n}, {self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate], full_match: bool) -> dict:  # type: ignore
        from predicate.match_predicate import reason

        rest = iterable
        for _ in range(self.n):
            if not rest:
                return {"reason": f"Not enough items in iterable, expected {self.n}"}

            item, *rest = rest
            if not self.predicate(item):
                return self.predicate.explain(item)

        return reason(rest, predicates=predicates, full_match=full_match)


def exactly_n(n: int, predicate: Predicate) -> Predicate:
    """Match exactly n instances of the given predicate."""
    return ExactlyPredicate(n=n, predicate=predicate)
