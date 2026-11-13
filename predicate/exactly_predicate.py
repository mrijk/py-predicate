from dataclasses import dataclass
from typing import Any, Iterable, override

from predicate.predicate import Predicate


@dataclass
class ExactlyPredicate[T](Predicate[T]):
    """Match exactly n instances of the given predicate."""

    n: int
    predicate: Predicate[Any]

    def __call__(self, iterable: Iterable[Any], *, predicates: list[Predicate[Any]], full_match: bool) -> bool:
        from predicate.match_predicate import match

        head, rest = self._split(iterable)
        if len(head) < self.n or not all(self.predicate(item) for item in head):
            return False
        return match(rest, predicates=predicates, full_match=full_match) if predicates else True

    def _split(self, iterable: Iterable[Any]) -> tuple[list[Any], list[Any]]:
        items = list(iterable)
        return items[: self.n], items[self.n :]

    def __repr__(self) -> str:
        return f"exactly({self.n}, {self.predicate!r})"

    @override
    def explain_failure(
        self, iterable: Iterable[T], *, predicates: list[Predicate[Any]], full_match: bool
    ) -> dict[str, Any]:
        from predicate.match_predicate import reason

        head, rest = self._split(iterable)
        for item in head:
            if not self.predicate(item):
                return self.predicate.explain(item)
        if len(head) < self.n:
            return {"reason": f"Not enough items in iterable, expected {self.n}"}
        return reason(rest, predicates=predicates, full_match=full_match)


def exactly_n(n: int, predicate: Predicate[Any]) -> Predicate[Any]:
    """Match exactly n instances of the given predicate."""
    return ExactlyPredicate(n=n, predicate=predicate)
