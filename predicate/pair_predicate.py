import operator
from dataclasses import dataclass, field
from typing import Callable, Final, override

from predicate.predicate import Predicate


@dataclass
class PairPredicate[T](Predicate[tuple[T, T]]):
    """A predicate that checks a relational constraint between two elements of a pair."""

    fn: Callable[[T, T], bool]
    klass: type = field(default=int)

    def __call__(self, x: tuple[T, T]) -> bool:
        first, second = x
        return self.fn(first, second)

    def __repr__(self) -> str:
        name = getattr(self.fn, "__name__", str(self.fn))
        if self.klass is int:
            return f"pair_p({name})"
        return f"pair_p({name}, {self.klass.__name__})"

    @override
    def explain_failure(self, x: tuple[T, T]) -> dict:
        first, second = x
        name = getattr(self.fn, "__name__", str(self.fn))
        return {"reason": f"pair ({first!r}, {second!r}) does not satisfy {name}"}


def pair_p[T](fn: Callable[[T, T], bool], klass: type = int) -> PairPredicate[T]:
    """Return True if fn(first, second) holds for a pair (first, second), otherwise False."""
    return PairPredicate(fn=fn, klass=klass)


pair_lt_p: Final[PairPredicate] = pair_p(operator.lt)
"""Return True if first < second, otherwise False."""

pair_le_p: Final[PairPredicate] = pair_p(operator.le)
"""Return True if first <= second, otherwise False."""

pair_eq_p: Final[PairPredicate] = pair_p(operator.eq)
"""Return True if first == second, otherwise False."""

pair_ne_p: Final[PairPredicate] = pair_p(operator.ne)
"""Return True if first != second, otherwise False."""

pair_ge_p: Final[PairPredicate] = pair_p(operator.ge)
"""Return True if first >= second, otherwise False."""

pair_gt_p: Final[PairPredicate] = pair_p(operator.gt)
"""Return True if first > second, otherwise False."""
