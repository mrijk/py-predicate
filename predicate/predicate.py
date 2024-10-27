from dataclasses import dataclass
from typing import Callable, Iterable, Self, cast


@dataclass
class Predicate[T]:
    def __call__(self, *args, **kwargs) -> bool: ...

    def __and__(self, predicate: "Predicate") -> "Predicate":
        return cast(Self, AndPredicate(left=self, right=predicate))

    def __or__(self, predicate: "Predicate") -> "Predicate":
        return cast(Self, OrPredicate(left=self, right=predicate))

    def __xor__(self, predicate: "Predicate") -> "Predicate":
        return cast(Self, XorPredicate[T](left=self, right=predicate))

    def __invert__(self) -> "Predicate":
        return cast(Self, NotPredicate(predicate=self))


@dataclass
class FnPredicate[T](Predicate[T]):
    predicate_fn: Callable[[T], bool]

    def __call__(self, x: T) -> bool:
        return self.predicate_fn(x)


@dataclass
class AndPredicate[T](Predicate[T]):
    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) and self.right(x)


@dataclass
class NotPredicate[T](Predicate[T]):
    predicate: Predicate[T]

    def __call__(self, x: T) -> bool:
        return not self.predicate(x)


@dataclass
class OrPredicate[T](Predicate[T]):
    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) or self.right(x)


@dataclass
class XorPredicate[T](Predicate[T]):
    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) ^ self.right(x)


@dataclass
class InPredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x in self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, InPredicate) else False


@dataclass
class EqPredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x == self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, EqPredicate) else False


@dataclass
class NePredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x != self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, NePredicate) else False


@dataclass
class GePredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x >= self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, GePredicate) else False


@dataclass
class GtPredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x > self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, GtPredicate) else False


@dataclass
class LePredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x <= self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, LePredicate) else False


@dataclass
class LtPredicate[T](Predicate[T]):
    v: T

    def __call__(self, x: T) -> bool:
        return x < self.v

    def __eq__(self, other: Self) -> bool:
        return self.v == other.v if isinstance(other, LtPredicate) else False


@dataclass
class AllPredicate[T](Predicate[T]):
    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iter)

    def __eq__(self, other: Self) -> bool:
        return self.predicate == other.predicate if isinstance(other, AllPredicate) else False


@dataclass
class AnyPredicate[T](Predicate[T]):
    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return any(self.predicate(x) for x in iter)

    def __eq__(self, other: Self) -> bool:
        return self.predicate == other.predicate if isinstance(other, AnyPredicate) else False


@dataclass
class IsEmptyPredicate[T](Predicate[T]):
    def __call__(self, iter: Iterable[T]) -> bool:
        return len(list(iter)) == 0

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, IsEmptyPredicate)


@dataclass
class IsInstancePredicate[T](Predicate[T]):
    klass: type | tuple

    def __call__(self, x: object) -> bool:
        return isinstance(x, self.klass)

    def __eq__(self, other: Self) -> bool:
        return self.klass == other.klass if isinstance(other, IsInstancePredicate) else False


def get_as_not_predicate[T](predicate: Predicate[T]) -> NotPredicate[T] | None:
    return cast(NotPredicate, predicate) if isinstance(predicate, NotPredicate) else None


def get_as_and_predicate[T](predicate: Predicate[T]) -> AndPredicate[T] | None:
    return cast(AndPredicate, predicate) if isinstance(predicate, AndPredicate) else None


def get_as_or_predicate[T](predicate: Predicate[T]) -> OrPredicate[T] | None:
    return cast(OrPredicate, predicate) if isinstance(predicate, OrPredicate) else None


@dataclass
class AlwaysTruePredicate(Predicate):
    def __call__(self, *args, **kwargs):
        return True

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, AlwaysTruePredicate)


@dataclass
class AlwaysFalsePredicate(Predicate):
    def __call__(self, *args, **kwargs):
        return False

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, AlwaysFalsePredicate)


@dataclass
class IsNonePredicate[T](Predicate[T]):
    def __call__(self, x: T) -> bool:
        return x is None

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, IsInstancePredicate)


@dataclass
class IsNotNonePredicate[T](Predicate[T]):
    def __call__(self, x: T) -> bool:
        return x is not None

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, IsNotNonePredicate)


always_true_p = AlwaysTruePredicate()
always_false_p = AlwaysFalsePredicate()
is_empty_p = IsEmptyPredicate()
