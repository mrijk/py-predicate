import math
from collections.abc import Callable, Container, Iterable
from dataclasses import dataclass
from datetime import datetime
from functools import partial
from itertools import repeat
from typing import Any, Final, Hashable, Iterator
from uuid import UUID

from predicate.all_predicate import AllPredicate
from predicate.any_predicate import AnyPredicate
from predicate.comp_predicate import CompPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.fn_predicate import FnPredicate, undefined
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.has_path_predicate import HasPathPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_predicate_of_p import IsPredicateOfPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.lazy_predicate import LazyPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import ConstrainedT, Predicate, resolve_predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.regex_predicate import RegexPredicate
from predicate.root_predicate import RootPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.tee_predicate import TeePredicate
from predicate.this_predicate import ThisPredicate
from predicate.tuple_of_predicate import TupleOfPredicate

is_not_none_p: Final[IsNotNonePredicate] = IsNotNonePredicate()
"""Return True if value is not None, otherwise False."""

is_none_p: Final[IsNonePredicate] = IsNonePredicate()
"""Return True if value is None, otherwise False."""


def eq_p[T](v: T) -> EqPredicate[T]:
    """Return True if the value is equal to the constant, otherwise False."""
    return EqPredicate(v=v)


def ne_p[T](v: T) -> NePredicate[T]:
    """Return True if the value is not equal to the constant, otherwise False."""
    return NePredicate(v=v)


def ge_p(v: ConstrainedT) -> GePredicate[ConstrainedT]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GePredicate(v=v)


def ge_le_p(lower: ConstrainedT, upper: ConstrainedT) -> GeLePredicate[ConstrainedT]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GeLePredicate(lower=lower, upper=upper)


def ge_lt_p(lower: ConstrainedT, upper: ConstrainedT) -> GeLtPredicate[ConstrainedT]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GeLtPredicate(lower=lower, upper=upper)


def gt_le_p(lower: ConstrainedT, upper: ConstrainedT) -> GtLePredicate[ConstrainedT]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GtLePredicate(lower=lower, upper=upper)


def gt_lt_p(lower: ConstrainedT, upper: ConstrainedT) -> GtLtPredicate[ConstrainedT]:
    """Return True if the value is greater or equal than the constant, otherwise False."""
    return GtLtPredicate(lower=lower, upper=upper)


def gt_p(v: ConstrainedT) -> GtPredicate[ConstrainedT]:
    """Return True if the value is greater than the constant, otherwise False."""
    return GtPredicate(v=v)


def le_p(v: ConstrainedT) -> LePredicate[ConstrainedT]:
    """Return True if the value is less than or equal to the constant, otherwise False."""
    return LePredicate(v=v)


def lt_p(v: ConstrainedT) -> LtPredicate[ConstrainedT]:
    """Return True if the value is less than the constant, otherwise False."""
    return LtPredicate(v=v)


def comp_p[T](fn: Callable[[Any], T], predicate: Predicate[T]) -> CompPredicate:
    """Return a predicate, composed of a function and another predicate."""
    return CompPredicate(fn=fn, predicate=predicate)


def fn_p[T](
    fn: Callable[[T], bool],
    generate_false_fn: Callable[[], Iterator] = undefined,
    generate_true_fn: Callable[[], Iterator] = undefined,
) -> Predicate[T]:
    """Return the boolean value of the function call."""
    return FnPredicate(predicate_fn=fn, generate_false_fn=generate_false_fn, generate_true_fn=generate_true_fn)


def tee_p[T](fn: Callable[[T], None]) -> Predicate[T]:
    """Return the boolean value of the function call."""
    return TeePredicate(fn=fn)


def has_length_p(length_p: Predicate[int]) -> Predicate[Iterable]:
    """Return True if length of iterable is equal to value, otherwise False."""
    return HasLengthPredicate(length_p=length_p)


def generate_even_numbers() -> Iterator[int]:
    from predicate.generator.helpers import random_ints

    yield 0
    yield from (value for value in random_ints() if value % 2 == 0)


def generate_odd_numbers() -> Iterator[int]:
    from predicate.generator.helpers import random_ints

    yield from (value for value in random_ints() if value % 2 != 0)


neg_p: Final[LtPredicate] = lt_p(0)
"""Returns True of the value is negative, otherwise False."""

zero_p: Final[EqPredicate] = eq_p(0)
"""Returns True of the value is zero, otherwise False."""

pos_p: Final[GtPredicate] = gt_p(0)
"""Returns True of the value is positive, otherwise False."""

is_even_p: Final[Predicate[int]] = fn_p(
    lambda x: x % 2 == 0, generate_true_fn=generate_even_numbers, generate_false_fn=generate_odd_numbers
)
is_odd_p: Final[Predicate[int]] = fn_p(
    lambda x: x % 2 != 0, generate_true_fn=generate_odd_numbers, generate_false_fn=generate_even_numbers
)

is_empty_p: Final[Predicate[Iterable]] = has_length_p(zero_p)
"""Predicate that returns True if the iterable is empty, otherwise False."""

is_not_empty_p: Final[Predicate[Iterable]] = has_length_p(pos_p)
"""Predicate that returns True if the iterable is not empty, otherwise False."""


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
    return IsInstancePredicate(instance_klass=klass)


def is_iterable_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is an iterable, and for all elements the predicate is True, otherwise False."""
    return is_iterable_p & all_p(predicate)


def is_single_or_iterable_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is an iterable or a single value, and for all elements the predicate is True, otherwise False."""
    return is_iterable_of_p(predicate) | predicate


