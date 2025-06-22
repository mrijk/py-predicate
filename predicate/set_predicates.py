from dataclasses import dataclass

from predicate.predicate import Predicate


@dataclass
class IsSubsetPredicate[T](Predicate[T]):
    """A predicate class that models the 'subset' predicate."""

    v: set[T]

    def __call__(self, v: set[T]) -> bool:
        return v <= self.v

    def __repr__(self) -> str:
        return f"is_subset_p({self.v})"


@dataclass
class IsRealSubsetPredicate[T](Predicate[T]):
    """A predicate class that models the 'real subset' predicate."""

    v: set[T]

    def __call__(self, v: set[T]) -> bool:
        return v < self.v

    def __repr__(self) -> str:
        return f"is_real_subset_p({self.v})"


@dataclass
class IsSupersetPredicate[T](Predicate[T]):
    """A predicate class that models the 'superset' predicate."""

    v: set[T]

    def __call__(self, v: set[T]) -> bool:
        return v >= self.v

    def __repr__(self) -> str:
        return f"is_superset_p({self.v})"


@dataclass
class IsRealSupersetPredicate[T](Predicate[T]):
    """A predicate class that models the 'real superset' predicate."""

    v: set[T]

    def __call__(self, v: set[T]) -> bool:
        return v > self.v

    def __repr__(self) -> str:
        return f"is_real_superset_p({self.v})"


def is_subset_p[T](v: set[T]) -> IsSubsetPredicate[T]:
    """Return True if the value is a subset, otherwise False."""
    return IsSubsetPredicate(v)


def is_real_subset_p[T](v: set[T]) -> IsRealSubsetPredicate[T]:
    """Return True if the value is a real subset, otherwise False."""
    return IsRealSubsetPredicate(v)


def is_superset_p[T](v: set[T]) -> IsSupersetPredicate[T]:
    """Return True if the value is a superset, otherwise False."""
    return IsSupersetPredicate(v)


def is_real_superset_p[T](v: set[T]) -> IsRealSupersetPredicate[T]:
    """Return True if the value is a real superset, otherwise False."""
    return IsRealSupersetPredicate(v)
