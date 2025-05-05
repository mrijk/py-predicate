from dataclasses import dataclass
from typing import Callable, Iterator, override

from predicate.predicate import Predicate


def undefined() -> Iterator:
    raise ValueError("Please register generator type")


@dataclass
class FnPredicate[T](Predicate[T]):
    """A predicate class that can hold a function."""

    predicate_fn: Callable[[T], bool]
    generate_false_fn: Callable[[], Iterator] = undefined
    generate_true_fn: Callable[[], Iterator] = undefined

    def __call__(self, x: T) -> bool:
        return self.predicate_fn(x)

    def __repr__(self) -> str:
        return f"fn_p(predicate_fn={self.predicate_fn.__name__})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"Function returned False for value {x}"}
