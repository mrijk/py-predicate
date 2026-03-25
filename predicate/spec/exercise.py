from inspect import iscoroutinefunction
from types import FunctionType
from typing import AsyncIterator, Callable, Iterator

from predicate.spec.exercise_class import async_exercise_class, exercise_class
from predicate.spec.exercise_function import async_exercise_function, exercise_function
from predicate.spec.spec import Spec


def exercise(f: Callable, spec: Spec | None = None, n: int = 10) -> Iterator[tuple] | AsyncIterator[tuple]:
    is_func = isinstance(f, FunctionType)
    is_async = iscoroutinefunction(f) if is_func else iscoroutinefunction(f.__call__)  # type: ignore[operator]
    if is_async:
        return async_exercise_function(f, spec, n) if is_func else async_exercise_class(f, spec, n)
    return exercise_function(f, spec, n) if is_func else exercise_class(f, spec, n)
