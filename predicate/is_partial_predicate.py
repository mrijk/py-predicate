from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from inspect import signature
from typing import Any, Final, override

from predicate.predicate import Predicate


def func_is_partial(func: Callable) -> bool:
    return isinstance(func, partial)


@dataclass
class IsPartialPredicate[T](Predicate[T]):
    """A predicate class that models the is_partial predicate."""

    nr_of_parameters: int | None = None

    def __call__(self, x: Any) -> bool:
        match x:
            case Callable() as func if func_is_partial(func):  # type: ignore
                if self.nr_of_parameters is not None:
                    sig = signature(func)
                    return len(sig.parameters) == self.nr_of_parameters
                return True
            case _:
                return False

    def __repr__(self) -> str:
        return (
            "is_partial_p"
            if self.nr_of_parameters is None
            else f"is_partial_with_signature_p(nr_of_parameters={self.nr_of_parameters})"
        )

    @override
    def explain_failure(self, x: Any) -> dict[str, Any]:
        match x:
            case Callable() as func if func_is_partial(func):  # type: ignore
                sig = signature(func)
                return {
                    "reason": f"Partial has {len(sig.parameters)} parameters, expected: {self.nr_of_parameters}",
                }
            case Callable() as func:  # type: ignore
                name = getattr(func, "__name__", repr(func))
                return {"reason": f"Function {name} is not a partial"}
            case _:
                return {"reason": f"Value {x} is not a partial"}


is_partial_p: Final[IsPartialPredicate] = IsPartialPredicate()


def is_partial_with_signature_p(*, nr_of_parameters: int) -> Predicate:
    return IsPartialPredicate(nr_of_parameters=nr_of_parameters)
