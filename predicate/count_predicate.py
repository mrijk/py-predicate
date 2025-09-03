from dataclasses import dataclass
from typing import Iterable, override

from more_itertools import ilen

from predicate.predicate import Predicate


@dataclass
class CountPredicate[T](Predicate[T]):
    """A predicate class that models the 'length' predicate."""

    predicate: Predicate[T]
    length_p: Predicate[int]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return self.length_p(ilen(x for x in iterable if self.predicate(x)))

    def __repr__(self) -> str:
        return f"count_p({self.predicate!r}, {self.length_p!r})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        actual_length = ilen(x for x in iterable if self.predicate(x))
        return {"reason": f"Expected count {self.length_p!r}, actual: {actual_length}"}


def count_p[T](predicate: Predicate[T], length_p: Predicate[int]) -> Predicate[T]:
    """Return True if length of iterable is equal to value, otherwise False."""
    return CountPredicate(predicate=predicate, length_p=length_p)


# is_empty_p: Final[Predicate[Iterable]] = has_length_p(zero_p)
# """Predicate that returns True if the iterable is empty, otherwise False."""
#
# is_not_empty_p: Final[Predicate[Iterable]] = has_length_p(pos_p)
# """Predicate that returns True if the iterable is not empty, otherwise False."""
