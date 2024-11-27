from dataclasses import dataclass

from predicate.predicate import ConstrainedT, Predicate


@dataclass
class GeLePredicate[T](Predicate[T]):
    """A predicate class that models the 'lower <= x <= upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower <= x <= self.upper

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GeLePredicate) and self.lower == other.lower and self.upper == other.upper

    def __repr__(self) -> str:
        return f"ge_le_p({self.lower}, {self.upper})"


@dataclass
class GeLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower <= x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower <= x < self.upper

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GeLtPredicate) and self.lower == other.lower and self.upper == other.upper

    def __repr__(self) -> str:
        return f"ge_lt_p({self.lower}, {self.upper})"


@dataclass
class GtLePredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x <= upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x <= self.upper

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GtLePredicate) and self.lower == other.lower and self.upper == other.upper

    def __repr__(self) -> str:
        return f"gt_le_p({self.lower}, {self.upper})"


@dataclass
class GtLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x < self.upper

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GtLtPredicate) and self.lower == other.lower and self.upper == other.upper

    def __repr__(self) -> str:
        return f"gt_lt_p({self.lower}, {self.upper})"
