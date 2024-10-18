from _operator import is_not, is_
from functools import partial
from typing import Any, Iterable

from predicate.predicate import Predicate

is_not_none_p: Predicate[Any | None] = Predicate(partial(is_not, None))
is_none_p: Predicate[Any | None] = Predicate(partial(is_, None))


def in_p[T](*v: T) -> Predicate[T]:
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


neg_p = Predicate[int](lambda x: x < 0)


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
