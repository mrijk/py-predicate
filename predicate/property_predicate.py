import sys
from dataclasses import dataclass
from typing import Any, Callable, override

from predicate.predicate import Predicate


@dataclass
class PropertyPredicate[T](Predicate[T]):
    """A predicate class that wraps a boolean property."""

    getter: property

    def __init__(self, getter: Callable[..., Any]):
        self.getter = getter  # type: ignore

    def __call__(self, obj: T) -> bool:
        if sys.version_info.minor > 12:
            if not hasattr(obj, self.getter.__name__):  # type: ignore[attr-defined,unused-ignore]
                return False

        return self.getter.fget(obj)  # type: ignore

    def __repr__(self) -> str:
        return "property_p()"

    @override
    def explain_failure(self, obj: T) -> dict[str, Any]:
        object_type = type(obj).__name__
        if sys.version_info.minor > 12:
            property_name = self.getter.__name__  # type: ignore[attr-defined,unused-ignore]
            if not hasattr(obj, property_name):
                return {"reason": f"Object {object_type} has no property {property_name}"}
        return {"reason": f"Property in Object {object_type} returned False"}


def property_p(getter: Callable[..., Any]) -> Predicate[Any]:
    return PropertyPredicate(getter=getter)
