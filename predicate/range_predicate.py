from dataclasses import dataclass

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


@dataclass
class GeLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower <= x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower <= x < self.upper

    def __repr__(self) -> str:
        return f"ge_lt_p({self.lower}, {self.upper})"


@dataclass
class GtLePredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x <= upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x <= self.upper

    def __repr__(self) -> str:
        return f"gt_le_p({self.lower}, {self.upper})"


@dataclass
class GtLtPredicate[T](Predicate[T]):
    """A predicate class that models the 'lower < x < upper' predicate."""

    lower: ConstrainedT
    upper: ConstrainedT

    def __call__(self, x: T) -> bool:
        return self.lower < x < self.upper

    def __repr__(self) -> str:
        return f"gt_lt_p({self.lower}, {self.upper})"
