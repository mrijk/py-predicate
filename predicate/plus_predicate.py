from dataclasses import dataclass
from typing import Iterable, override

from predicate.predicate import Predicate


@dataclass
class PlusPredicate[T](Predicate[T]):
    """Match at least one instance of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate], full_match: bool) -> bool:
        from predicate import star

        if not iterable:
            return False

        item, *rest = iterable
        return self.predicate(item) and star(self.predicate)(rest, predicates=predicates, full_match=full_match)

    def __repr__(self) -> str:
        return f"plus({self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate], full_match: bool) -> dict:  # type: ignore
        if not iterable:
            return {"reason": f"Iterable should have at least one element to match against {self.predicate!r}"}

        item, *rest = iterable
        if not self.predicate(item):
            return {"reason": f"tbd {self.predicate!r}"}

        return {"reason": f"`{self.predicate!r}`"}


def plus(predicate: Predicate) -> Predicate:
    """Match at least one instance of the given predicate."""
    return PlusPredicate(predicate=predicate)
