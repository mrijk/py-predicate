from collections.abc import Callable
from dataclasses import dataclass
from inspect import signature
from typing import Any, Final, override

from predicate.predicate import Predicate


def func_is_lambda(func: Callable) -> bool:
    lambda_name = (lambda: 0).__name__
    return func.__name__ == lambda_name


@dataclass
class IsLambdaPredicate[T](Predicate[T]):
    """A predicate class that models the is_lambda predicate."""

    nr_of_parameters: int | None = None

    def __call__(self, x: Any) -> bool:
        match x:
            case Callable() as func if func_is_lambda(func):  # type: ignore
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
    def explain_failure(self, x: Any) -> dict:
        match x:
            case Callable() as func if func_is_lambda(func):  # type: ignore
                sig = signature(func)
                return {
                    "reason": f"Lambda has {len(sig.parameters)} parameters, expected: {self.nr_of_parameters}",
                }
            case Callable() as func:  # type: ignore
                return {"reason": f"Function {func.__name__} is not a lambda"}
            case _:
                return {"reason": f"Value {x} is not a lambda"}


is_lambda_p: Final[IsLambdaPredicate] = IsLambdaPredicate()


def is_lambda_with_signature_p(*, nr_of_parameters: int) -> Predicate:
    return IsLambdaPredicate(nr_of_parameters=nr_of_parameters)
