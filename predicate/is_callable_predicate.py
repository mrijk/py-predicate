from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, override

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
        return "is_callable_p"

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case Callable() as c:  # type: ignore
                annotations = c.__annotations__
                return_type = annotations["return"]

                if return_type != self.return_type:
                    return {"reason": f"Wrong return type: {return_type}"}

                return {"reason": "tbd"}
            case _:
                return {"reason": f"{x} is not a Callable"}
