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
        return f"ge_le_p({self.lower}, {self.upper})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not greater equal {self.lower} and less equal {self.upper}"}


@dataclass
class GeLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower <= x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower <= x < self.upper

    def __repr__(self) -> str:
        return f"ge_lt_p({self.lower}, {self.upper})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not greater equal {self.lower} and less than {self.upper}"}


@dataclass
class GtLePredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x <= upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x <= self.upper

    def __repr__(self) -> str:
        return f"gt_le_p({self.lower}, {self.upper})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "reason": f"{x} is not greater than {self.lower} and less than or equal to {self.upper}",
        }


@dataclass
class GtLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x < self.upper

    def __repr__(self) -> str:
        return f"gt_lt_p({self.lower}, {self.upper})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not greater than {self.lower} and less than {self.upper}"}
