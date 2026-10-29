from functools import partial
from types import FunctionType
from typing import AsyncIterator, Callable, Iterator

from predicate.is_async_predicate import is_async_p
from predicate.spec.exercise_class import async_exercise_class, exercise_class
from predicate.spec.exercise_function import async_exercise_function, exercise_function
from predicate.spec.spec import Spec


def exercise(f: Callable, spec: Spec | None = None, n: int = 10) -> Iterator[tuple] | AsyncIterator[tuple]:
    # A partial carries the signature of the function it wraps, so it's exercised like one (#362)
    is_func = isinstance(f, FunctionType | partial)
    is_async = is_async_p(f) if is_func else is_async_p(f.__call__)  # type: ignore[operator]
    if is_async:
        return async_exercise_function(f, spec, n) if is_func else async_exercise_class(f, spec, n)
    return exercise_function(f, spec, n) if is_func else exercise_class(f, spec, n)
