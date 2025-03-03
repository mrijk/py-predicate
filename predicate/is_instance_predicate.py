from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class IsInstancePredicate[T](Predicate[T]):
    """A predicate class that models the 'isinstance' predicate."""

    instance_klass: type | tuple

    def __call__(self, x: object) -> bool:
        # This is different from standard Python behaviour: a False/True value is not an int!
        if isinstance(x, bool) and self.instance_klass[0] is int:  # type: ignore
            return False
        return isinstance(x, self.instance_klass)

    def __repr__(self) -> str:
        name = self.instance_klass[0].__name__  # type: ignore
        return f"is_{name}_p"

    @override
    def get_klass(self) -> type:
        return self.instance_klass  # type: ignore

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"{x} is not an instance of {self.instance_klass}"}
