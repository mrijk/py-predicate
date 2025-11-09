from dataclasses import dataclass
from typing import Iterable, override

from predicate.predicate import Predicate


@dataclass
class OptionalPredicate[T](Predicate[T]):
    """Match 0 or 1 instances of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
        if not iterable:
            return True
        item, *rest = iterable
        if predicates:
            from predicate.match_predicate import match

            return (self.predicate(item) and match(rest, predicates=predicates)) or match(
                iterable, predicates=predicates
            )
        return self.predicate(item)

    def __repr__(self) -> str:
        return f"optional({self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        item, *rest = iterable

        if predicates:
            from predicate.match_predicate import match, reason

            if not self.predicate(item):
                return reason(iterable, predicates=predicates)
            if not match(rest, predicates=predicates):  # type: ignore
                return reason(rest, predicates=predicates)

        return self.predicate.explain_failure(item)


def optional(predicate: Predicate) -> Predicate:
    """Match 0 or 1 instances of the given predicate."""
    return OptionalPredicate(predicate=predicate)
