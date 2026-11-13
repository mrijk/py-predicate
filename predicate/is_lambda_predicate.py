from collections.abc import Callable
from dataclasses import dataclass
from inspect import signature
from typing import Any, Final, override

from predicate.predicate import Predicate


def func_is_lambda(func: Callable[..., Any]) -> bool:
    lambda_name = (lambda: 0).__name__
    return getattr(func, "__name__", None) == lambda_name


@dataclass
class IsLambdaPredicate[T](Predicate[T]):
    """A predicate class that models the is_lambda predicate."""

    nr_of_parameters: int | None = None

    def __call__(self, x: Any) -> bool:
        match x:
            case func if callable(func) and func_is_lambda(func):
                if self.nr_of_parameters is not None:
                    sig = signature(func)
                    return len(sig.parameters) == self.nr_of_parameters
                return True
            case _:
                return False

    def __repr__(self) -> str:
        return (
            "is_lambda_p"
            if self.nr_of_parameters is None
            else f"is_lambda_with_signature_p(nr_of_parameters={self.nr_of_parameters})"
        )

    @override
    def explain_failure(self, x: Any) -> dict[str, Any]:
        match x:
            case func if callable(func) and func_is_lambda(func):
                sig = signature(func)
                return {
                    "reason": f"Lambda has {len(sig.parameters)} parameters, expected: {self.nr_of_parameters}",
                }
            case func if callable(func):
                return {"reason": f"Function {func.__name__} is not a lambda"}
            case _:
                return {"reason": f"Value {x} is not a lambda"}


is_lambda_p: Final[IsLambdaPredicate[Any]] = IsLambdaPredicate()


def is_lambda_with_signature_p(*, nr_of_parameters: int) -> Predicate[Any]:
    return IsLambdaPredicate(nr_of_parameters=nr_of_parameters)
