from dataclasses import dataclass
from typing import Iterable, override

from predicate import always_true_p
from predicate.predicate import Predicate


@dataclass
class StarPredicate[T](Predicate[T]):
    """Match any instances of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate], full_match: bool) -> bool:
        from predicate.match_predicate import match

        if not iterable:
            return not predicates
        item, *rest = iterable
        if self.predicate(item):
            if self(rest, predicates=predicates, full_match=full_match):
                return True
            if predicates:
                matched = match(rest, predicates=predicates, full_match=full_match)
                return (
                    match(iterable, predicates=predicates, full_match=full_match) if not matched else True
                )  # backtrack
        return match(iterable, predicates=predicates, full_match=full_match) if predicates else False

    def __repr__(self) -> str:
        return f"star({self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate], full_match: bool) -> dict:  # type: ignore
        return {"reason": f"tbd {self.predicate!r}"}


def star(predicate: Predicate) -> Predicate:
    """Match any instances of the given predicate."""
    return StarPredicate(predicate=predicate)


wildcard = star(always_true_p)
