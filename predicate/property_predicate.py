from dataclasses import dataclass
from typing import Callable, override

from predicate.predicate import Predicate


@dataclass
class PropertyPredicate[T](Predicate[T]):
    """A predicate class that wraps a boolean property."""

    getter: property

    def __init__(self, getter: Callable):
        self.getter = getter
        self._property_name = self.getter.__name__

    def __call__(self, obj: T) -> bool:
        if hasattr(obj, self.getter.__name__):
            return self.getter.fget(obj)  # type: ignore
        return False

    def __repr__(self) -> str:
        return f"property_p({self._property_name})"

    @override
    def explain_failure(self, obj: T) -> dict:
        if hasattr(obj, self.getter.__name__):
            return {"reason": f"Property {self._property_name} in Object {type(obj).__name__} returned False"}
        return {"reason": f"Object {type(obj).__name__} has no property {self._property_name}"}


def property_p(getter: Callable):
    return PropertyPredicate(getter=getter)
