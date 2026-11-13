import math
import random
import sys
from itertools import repeat
from typing import Any, Final, Iterator

from predicate.function_predicate import fn_p
from predicate.generator.helpers import generate_even_numbers, generate_odd_numbers, random_floats
from predicate.predicate import Predicate

is_even_p: Final[Predicate[int]] = fn_p(
    fn=lambda x: x % 2 == 0, generate_true_fn=generate_even_numbers, generate_false_fn=generate_odd_numbers
)
is_odd_p: Final[Predicate[int]] = fn_p(
    fn=lambda x: x % 2 != 0, generate_true_fn=generate_odd_numbers, generate_false_fn=generate_even_numbers
)


def generate_nan() -> Iterator[Any]:
    yield from repeat(math.nan)


def generate_inf() -> Iterator[Any]:
    while True:
        yield -math.inf
        yield math.inf


is_finite_p: Final[Predicate[Any]] = fn_p(
    fn=math.isfinite, generate_true_fn=random_floats, generate_false_fn=generate_inf
)
"""Return True if value is finite, otherwise False."""

is_inf_p: Final[Predicate[Any]] = fn_p(fn=math.isinf, generate_true_fn=generate_inf, generate_false_fn=random_floats)
"""Return True if value is infinite, otherwise False."""

is_nan_p: Final[Predicate[Any]] = fn_p(fn=math.isnan, generate_true_fn=generate_nan, generate_false_fn=random_floats)
"""Return True if value is not a number, otherwise False."""


if sys.version_info >= (3, 15):
    isnormal, issubnormal = math.isnormal, math.issubnormal
else:

    def isnormal(x: float) -> bool:
        return math.isfinite(x) and abs(x) >= sys.float_info.min

    def issubnormal(x: float) -> bool:
        return math.isfinite(x) and 0 < abs(x) < sys.float_info.min


def generate_subnormal() -> Iterator[Any]:
    while True:
        yield random.choice([-1, 1]) * random.uniform(5e-324, sys.float_info.min / 2)


def generate_non_normal() -> Iterator[Any]:
    while True:
        yield 0.0
        yield from generate_inf()
        yield math.nan
        yield next(generate_subnormal())


is_normal_p: Final[Predicate[Any]] = fn_p(
    fn=isnormal, generate_true_fn=random_floats, generate_false_fn=generate_non_normal
)
"""Return True if value is a normal float (finite, non-zero, not subnormal), otherwise False."""

is_subnormal_p: Final[Predicate[Any]] = fn_p(
    fn=issubnormal, generate_true_fn=generate_subnormal, generate_false_fn=random_floats
)
"""Return True if value is a subnormal float, otherwise False."""
