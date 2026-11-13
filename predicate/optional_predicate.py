from dataclasses import dataclass
from typing import Any, Iterable, override

from predicate.predicate import Predicate


@dataclass
class OptionalPredicate[T](Predicate[T]):
    """Match 0 or 1 instances of the given predicate."""

    predicate: Predicate[Any]

    def __call__(self, iterable: Iterable[Any], *, predicates: list[Predicate[Any]], full_match: bool) -> bool:
        if not iterable:
            return True
        item, *rest = iterable
        if predicates:
            from predicate.match_predicate import match

            return (self.predicate(item) and match(rest, predicates=predicates, full_match=full_match)) or match(
                iterable, predicates=predicates, full_match=full_match
            )
        return self.predicate(item)

    def __repr__(self) -> str:
        return f"optional({self.predicate!r})"

    @override
    def explain_failure(
        self, iterable: Iterable[T], *, predicates: list[Predicate[Any]], full_match: bool
    ) -> dict[str, Any]:
        item, *rest = iterable

        if predicates:
            from predicate.match_predicate import match, reason

            if not self.predicate(item):
                return reason(iterable, predicates=predicates, full_match=full_match)
            if not match(rest, predicates=predicates, full_match=full_match):
                return reason(rest, predicates=predicates, full_match=full_match)

        return self.predicate.explain_failure(item)


def optional(predicate: Predicate[Any]) -> Predicate[Any]:
    """Match 0 or 1 instances of the given predicate."""
    return OptionalPredicate(predicate=predicate)
