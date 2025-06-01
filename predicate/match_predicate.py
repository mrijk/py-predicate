from dataclasses import dataclass
from types import FunctionType
from typing import Callable, Iterable, override

from predicate import always_true_p
from predicate.predicate import Predicate


@dataclass
class MatchPredicate[T](Predicate[T]):
    """A predicate class that models 'match iterable' predicate."""

    predicates: list[Callable]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return match(self.predicates, iterable)

    def __repr__(self) -> str:
        def callable_repr() -> Iterable[str]:
            for predicate in self.predicates:
                match predicate:
                    case Predicate() as p:
                        yield repr(p)
                    case FunctionType() as f:
                        yield f.__doc__ or "unknown()"

        param = ", ".join(callable_repr())

        return f"match_p({param})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        # TODO
        return {"reason": "Tbd"}


def match_p[T](*predicates: Callable) -> MatchPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return MatchPredicate(predicates=list(predicates))


def match(predicates: list[Callable], iterable: Iterable) -> bool:
    predicate, *rest_predicates = predicates
    match predicate:
        case Predicate():
            if not iterable:
                return False
            item, *rest = iterable
            if rest_predicates:
                return predicate(item) and match(rest_predicates, rest)
            return predicate(item)
        case _:
            return predicate(rest_predicates, iterable)


def add_doc(docstring):
    def decorator(func):
        func.__doc__ = docstring
        return func

    return decorator


def repeat(m: int, n: int, predicate: Predicate) -> Callable:
    """Match exactly m to n instances of the given predicate."""

    @add_doc(f"repeat({m}, {n}, {predicate!r})")
    def _repeat(predicates: list[Predicate], iterable: Iterable) -> bool:
        for n_ in range(n, m - 1, -1):
            f = exactly_n(n_, predicate)
            if f(predicates, iterable):
                return True
        return False

    return _repeat


def exactly_n(n: int, predicate: Predicate) -> Callable:
    """Match exactly n instances of the given predicate."""

    @add_doc(f"exactly_n({n}, {predicate!r})")
    def _exactly_n(predicates: list[Callable], iterable: Iterable) -> bool:
        rest = iterable
        for _ in range(n):
            if not rest:
                return False

            item, *rest = rest
            if not predicate(item):
                return False
        return match(predicates, rest) if predicates else True

    return _exactly_n


def plus(predicate: Predicate) -> Callable:
    """Match at least one instance of the given predicate."""

    @add_doc(f"plus({predicate!r})")
    def _plus(predicates: list[Callable], iterable: Iterable) -> bool:
        if not iterable:
            return False

        item, *rest = iterable
        return predicate(item) and star(predicate)(predicates, rest)

    return _plus


def star(predicate: Predicate) -> Callable:
    """Match any instances of the given predicate."""

    @add_doc(f"star({predicate!r})")
    def _star(predicates: list[Callable], iterable: Iterable) -> bool:
        if not iterable:
            return not predicates
        item, *rest = iterable
        if predicate(item):
            if _star(predicates, rest):
                return True
            if predicates:
                matched = match(predicates, rest)
                return match(predicates, iterable) if not matched else True  # backtrack
        return match(predicates, iterable) if predicates else False

    return _star


def optional(predicate: Predicate) -> Callable:
    """Match 0 or 1 instances of the given predicate."""

    @add_doc(f"optional({predicate!r})")
    def _optional(predicates: list[Callable], iterable: Iterable) -> bool:
        if not iterable:
            return True
        item, *rest = iterable
        if predicates:
            return (predicate(item) and match(predicates, rest)) or match(predicates, iterable)
        return predicate(item)

    return _optional


wildcard = star(always_true_p)
