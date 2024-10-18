from _operator import is_not, is_
from dataclasses import dataclass
from functools import partial
from typing import Any, Callable, Self, Iterable, cast

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

    def __and__(self, predicate: Self) -> "AndPredicate":
        return AndPredicate(left=self, right=predicate)

    def __or__(self, predicate: Self) -> "OrPredicate":
        return OrPredicate(left=self, right=predicate)

    def __xor__(self, predicate: Self) -> "XorPredicate":
        return XorPredicate(left=self, right=predicate)

    def __invert__(self) -> "NotPredicate":
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


def get_as_not_predicate[T](predicate: Predicate[T]) -> NotPredicate[T] | None:
    return (
        cast(NotPredicate, predicate) if isinstance(predicate, NotPredicate) else None
    )


def get_as_and_predicate[T](predicate: Predicate[T]) -> AndPredicate[T] | None:
    return (
        cast(AndPredicate, predicate) if isinstance(predicate, AndPredicate) else None
    )


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


# Couple of standard predicates


is_not_none_p: Predicate[Any | None] = Predicate(partial(is_not, None))
is_none_p: Predicate[Any | None] = Predicate(partial(is_, None))


def in_p(*v) -> Predicate:
    return Predicate(lambda x: x in v)


def eq_p[T](v: T) -> Predicate[T]:
    return Predicate(lambda x: x == v)


def ne_p[T](v: T) -> Predicate[T]:
    return Predicate(lambda x: x != v)


def ge_p[T: (int, str)](v: T) -> Predicate[T]:
    def _ge(x: T) -> bool:
        return x >= v

    return Predicate(_ge)


def gt_p[T: (int, str)](v: T) -> Predicate[T]:
    def _gt(x: T) -> bool:
        return x > v

    return Predicate(_gt)


def le_p[T: (int, str)](v: T) -> Predicate[T]:
    return Predicate(lambda x: x <= v)


def lt_p[T: (int, str)](v: T) -> Predicate[T]:
    return Predicate(lambda x: x < v)


def any_p[T](predicate: Predicate[T]) -> Predicate[Iterable[T]]:
    return Predicate(lambda iter: any(predicate(x) for x in iter))


def all_p[T](predicate: Predicate[T]) -> Predicate[Iterable[T]]:
    return Predicate(lambda iter: all(predicate(x) for x in iter))


def is_instance_p(*klass: type) -> Predicate:
    return Predicate(lambda x: isinstance(x, klass))


is_int_p = is_instance_p(int)
is_str_p = is_instance_p(str)
is_dict_p = is_instance_p(dict)
is_list_p = is_instance_p(list)

eq_true_p = eq_p(True)
eq_false_p = eq_p(False)


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
