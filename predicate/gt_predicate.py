from dataclasses import dataclass
from typing import Final, override

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class GtPredicate[T](Predicate[T]):
    """A predicate class that models the 'gt' (>) predicate."""

    v: ConstrainedT

    def __call__(self, x: T) -> bool:
        return x > self.v

    def __repr__(self) -> str:
        return f"gt_p({self.v!r})"

    @override
    def get_klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not greater than {self.v!r}"}


def gt_p(v: ConstrainedT) -> GtPredicate[ConstrainedT]:
    """Return True if the value is greater than the constant, otherwise False."""
    return GtPredicate(v=v)


pos_p: Final[GtPredicate] = gt_p(0)
"""Returns True of the value is positive, otherwise False."""
