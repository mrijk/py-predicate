import asyncio
from dataclasses import dataclass, field
from typing import Callable, Iterator, overload, override

from predicate.predicate import Predicate


def _undefined() -> Iterator:
    raise ValueError("Please register generator type")


@dataclass
class FnPredicate[T](Predicate[T]):
    """A predicate class that can hold a function."""

    predicate_fn: Callable[[T], bool]
    generate_false_fn: Callable[[], Iterator] = _undefined
    generate_true_fn: Callable[[], Iterator] = _undefined
    _call: Callable[[T], bool] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        from predicate.is_async_predicate import is_async_p

        if is_async_p(self.predicate_fn):
            self._call = lambda x: asyncio.run(self.predicate_fn(x))  # type: ignore[arg-type]
        else:
            self._call = self.predicate_fn

    def __call__(self, x: T) -> bool:
        return self._call(x)

    def __repr__(self) -> str:
        return f"fn_p(predicate_fn={self.predicate_fn.__name__})"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"reason": f"Function returned False for value {x}"}


def fn_p[T](
    fn: Callable[[T], bool],
    generate_false_fn: Callable[[], Iterator[T]] = _undefined,
    generate_true_fn: Callable[[], Iterator[T]] = _undefined,
) -> Predicate[T]:
    """Return the boolean value of the function call."""
    return FnPredicate(predicate_fn=fn, generate_false_fn=generate_false_fn, generate_true_fn=generate_true_fn)


@overload
def as_predicate[T](fn: Callable[[T], bool]) -> Predicate[T]: ...


@overload
def as_predicate[T](
    fn: None = None,
    *,
    generate_true_fn: Callable[[], Iterator[T]] = _undefined,
    generate_false_fn: Callable[[], Iterator[T]] = _undefined,
) -> Callable[[Callable[[T], bool]], Predicate[T]]: ...


def as_predicate[T](
    fn: Callable[[T], bool] | None = None,
    *,
    generate_true_fn: Callable[[], Iterator[T]] = _undefined,
    generate_false_fn: Callable[[], Iterator[T]] = _undefined,
) -> Predicate[T] | Callable[[Callable[[T], bool]], Predicate[T]]:
    def decorator(f: Callable[[T], bool]) -> Predicate[T]:
        return fn_p(f, generate_true_fn=generate_true_fn, generate_false_fn=generate_false_fn)

    return decorator if fn is None else decorator(fn)
