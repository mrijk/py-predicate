import math
from dataclasses import dataclass
from typing import Callable, Final, Iterator, override

from predicate.generator.helpers import generate_even_numbers, generate_odd_numbers, random_floats
from predicate.predicate import Predicate
from predicate.standard_predicates import generate_inf, generate_nan


def undefined() -> Iterator:
    raise ValueError("Please register generator type")


@dataclass
class FnPredicate[T](Predicate[T]):
    """A predicate class that can hold a function."""

    predicate_fn: Callable[[T], bool]
    generate_false_fn: Callable[[], Iterator] = undefined
    generate_true_fn: Callable[[], Iterator] = undefined

    def __call__(self, x: T) -> bool:
        return self.predicate_fn(x)

    def __repr__(self) -> str:
        return f"fn_p(predicate_fn={self.predicate_fn.__name__})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"Function returned False for value {x}"}


def fn_p[T](
    fn: Callable[[T], bool],
    generate_false_fn: Callable[[], Iterator[T]] = undefined,
    generate_true_fn: Callable[[], Iterator[T]] = undefined,
) -> Predicate[T]:
    """Return the boolean value of the function call."""
    return FnPredicate(predicate_fn=fn, generate_false_fn=generate_false_fn, generate_true_fn=generate_true_fn)


is_even_p: Final[Predicate[int]] = fn_p(
    fn=lambda x: x % 2 == 0, generate_true_fn=generate_even_numbers, generate_false_fn=generate_odd_numbers
)
is_odd_p: Final[Predicate[int]] = fn_p(
    fn=lambda x: x % 2 != 0, generate_true_fn=generate_odd_numbers, generate_false_fn=generate_even_numbers
)

is_finite_p: Final[Predicate] = fn_p(fn=math.isfinite, generate_true_fn=random_floats, generate_false_fn=generate_inf)
"""Return True if value is finite, otherwise False."""

is_inf_p: Final[Predicate] = fn_p(fn=math.isinf, generate_true_fn=generate_inf, generate_false_fn=random_floats)
"""Return True if value is infinite, otherwise False."""

is_nan_p: Final[Predicate] = fn_p(fn=math.isnan, generate_true_fn=generate_nan, generate_false_fn=random_floats)
"""Return True if value is not a number, otherwise False."""
