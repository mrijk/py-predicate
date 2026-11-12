from dataclasses import dataclass
from typing import Any, Iterable, override

from predicate.predicate import Predicate


@dataclass
class PlusPredicate[T](Predicate[T]):
    """Match at least one instance of the given predicate."""

    predicate: Predicate[Any]

    def __call__(self, iterable: Iterable[Any], *, predicates: list[Predicate[Any]], full_match: bool) -> bool:
        from predicate import star

        if not iterable:
            return False

        item, *rest = iterable
        return self.predicate(item) and star(self.predicate)(rest, predicates=predicates, full_match=full_match)

    def __repr__(self) -> str:
        return f"plus({self.predicate!r})"

    @override
    def explain_failure(
        self, iterable: Iterable[T], *, predicates: list[Predicate[Any]], full_match: bool
    ) -> dict[str, Any]:
        if not iterable:
            return {"reason": f"Iterable should have at least one element to match against {self.predicate!r}"}

        item, *rest = iterable
        if not self.predicate(item):
            return {"reason": f"tbd {self.predicate!r}"}

        return {"reason": f"`{self.predicate!r}`"}


def plus(predicate: Predicate[Any]) -> Predicate[Any]:
    """Match at least one instance of the given predicate."""
    return PlusPredicate(predicate=predicate)
