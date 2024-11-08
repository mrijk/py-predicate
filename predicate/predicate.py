from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Final, Iterable, Self, cast
from uuid import UUID


@dataclass
class Predicate[T]:
    """An abstract class to represent a predicate."""

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    def __and__(self, predicate: "Predicate") -> "Predicate":
        return cast(Self, AndPredicate(left=self, right=predicate))

    def __or__(self, predicate: "Predicate") -> "Predicate":
        return cast(Self, OrPredicate(left=self, right=predicate))

    def __xor__(self, predicate: "Predicate") -> "Predicate":
        return cast(Self, XorPredicate(left=self, right=predicate))

    def __invert__(self) -> "Predicate":
        return cast(Self, NotPredicate(predicate=self))


@dataclass
class FnPredicate[T](Predicate[T]):
    """A predicate class that can hold a function."""

    predicate_fn: Callable[[T], bool]

    def __call__(self, x: T) -> bool:
        return self.predicate_fn(x)


@dataclass
class AndPredicate[T](Predicate[T]):
    """A predicate class that models the 'and' predicate.

    ```

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the AndPredicate
    right: Predicate[T]
        right predicate of the AndPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) and self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case AndPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False


@dataclass
class NotPredicate[T](Predicate[T]):
    """A predicate class that models the 'not' predicate.

    ```

    Attributes
    ----------
    predicate: Predicate[T]
        predicate that will be negated


    """

    predicate: Predicate[T]

    def __call__(self, x: T) -> bool:
        return not self.predicate(x)


@dataclass
class OrPredicate[T](Predicate[T]):
    """A predicate class that models the 'or' predicate.

    ```

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the OrPredicate
    right: Predicate[T]
        right predicate of the OrPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) or self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case OrPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False


@dataclass
class XorPredicate[T](Predicate[T]):
    """A predicate class that models the 'xor' predicate.

    ```

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the XorPredicate
    right: Predicate[T]
        right predicate of the XorPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) ^ self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case XorPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False


@dataclass
class InPredicate[T](Predicate[T]):
    """A predicate class that models the 'in' predicate."""

    v: set[T]

    def __init__(self, v: Iterable[T]):
        self.v = set(v)

    def __call__(self, x: T) -> bool:
        return x in self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, InPredicate) else False


@dataclass
class NotInPredicate[T](Predicate[T]):
    """A predicate class that models the 'not in' predicate."""

    v: set[T]

    def __init__(self, v: Iterable[T]):
        self.v = set(v)

    def __call__(self, x: T) -> bool:
        return x not in self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, NotInPredicate) else False


@dataclass
class EqPredicate[T](Predicate[T]):
    """A predicate class that models the 'eq' (=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x == self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, EqPredicate) else False


@dataclass
class NePredicate[T](Predicate[T]):
    """A predicate class that models the 'ne' (!=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x != self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, NePredicate) else False


@dataclass
class GePredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'ge' (>=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x >= self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, GePredicate) else False


@dataclass
class GtPredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'gt' (>) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x > self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, GtPredicate) else False


@dataclass
class LePredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'le' (<=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x <= self.v

    def __eq__(self, other: object) -> bool:
        return self.v == other.v if isinstance(other, LePredicate) else False


@dataclass
class LtPredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'lt' (<) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x < self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LtPredicate) and self.v == other.v


@dataclass
class AllPredicate[T](Predicate[T]):
    """A predicate class that models the 'all' predicate."""

    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iter)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AllPredicate) and self.predicate == other.predicate


@dataclass
class AnyPredicate[T](Predicate[T]):
    """A predicate class that models the 'any' predicate."""

    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return any(self.predicate(x) for x in iter)

    def __eq__(self, other: object) -> bool:
        return self.predicate == other.predicate if isinstance(other, AnyPredicate) else False


@dataclass
class IsEmptyPredicate[T](Predicate[T]):
    """A predicate class that models the 'empty' predicate."""

    def __call__(self, iter: Iterable[T]) -> bool:
        return len(list(iter)) == 0

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsEmptyPredicate)


@dataclass
class IsInstancePredicate[T](Predicate[T]):
    """A predicate class that models the 'isinstance' predicate."""

    klass: type | tuple

    def __call__(self, x: object) -> bool:
        return isinstance(x, self.klass)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsInstancePredicate) and self.klass == other.klass


@dataclass
class AlwaysTruePredicate(Predicate):
    """A predicate class that models the 'True' predicate."""

    def __call__(self, *args, **kwargs):
        return True

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AlwaysTruePredicate)


@dataclass
class AlwaysFalsePredicate(Predicate):
    """A predicate class that models the 'False' predicate."""

    def __call__(self, *args, **kwargs):
        return False

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AlwaysFalsePredicate)


@dataclass
class IsNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is none' predicate."""

    def __call__(self, x: T) -> bool:
        return x is None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsNonePredicate)


@dataclass
class IsNotNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is not none' predicate."""

    def __call__(self, x: T) -> bool:
        return x is not None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsNotNonePredicate)


always_true_p: Final[AlwaysTruePredicate] = AlwaysTruePredicate()
"""Predicate that always evaluates to True."""

always_false_p: Final[AlwaysFalsePredicate] = AlwaysFalsePredicate()
"""Predicate that always evaluates to False."""

is_empty_p: Final[IsEmptyPredicate] = IsEmptyPredicate()
"""Predicate that returns True if the iterable is empty, otherwise False."""
