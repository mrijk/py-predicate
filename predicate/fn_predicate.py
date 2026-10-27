import asyncio
import math
import random
import sys
from dataclasses import dataclass, field
from itertools import repeat
from typing import Callable, Final, Iterator, overload, override

from predicate.generator.helpers import generate_even_numbers, generate_odd_numbers, random_floats
from predicate.is_async_predicate import is_async_p
from predicate.predicate import Predicate


def _undefined() -> Iterator:
    raise ValueError("Please register generator type")


@dataclass
class FnPredicate[T](Predicate[T]):
    """A predicate class that can hold a function."""

    predicate_fn: Callable[[T], bool]
    generate_false_fn: Callable[[], Iterator] = _undefined
    generate_true_fn: Callable[[], Iterator] = _undefined
    _call: Callable[[T], bool] = field(init=False, repr=False)

    def __post_init__(self):
        if is_async_p(self.predicate_fn):
            self._call = lambda x: asyncio.run(self.predicate_fn(x))  # type: ignore[arg-type]
        else:
            self._call = self.predicate_fn

    def __call__(self, x: T) -> bool:
        return self._call(x)

    def __repr__(self) -> str:
        return f"fn_p(predicate_fn={self.predicate_fn.__name__})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"Function returned False for value {x}"}


def fn_p[T](
    fn: Callable[[T], bool],
    generate_false_fn: Callable[[], Iterator[T]] = _undefined,
    generate_true_fn: Callable[[], Iterator[T]] = _undefined,
) -> Predicate[T]:
    """Return the boolean value of the function call."""
    return FnPredicate(predicate_fn=fn, generate_false_fn=generate_false_fn, generate_true_fn=generate_true_fn)


@overload
def as_predicate[T](fn: Callable[[T], bool]) -> Predicate[T]: ...


@overload
def as_predicate[T](
    fn: None = None,
    *,
    generate_true_fn: Callable[[], Iterator[T]] = _undefined,
    generate_false_fn: Callable[[], Iterator[T]] = _undefined,
) -> Callable[[Callable[[T], bool]], Predicate[T]]: ...


def as_predicate[T](
    fn: Callable[[T], bool] | None = None,
    *,
    generate_true_fn: Callable[[], Iterator[T]] = _undefined,
    generate_false_fn: Callable[[], Iterator[T]] = _undefined,
) -> Predicate[T] | Callable[[Callable[[T], bool]], Predicate[T]]:
    def decorator(f: Callable[[T], bool]) -> Predicate[T]:
        return fn_p(f, generate_true_fn=generate_true_fn, generate_false_fn=generate_false_fn)

    return decorator if fn is None else decorator(fn)


is_even_p: Final[Predicate[int]] = fn_p(
    fn=lambda x: x % 2 == 0, generate_true_fn=generate_even_numbers, generate_false_fn=generate_odd_numbers
)
is_odd_p: Final[Predicate[int]] = fn_p(
    fn=lambda x: x % 2 != 0, generate_true_fn=generate_odd_numbers, generate_false_fn=generate_even_numbers
)


def generate_nan() -> Iterator:
    yield from repeat(math.nan)


def generate_inf() -> Iterator:
    while True:
        yield -math.inf
        yield math.inf


is_finite_p: Final[Predicate] = fn_p(fn=math.isfinite, generate_true_fn=random_floats, generate_false_fn=generate_inf)
"""Return True if value is finite, otherwise False."""

is_inf_p: Final[Predicate] = fn_p(fn=math.isinf, generate_true_fn=generate_inf, generate_false_fn=random_floats)
"""Return True if value is infinite, otherwise False."""

is_nan_p: Final[Predicate] = fn_p(fn=math.isnan, generate_true_fn=generate_nan, generate_false_fn=random_floats)
"""Return True if value is not a number, otherwise False."""


if sys.version_info >= (3, 15):
    isnormal, issubnormal = math.isnormal, math.issubnormal
else:

    def isnormal(x: float) -> bool:
        return math.isfinite(x) and abs(x) >= sys.float_info.min

    def issubnormal(x: float) -> bool:
        return math.isfinite(x) and 0 < abs(x) < sys.float_info.min


def generate_subnormal() -> Iterator:
    while True:
        yield random.choice([-1, 1]) * random.uniform(5e-324, sys.float_info.min / 2)


def generate_non_normal() -> Iterator:
    while True:
        yield 0.0
        yield from generate_inf()
        yield math.nan
        yield next(generate_subnormal())


is_normal_p: Final[Predicate] = fn_p(fn=isnormal, generate_true_fn=random_floats, generate_false_fn=generate_non_normal)
"""Return True if value is a normal float (finite, non-zero, not subnormal), otherwise False."""

is_subnormal_p: Final[Predicate] = fn_p(
    fn=issubnormal, generate_true_fn=generate_subnormal, generate_false_fn=random_floats
)
"""Return True if value is a subnormal float, otherwise False."""
