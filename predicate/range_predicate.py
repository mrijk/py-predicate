from dataclasses import dataclass
from typing import override

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class GeLePredicate[T](Predicate[T]):
    """A predicate class that models the 'lower <= x <= upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower <= x <= self.upper

    def __repr__(self) -> str:
        return f"ge_le_p({self.lower!r}, {self.upper!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x!r} is not greater equal {self.lower!r} and less equal {self.upper!r}"}


@dataclass
class GeLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower <= x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower <= x < self.upper

    def __repr__(self) -> str:
        return f"ge_lt_p({self.lower!r}, {self.upper!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x!r} is not greater equal {self.lower!r} and less than {self.upper!r}"}


@dataclass
class GtLePredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x <= upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x <= self.upper

    def __repr__(self) -> str:
        return f"gt_le_p({self.lower!r}, {self.upper!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "reason": f"{x!r} is not greater than {self.lower!r} and less than or equal to {self.upper!r}",
        }


@dataclass
class GtLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x < self.upper

    def __repr__(self) -> str:
        return f"gt_lt_p({self.lower!r}, {self.upper!r})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x!r} is not greater than {self.lower!r} and less than {self.upper!r}"}
