from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, override

from more_itertools import first

from predicate.predicate import Predicate


@dataclass
class IsCallablePredicate[T](Predicate[T]):
    """A predicate class that models the is_callable predicate."""

    params: list
    return_type: Any

    def __call__(self, x: Any) -> bool:
        match x:
            case Callable() as c:  # type: ignore
                annotations = c.__annotations__
                return_type = annotations["return"]
                params = [param for key, param in annotations.items() if key != "return"]

                return params == self.params and return_type == self.return_type
            case _:
                return False

    def __repr__(self) -> str:
        return_type = self.return_type.__name__
        return f"is_callable_p([], {return_type})"

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case Callable() as c:  # type: ignore
                annotations = c.__annotations__
                return_type = annotations["return"]

                if return_type != self.return_type:
                    return {"reason": f"Wrong return type: {return_type}"}

                params = [param for key, param in annotations.items() if key != "return"]
                combined = zip(self.params, params, strict=False)
                different = first(
                    (expected_param, param) for expected_param, param in combined if expected_param != param
                )
                expected, actual = different

                return {"reason": f"Got type {actual.__name__}, expected {expected.__name__}"}
            case _:
                return {"reason": f"{x} is not a Callable"}


def is_callable_p(params: list, return_type: Any) -> IsCallablePredicate:
    return IsCallablePredicate(params, return_type)
