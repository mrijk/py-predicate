from dataclasses import dataclass
from typing import Any

from predicate.predicate import Predicate


@dataclass
class MaybeOptimized[T]:
    """Base class to hold optimized predicate."""

    predicate: Predicate[T] | None = None


@dataclass
class Optimized[T](MaybeOptimized[Any]):
    """Contains predicate if optimized."""

    predicate: Predicate[T]


@dataclass
class NotOptimized(MaybeOptimized[Any]):
    """Not optimized."""

    pass
