from dataclasses import dataclass
from typing import Any, Final, override

from predicate.predicate import Predicate


def is_named_tuple_class(klass: Any) -> bool:
    return isinstance(klass, type) and issubclass(klass, tuple) and hasattr(klass, "_fields")


@dataclass
class IsNamedTuplePredicate[T](Predicate[T]):
    """A predicate class that models the is_named_tuple predicate."""

    def __call__(self, x: Any) -> bool:
        return is_named_tuple_class(type(x))

    def __repr__(self) -> str:
        return "is_named_tuple_p"

    @override
    def explain_failure(self, x: Any) -> dict:
        return {"reason": f"{x} is not a named tuple"}


is_named_tuple_p: Final[IsNamedTuplePredicate] = IsNamedTuplePredicate()
