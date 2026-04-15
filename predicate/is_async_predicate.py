from dataclasses import dataclass
from inspect import iscoroutinefunction
from typing import Any, Final, override

from predicate.predicate import Predicate


@dataclass
class IsAsyncPredicate[T](Predicate[T]):
    """A predicate class that models the is_async predicate."""

    def __call__(self, x: Any) -> bool:
        return iscoroutinefunction(x)

    def __repr__(self) -> str:
        return "is_async_p"

    @override
    def explain_failure(self, x: Any) -> dict:
        return {"reason": f"{x} is not an async function"}


is_async_p: Final[IsAsyncPredicate] = IsAsyncPredicate()
