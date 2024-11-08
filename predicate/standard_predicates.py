from collections.abc import Callable
from datetime import datetime
from typing import Final
from uuid import UUID

from predicate.predicate import (
    AllPredicate,
    AnyPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsInstancePredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    Predicate,
)

is_not_none_p: Final[IsNotNonePredicate] = IsNotNonePredicate()
"""Return True if value is not None, otherwise False."""

is_none_p: Final[IsNonePredicate] = IsNonePredicate()
"""Return True if value is None, otherwise False."""


def in_p[T](*v: T) -> InPredicate[T]:
    """Return True if the values are included in the set, otherwise False."""
    return InPredicate(v=v)


def not_in_p[T](*v: T) -> NotInPredicate[T]:
    """Return True if the values are not in the set, otherwise False."""
    return NotInPredicate(v=v)


def eq_p[T](v: T) -> EqPredicate[T]:
    """Return True if the value is equal to the constant, otherwise False."""
    return EqPredicate(v=v)


def ne_p[T](v: T) -> NePredicate[T]:
    """Return True if the value is not equal to the constant, otherwise False."""
    return NePredicate(v=v)


def ge_p[T: (int, str, datetime, UUID)](v: T) -> GePredicate[T]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GePredicate(v=v)


def gt_p[T: (int, str, datetime, UUID)](v: T) -> GtPredicate[T]:
    """Return True if the value is greater than the constant, otherwise False."""
    return GtPredicate(v=v)


def le_p[T: (int, str, datetime, UUID)](v: T) -> LePredicate[T]:
    """Return True if the value is less than or equal to the constant, otherwise False."""
    return LePredicate(v=v)


def lt_p[T: (int, str, datetime, UUID)](v: T) -> LtPredicate[T]:
    """Return True if the value is less than the constant, otherwise False."""
    return LtPredicate(v=v)


def fn_p[T](fn: Callable[[T], bool]) -> FnPredicate[T]:
    """Return the boolean value of the function call."""
    return FnPredicate(predicate_fn=fn)


neg_p = lt_p(0)
"""Returns True of the value is negative, otherwise False."""

zero_p = eq_p(0)
"""Returns True of the value is zero, otherwise False."""

pos_p = gt_p(0)
"""Returns True of the value is positive, otherwise False."""


def any_p[T](predicate: Predicate[T]) -> AnyPredicate[T]:
    return AnyPredicate(predicate=predicate)


def all_p[T](predicate: Predicate[T]) -> AllPredicate[T]:
    return AllPredicate(predicate=predicate)


def is_instance_p(*klass: type) -> IsInstancePredicate:
    """Return True if value is an instance of one of the classes, otherwise False."""
    return IsInstancePredicate(klass=klass)


is_datetime_p = is_instance_p(datetime)
"""Returns True if the value is a datetime, otherwise False."""

is_dict_p = is_instance_p(dict)
"""Returns True if the value is a dict, otherwise False."""

is_float_p = is_instance_p(float)
"""Returns True if the value is a float, otherwise False."""

is_int_p = is_instance_p(int)
"""Returns True if the value is an integer, otherwise False."""

is_list_p = is_instance_p(list)
"""Returns True if the value is a list, otherwise False."""

is_str_p = is_instance_p(str)
"""Returns True if the value is a str, otherwise False."""

is_uuid_p = is_instance_p(UUID)
"""Returns True if the value is a UUID, otherwise False."""

eq_true_p = eq_p(True)
eq_false_p = eq_p(False)
