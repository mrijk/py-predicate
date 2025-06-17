from dataclasses import dataclass
from typing import Final, override

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class LtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lt' (<) predicate."""

    v: ConstrainedT

    def __call__(self, x: T) -> bool:
        return x < self.v

    def __repr__(self) -> str:
        return f"lt_p({self.v!r})"

    @override
    def get_klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not less than {self.v!r}"}


def lt_p(v: ConstrainedT) -> LtPredicate[ConstrainedT]:
    """Return True if the value is less than the constant, otherwise False."""
    return LtPredicate(v=v)


neg_p: Final[LtPredicate] = lt_p(0)
"""Returns True of the value is negative, otherwise False."""
