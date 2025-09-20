from functools import partial
from typing import Callable

from predicate.all_predicate import all_p
from predicate.comp_predicate import comp_p
from predicate.eq_predicate import eq_p
from predicate.ge_predicate import ge_p
from predicate.gt_predicate import gt_p
from predicate.is_instance_predicate import is_dict_p, is_float_p, is_int_p, is_iterable_p, is_list_p, is_str_p
from predicate.is_none_predicate import is_none_p
from predicate.lazy_predicate import lazy_p
from predicate.le_predicate import le_p
from predicate.lt_predicate import lt_p
from predicate.ne_predicate import ne_p
from predicate.predicate import Predicate
from predicate.predicate_factory import PredicateFactory
from predicate.root_predicate import RootPredicate
from predicate.this_predicate import ThisPredicate


def is_iterable_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is an iterable, and for all elements the predicate is True, otherwise False."""
    return is_iterable_p & all_p(predicate)


def is_single_or_iterable_of_p[T](predicate: Predicate[T]) -> Predicate:
    """Return True if value is an iterable or a single value, and for all elements the predicate is True, otherwise False."""
    return is_iterable_of_p(predicate) | predicate


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


def depth_op_p(depth: int, predicate: Callable[[int], Predicate]) -> Predicate[dict]:
    return comp_p(dict_depth, predicate(depth))


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

# Construction of a lazy predicate to check for valid json

_valid_json_p = lazy_p("is_json_p")
json_list_p = is_list_p & lazy_p("json_values")

json_keys_p = all_p(is_str_p)

json_values = all_p(is_str_p | is_int_p | is_float_p | json_list_p | _valid_json_p | is_none_p)
json_values_p = comp_p(lambda x: x.values(), json_values)

is_json_p = (is_dict_p & json_keys_p & json_values_p) | json_list_p
"""Returns True if the value is a valid json structure, otherwise False."""
