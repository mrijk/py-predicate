from dataclasses import dataclass
from typing import Final, override

from predicate.predicate import Predicate


@dataclass
class EqPredicate[T](Predicate[T]):
    """A predicate class that models the 'eq' (=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x == self.v

    def __repr__(self) -> str:
        return f"eq_p({self.v!r})"

    @override
    def get_klass(self) -> type:
        return type(self.v)

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not equal to {self.v!r}"}


def eq_p[T](v: T) -> EqPredicate[T]:
    """Return True if the value is equal to the constant, otherwise False."""
    return EqPredicate(v=v)


zero_p: Final[EqPredicate] = eq_p(0)
"""Returns True of the value is zero, otherwise False."""

eq_true_p: Final[EqPredicate] = eq_p(True)
"""Returns True if the value is True, otherwise False."""

eq_false_p: Final[EqPredicate] = eq_p(False)
"""Returns True if the value is False, otherwise False."""
