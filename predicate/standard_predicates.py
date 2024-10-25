from typing import Iterable
from uuid import UUID

from predicate.predicate import (
    EqPredicate,
    GePredicate,
    AllPredicate,
    GtPredicate,
    NePredicate,
    AnyPredicate,
    LePredicate,
    LtPredicate,
    IsInstancePredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    Predicate,
    InPredicate,
)

is_not_none_p = IsNotNonePredicate()
is_none_p = IsNonePredicate()


def in_p[T](*v: T) -> InPredicate[T]:
    return InPredicate(v=v)


def eq_p[T](v: T) -> EqPredicate[T]:
    return EqPredicate(v=v)


def ne_p[T](v: T) -> NePredicate[T]:
    return NePredicate(v=v)


def ge_p[T: (int, str)](v: T) -> GePredicate[T]:
    return GePredicate(v=v)


def gt_p[T: (int, str)](v: T) -> GtPredicate[T]:
    return GtPredicate(v=v)


def le_p[T: (int, str)](v: T) -> LePredicate[T]:
    return LePredicate(v=v)


def lt_p[T: (int, str)](v: T) -> LtPredicate[T]:
    return LtPredicate(v=v)


neg_p = lt_p(0)
zero_p = eq_p(0)
pos_p = gt_p(0)


def any_p[T](predicate: Predicate[T]) -> AnyPredicate[T]:
    return AnyPredicate(predicate=predicate)


def all_p[T](predicate: Predicate[T]) -> AllPredicate[T]:
    return AllPredicate(predicate=predicate)


def is_instance_p(*klass: type) -> IsInstancePredicate:
    return IsInstancePredicate(klass=klass)


is_int_p = is_instance_p(int)
is_str_p = is_instance_p(str)
is_dict_p = is_instance_p(dict)
is_list_p = is_instance_p(list)
is_uuid_p = is_instance_p(UUID)

eq_true_p = eq_p(True)
eq_false_p = eq_p(False)
