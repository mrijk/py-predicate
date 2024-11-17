from collections.abc import Callable, Iterable
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Final
from uuid import UUID

from more_itertools import ilen

from predicate.comp_predicate import CompPredicate
from predicate.lazy_predicate import LazyPredicate
from predicate.predicate import (
    AllPredicate,
    AnyPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsFalsyPredicate,
    IsInstancePredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    IsTruthyPredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    Predicate,
    resolve_predicate,
)
from predicate.regex_predicate import RegexPredicate
from predicate.root_predicate import RootPredicate
from predicate.this_predicate import ThisPredicate

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


def comp_p[T](fn: Callable[[Any], T], predicate: Predicate[T]) -> CompPredicate:
    """Return a predicate, composed of a function and another predicate."""
    return CompPredicate(fn=fn, predicate=predicate)


def fn_p[T](fn: Callable[[T], bool]) -> FnPredicate[T]:
    """Return the boolean value of the function call."""
    return FnPredicate(predicate_fn=fn)


def has_length_p(length: int) -> Predicate[Iterable]:
    """Return True if length of iterable is equal to value, otherwise False."""
    return fn_p(lambda x: ilen(x) == length)


neg_p = lt_p(0)
"""Returns True of the value is negative, otherwise False."""

zero_p = eq_p(0)
"""Returns True of the value is zero, otherwise False."""

pos_p = gt_p(0)
"""Returns True of the value is positive, otherwise False."""


def any_p[T](predicate: Predicate[T]) -> AnyPredicate[T]:
    """Return True if the predicate holds for any item in the iterable, otherwise False."""
    return AnyPredicate(predicate=resolve_predicate(predicate))


def all_p[T](predicate: Predicate[T]) -> AllPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return AllPredicate(predicate=resolve_predicate(predicate))


def lazy_p(ref: str) -> LazyPredicate:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return LazyPredicate(ref=ref)


def is_instance_p(*klass: type) -> Predicate:
    """Return True if value is an instance of one of the classes, otherwise False."""
    return IsInstancePredicate(klass=klass)


def is_iterable_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is an iterable, and for all elements the predicate is True, otherwise False."""
    return is_iterable_p & all_p(predicate)


def is_list_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is a list, and for all elements in the list the predicate is True, otherwise False."""
    return is_list_p & all_p(predicate)


def is_tuple_of_p(*predicates: Predicate) -> Predicate:
    """Return True if value is a tuple, and for all elements in the tuple the predicate is True, otherwise False."""

    def valid_tuple_values(x: Iterable) -> bool:
        return all(p(v) for p, v in zip(predicates, x, strict=False))

    return is_tuple_p & has_length_p(length=len(predicates)) & fn_p(fn=valid_tuple_values)


def is_set_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is a set, and for all elements in the set the predicate is True, otherwise False."""
    return is_set_p & all_p(predicate)


def regex_p(pattern: str) -> Predicate[str]:
    return RegexPredicate(pattern=pattern)


is_bool_p = is_instance_p(bool)
"""Returns True if the value is a bool, otherwise False."""

is_callable_p = is_instance_p(Callable)  # type: ignore
"""Returns True if the value is a callable, otherwise False."""

is_complex_p = is_instance_p(complex)
"""Returns True if the value is a complex, otherwise False."""

is_datetime_p = is_instance_p(datetime)
"""Returns True if the value is a datetime, otherwise False."""

is_dict_p = is_instance_p(dict)
"""Returns True if the value is a dict, otherwise False."""

is_float_p = is_instance_p(float)
"""Returns True if the value is a float, otherwise False."""

is_iterable_p = is_instance_p(Iterable)
"""Returns True if the value is an Iterable, otherwise False."""

is_int_p = is_instance_p(int)
"""Returns True if the value is an integer, otherwise False."""

is_list_p = is_instance_p(list)
"""Returns True if the value is a list, otherwise False."""

is_predicate_p = is_instance_p(Predicate)
"""Returns True if the value is a predicate, otherwise False."""

is_range_p = is_instance_p(range)
"""Returns True if the value is a range, otherwise False."""

is_set_p = is_instance_p(set)
"""Returns True if the value is a set, otherwise False."""

is_str_p = is_instance_p(str)
"""Returns True if the value is a str, otherwise False."""

is_tuple_p = is_instance_p(tuple)
"""Returns True if the value is a tuple, otherwise False."""

is_uuid_p = is_instance_p(UUID)
"""Returns True if the value is a UUID, otherwise False."""

eq_true_p = eq_p(True)
"""Returns True if the value is True, otherwise False."""

eq_false_p = eq_p(False)
"""Returns True if the value is False, otherwise False."""

is_falsy_p: Final[IsFalsyPredicate] = IsFalsyPredicate()
is_truthy_p: Final[IsTruthyPredicate] = IsTruthyPredicate()


@dataclass
class PredicateFactory[T](Predicate[T]):
    """Test."""

    factory: Callable[[], Predicate]

    @property
    def predicate(self) -> Predicate:
        return self.factory()

    def __call__(self, *args, **kwargs) -> bool:
        raise ValueError("Don't call PredicateFactory")

    def __repr__(self) -> str:
        return repr(self.predicate)


root_p: PredicateFactory = PredicateFactory(factory=RootPredicate)
this_p: PredicateFactory = PredicateFactory(factory=ThisPredicate)

# Construction of a lazy predicate to check for valid json

_valid_json_p = lazy_p("is_json_p")
json_list_p = is_list_p & lazy_p("json_values")

json_keys_p = all_p(is_str_p)

json_values = all_p(is_str_p | is_int_p | is_float_p | json_list_p | _valid_json_p | is_none_p)
json_values_p = comp_p(lambda x: x.values(), json_values)

is_json_p = (is_dict_p & json_keys_p & json_values_p) | json_list_p
"""Returns True if the value is a valid json structure, otherwise False."""
