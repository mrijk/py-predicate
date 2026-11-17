import math
from itertools import cycle
from typing import Any, Final

from predicate.function_predicate import fn_p
from predicate.is_close_predicate import IsClosePredicate, is_close_p
from predicate.predicate import Predicate
from predicate.range_predicate import ge_le_p

is_integer_valued_p: Final[Predicate[float]] = fn_p(
    fn=lambda value: isinstance(value, float) and value.is_integer(),
    generate_true_fn=lambda: cycle([0.0, -0.0, 1.0, -2.0, 2.0**53]),
    generate_false_fn=lambda: cycle([0.5, -0.5, math.inf, -math.inf, math.nan]),
)
"""Return True for a float with no fractional part, otherwise False."""

is_probability_p = ge_le_p(0.0, 1.0)
"""Return True for values in the closed unit interval."""


def is_within_p(target: float, delta: float) -> IsClosePredicate[Any]:
    """Compare with an absolute tolerance, without relative tolerance.

    The target and delta must be finite, and delta must be non-negative.
    This is a convenience form of is_close_p(target, rel_tol=0, abs_tol=delta).
    """
    if not math.isfinite(target):
        raise ValueError("target must be finite")
    if not math.isfinite(delta) or delta < 0:
        raise ValueError("delta must be finite and non-negative")
    return is_close_p(target, rel_tol=0.0, abs_tol=delta)
