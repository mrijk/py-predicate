"""Predicates for annotated-types constraints in Annotated[T, ...] metadata (#384).

annotated-types isn't a dependency: its constraints are recognised by their module and class name.
"""

import math
import zoneinfo
from collections.abc import Callable, Iterator
from datetime import UTC, datetime, tzinfo
from typing import Any

from predicate.fn_predicate import fn_p, is_finite_p, is_inf_p, is_nan_p
from predicate.ge_predicate import ge_p
from predicate.gt_predicate import gt_p
from predicate.has_length_predicate import has_length_p
from predicate.le_predicate import le_p
from predicate.lt_predicate import lt_p
from predicate.predicate import Predicate
from predicate.str_predicates import is_digit_p, is_lower_p, is_upper_p

# The functions annotated-types' LowerCase, UpperCase, IsDigits, IsFinite, IsNan and IsInfinite wrap
_known_functions: list[tuple[Callable, Predicate]] = [
    (str.islower, is_lower_p),
    (str.isupper, is_upper_p),
    (str.isdigit, is_digit_p),
    (math.isfinite, is_finite_p),
    (math.isnan, is_nan_p),
    (math.isinf, is_inf_p),
]


def constraint_predicates(metadata: Any) -> Iterator[Predicate]:
    """Yield the predicates for one Annotated metadata item; anything but an annotated-types constraint yields none."""
    if type(metadata).__module__ != "annotated_types":
        return
    if getattr(metadata, "__is_annotated_types_grouped_metadata__", False):
        # Interval and Len iterate into Gt, Ge, Lt, Le, MinLen and MaxLen
        yield from (predicate for item in metadata for predicate in constraint_predicates(item))
        return
    if make := _constraints.get(type(metadata).__name__):
        yield make(metadata)


def _callable_predicate(func: Any) -> Predicate:
    if isinstance(func, Predicate):
        return func  # e.g. Predicate(ge_lt_p(0, 150)): a py-predicate predicate used as annotated-types metadata
    if type(func).__module__ == "annotated_types" and type(func).__name__ == "Not":
        return ~_callable_predicate(func.func)
    return next((predicate for known, predicate in _known_functions if known is func), None) or fn_p(func)


def _multiple_of_p(n: Any) -> Predicate:
    from predicate.generator.helpers import random_ints

    def is_multiple(x: Any) -> bool:
        return x % n == 0

    is_multiple.__name__ = f"is_multiple_of_{n}"
    return fn_p(is_multiple, generate_true_fn=lambda: (n * k for k in random_ints(lower=-1000, upper=1000)))


def _timezone_p(tz: Any) -> Predicate:
    """Timezone(None) means naive, Timezone(...) aware, and Timezone('Europe/Amsterdam') or Timezone(UTC) that zone."""
    from predicate.generator.helpers import random_datetimes

    if tz is None:
        return fn_p(lambda x: x.tzinfo is None, generate_true_fn=random_datetimes)
    if tz is ...:
        zone: tzinfo = UTC
        return fn_p(lambda x: x.tzinfo is not None, generate_true_fn=lambda: _in_zone(random_datetimes(), zone))
    zone = zoneinfo.ZoneInfo(tz) if isinstance(tz, str) else tz
    # ponytail: compared with ==, so the same offset under another zone object (e.g. a fixed +09:00) doesn't match
    return fn_p(lambda x: x.tzinfo == zone, generate_true_fn=lambda: _in_zone(random_datetimes(), zone))


def _in_zone(values: Iterator[datetime], zone: tzinfo) -> Iterator[datetime]:
    return (value.replace(tzinfo=zone) for value in values)


# One predicate per annotated-types constraint class, by class name
_constraints: dict[str, Callable[[Any], Predicate]] = {
    "Gt": lambda c: gt_p(c.gt),
    "Ge": lambda c: ge_p(c.ge),
    "Lt": lambda c: lt_p(c.lt),
    "Le": lambda c: le_p(c.le),
    "MinLen": lambda c: has_length_p(ge_p(c.min_length)),
    "MaxLen": lambda c: has_length_p(le_p(c.max_length)),
    "MultipleOf": lambda c: _multiple_of_p(c.multiple_of),
    "Timezone": lambda c: _timezone_p(c.tz),
    "Predicate": lambda c: _callable_predicate(c.func),
}
