from dataclasses import dataclass
from typing import Any, Callable, Self, cast

from predicate.helpers import const


def predicate_or(*predicates):
    def _predicate_or(x: Any) -> bool:
        return any(predicate(x) for predicate in predicates)

    return _predicate_or


def predicate_xor(predicate_1, predicate_2):
    def _predicate_xor(x: Any) -> bool:
        return predicate_1(x) ^ predicate_2(x)

    return _predicate_xor


def predicate_and(*predicates):
    def _predicate_and(x: Any) -> bool:
        return all(predicate(x) for predicate in predicates)

    return _predicate_and


@dataclass
class Predicate[T]:
    predicate_fn: Callable[[T], bool]

    def __call__(self, x: T) -> bool:
        return self.predicate_fn(x)

    def __and__(self, predicate: Self) -> Self:
        return AndPredicate(left=self, right=predicate)

    def __or__(self, predicate: Self) -> Self:
        return OrPredicate(left=self, right=predicate)

    def __xor__(self, predicate: Self) -> Self:
        return XorPredicate[T](left=self, right=predicate)

    def __invert__(self) -> Self:
        return NotPredicate(predicate=self)

    def __str__(self) -> str:
        return str(self.predicate_fn)

    def __eq__(self, other) -> bool:
        p1 = self.predicate_fn
        p2 = other.predicate_fn
        return p1.__code__ == p2.__code__ and p1.__closure__ == p2.__closure__

    @property
    def always_true(self) -> bool:
        return False

    @property
    def always_false(self) -> bool:
        return False


@dataclass
class AndPredicate[T](Predicate[T]):
    def __init__(self, left: Predicate[T], right: Predicate[T]):
        self.left = left
        self.right = right
        self.predicate_fn = predicate_and(left, right)

    @property
    def always_false(self) -> bool:
        return self.left.always_false or self.right.always_false

    @property
    def always_true(self) -> bool:
        return self.left.always_true and self.right.always_true


@dataclass
class NotPredicate[T](Predicate[T]):
    def __init__(self, predicate: Predicate[T]):
        self.predicate = predicate
        self.predicate_fn = lambda x: not predicate(x)

    @property
    def always_true(self) -> bool:
        return self.predicate.always_false

    @property
    def always_false(self) -> bool:
        return self.predicate.always_true


@dataclass
class OrPredicate[T](Predicate[T]):
    def __init__(self, left: Predicate[T], right: Predicate[T]):
        self.left = left
        self.right = right
        self.predicate_fn = predicate_or(left, right)

    @property
    def always_false(self) -> bool:
        return self.left.always_false and self.right.always_false

    @property
    def always_true(self) -> bool:
        return self.left.always_true or self.right.always_true


@dataclass
class XorPredicate[T](Predicate[T]):
    def __init__(self, left: Predicate[T], right: Predicate[T]):
        self.left = left
        self.right = right
        self.predicate_fn = predicate_xor(left, right)

    @property
    def always_false(self) -> bool:
        return (self.left.always_false and self.right.always_false) or (
            self.left.always_true and self.right.always_true
        )

    @property
    def always_true(self) -> bool:
        return (self.left.always_true and self.right.always_false) or (
            self.left.always_false and self.right.always_true
        )


def to_filtered(
    iter: list[str | None], predicate: Predicate[str | None]
) -> list[str | None]:
    return [x for x in iter if predicate(x)]


def get_as_not_predicate[T](predicate: Predicate[T]) -> NotPredicate[T] | None:
    return (
        cast(NotPredicate, predicate) if isinstance(predicate, NotPredicate) else None
    )


def get_as_and_predicate[T](predicate: Predicate[T]) -> AndPredicate[T] | None:
    return (
        cast(AndPredicate, predicate) if isinstance(predicate, AndPredicate) else None
    )


def get_as_or_predicate[T](predicate: Predicate[T]) -> OrPredicate[T] | None:
    return cast(OrPredicate, predicate) if isinstance(predicate, OrPredicate) else None


def get_as_xor_predicate[T](predicate: Predicate[T]) -> XorPredicate[T] | None:
    return (
        cast(XorPredicate, predicate) if isinstance(predicate, XorPredicate) else None
    )


@dataclass
class AlwaysTruePredicate(Predicate):
    def __init__(self):
        super().__init__(predicate_fn=const(True))

    @property
    def always_true(self) -> bool:
        return True


@dataclass
class AlwaysFalsePredicate(Predicate):
    def __init__(self):
        super().__init__(predicate_fn=const(False))

    @property
    def always_false(self) -> bool:
        return True


always_true_p = AlwaysTruePredicate()
always_false_p = AlwaysFalsePredicate()