def is_list_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is a list, and for all elements in the list the predicate is True, otherwise False."""
    return ListOfPredicate(predicate)


def is_single_or_list_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is a list or a single value, and for all elements in the list the predicate is True, otherwise False."""
    return is_list_of_p(predicate) | predicate


def is_dict_of_p(*predicates: tuple[Predicate | str, Predicate]) -> Predicate:
    """Return True if value is a set, and for all elements in the set the predicate is True, otherwise False."""
    # return is_set_p & all_p(predicate)
    return DictOfPredicate(list(predicates))


def is_tuple_of_p(*predicates: Predicate) -> Predicate:
    """Return True if value is a tuple, and for all elements in the tuple the predicate is True, otherwise False."""
    return TupleOfPredicate(list(predicates))


def is_set_of_p[T](predicate: Predicate[T]) -> Predicate[set[T]]:
    """Return True if value is a set, and for all elements in the set the predicate is True, otherwise False."""
    return SetOfPredicate(predicate)


def has_path_p(*predicates: Predicate) -> Predicate:
    """Return True if value is a dict, and contains the path specified by the predicates, otherwise False."""
    return HasPathPredicate(list(predicates))


def regex_p(pattern: str) -> Predicate[str]:
    """Return True if value matches regex, otherwise False."""
    return RegexPredicate(pattern=pattern)


def is_predicate_of_p(klass: type) -> Predicate:
    return IsPredicateOfPredicate(predicate_klass=klass)


is_bool_p = is_instance_p(bool)
"""Returns True if the value is a bool, otherwise False."""

is_bytearray_p = is_instance_p(bytearray)
"""Returns True if the value is a bytearray, otherwise False."""

is_callable_p = is_instance_p(Callable)  # type: ignore
"""Returns True if the value is a callable, otherwise False."""

is_complex_p = is_instance_p(complex)
"""Returns True if the value is a complex, otherwise False."""

is_container_p = is_instance_p(Container)
"""Returns True if the value is a container (list, set, tuple, etc.), otherwise False."""

is_datetime_p = is_instance_p(datetime)
"""Returns True if the value is a datetime, otherwise False."""

is_dict_p = is_instance_p(dict)
"""Returns True if the value is a dict, otherwise False."""

is_float_p = is_instance_p(float)
"""Returns True if the value is a float, otherwise False."""

is_hashable_p = is_instance_p(Hashable)
"""Returns True if the value is hashable, otherwise False."""

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

eq_true_p: Final[EqPredicate] = eq_p(True)
"""Returns True if the value is True, otherwise False."""

eq_false_p: Final[EqPredicate] = eq_p(False)
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
        raise ValueError("Don't call PredicateFactory directly")

    def __repr__(self) -> str:
        return repr(self.predicate)


root_p: PredicateFactory = PredicateFactory(factory=RootPredicate)
this_p: PredicateFactory = PredicateFactory(factory=ThisPredicate)


def dict_depth(value: dict) -> int:
    match value:
        case list() as l:
            return 1 + max(dict_depth(item) for item in l) if l else 0
        case dict() as d if d:
            return 1 + max(dict_depth(item) for item in d.values())
        case _:
            return 1


def has_key_p[T](key: T) -> HasKeyPredicate:
    """Return True if dict contains key, otherwise False."""
    return HasKeyPredicate(key=key)


def depth_op_p(depth: int, predicate: Callable[[int], Predicate]) -> Predicate[dict]:
    return comp_p(dict_depth, predicate(depth))


def generate_nan() -> Iterator:
    yield from repeat(math.nan)


def generate_inf() -> Iterator:
    while True:
        yield -math.inf
        yield math.inf


def _random_floats() -> Iterator:
    from predicate.generator.helpers import random_floats

    yield from random_floats()


depth_eq_p = partial(depth_op_p, predicate=eq_p)
"""Returns if dict depth is equal to given depth, otherwise False."""

depth_ne_p = partial(depth_op_p, predicate=ne_p)
"""Returns if dict depth is not equal to given depth, otherwise False."""

depth_le_p = partial(depth_op_p, predicate=le_p)
"""Returns if dict depth is less or equal to given depth, otherwise False."""

depth_lt_p = partial(depth_op_p, predicate=lt_p)
"""Returns if dict depth is less than given depth, otherwise False."""

depth_ge_p = partial(depth_op_p, predicate=ge_p)
"""Returns if dict depth is greater or equal to given depth, otherwise False."""

depth_gt_p = partial(depth_op_p, predicate=gt_p)
"""Returns if dict depth is greater than given depth, otherwise False."""

is_finite_p: Final[Predicate] = fn_p(fn=math.isfinite, generate_true_fn=_random_floats, generate_false_fn=generate_inf)
"""Return True if value is finite, otherwise False."""

is_inf_p: Final[Predicate] = fn_p(fn=math.isinf, generate_true_fn=generate_inf, generate_false_fn=_random_floats)
"""Return True if value is infinite, otherwise False."""

is_nan_p: Final[Predicate] = fn_p(fn=math.isnan, generate_true_fn=generate_nan, generate_false_fn=_random_floats)
"""Return True if value is not a number, otherwise False."""


# Construction of a lazy predicate to check for valid json

_valid_json_p = lazy_p("is_json_p")
json_list_p = is_list_p & lazy_p("json_values")

json_keys_p = all_p(is_str_p)

json_values = all_p(is_str_p | is_int_p | is_float_p | json_list_p | _valid_json_p | is_none_p)
json_values_p = comp_p(lambda x: x.values(), json_values)

is_json_p = (is_dict_p & json_keys_p & json_values_p) | json_list_p
"""Returns True if the value is a valid json structure, otherwise False."""
