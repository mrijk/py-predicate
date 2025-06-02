from dataclasses import dataclass
from typing import Iterator, override

from predicate.predicate import Predicate


def join_with_or(s: list[str]) -> str:
    first = s[:-1]
    last = s[-1]
    if first:
        return f"{', '.join(first)} or {last}"
    return last


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
        def class_names() -> Iterator[str]:
            match self.instance_klass:
                case tuple() as klasses:
                    for klass in klasses:
                        yield klass.__name__
                case _:
                    yield self.instance_klass.__name__

        klasses = join_with_or(list(class_names()))

        return {"reason": f"{x} is not an instance of type {klasses}"}
