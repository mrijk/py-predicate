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
        return match(iterable, predicates=self.predicates)

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
        return {"reason": reason(iterable, predicates=self.predicates)}


def match_p[T](*predicates: Callable) -> MatchPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return MatchPredicate(predicates=list(predicates))


def reason(iterable: Iterable, *, predicates: list[Callable] | list[Predicate]) -> dict:
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate():
            return predicate.explain(iterable, predicates=rest_predicates)
        case Predicate():
            item, *rest = iterable
            return predicate.explain(item)
        case _:
            raise NotImplementedError


def match(iterable: Iterable, *, predicates: list[Callable]) -> bool:
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate():
            return predicate(iterable, predicates=rest_predicates)
        case Predicate():
            if not iterable:
                return False
            item, *rest = iterable
            if rest_predicates:
                return predicate(item) and match(rest, predicates=rest_predicates)
            return predicate(item)
        case _:
            return predicate(iterable, predicates=rest_predicates)


def add_doc(docstring):
    def decorator(func):
        func.__doc__ = docstring
        return func

    return decorator


def repeat(m: int, n: int, predicate: Predicate) -> Callable:
    """Match exactly m to n instances of the given predicate."""

    @add_doc(f"repeat({m}, {n}, {predicate!r})")
    def _repeat(
        iterable: Iterable,
        *,
        predicates: list[Predicate],
    ) -> bool:
        for n_ in range(n, m - 1, -1):
            f = exactly_n(n_, predicate)
            if f(iterable, predicates=predicates):
                return True
        return False

    return _repeat


def exactly_n(n: int, predicate: Predicate) -> Callable:
    """Match exactly n instances of the given predicate."""

    @add_doc(f"exactly_n({n}, {predicate!r})")
    def _exactly_n(
        iterable: Iterable,
        *,
        predicates: list[Callable],
    ) -> bool:
        rest = iterable
        for _ in range(n):
            if not rest:
                return False

            item, *rest = rest
            if not predicate(item):
                return False
        return match(rest, predicates=predicates) if predicates else True

    return _exactly_n


def plus(predicate: Predicate) -> Callable:
    """Match at least one instance of the given predicate."""

    @add_doc(f"plus({predicate!r})")
    def _plus(iterable: Iterable, *, predicates: list[Callable]) -> bool:
        if not iterable:
            return False

        item, *rest = iterable
        return predicate(item) and star(predicate)(rest, predicates=predicates)

    return _plus


def star(predicate: Predicate) -> Callable:
    """Match any instances of the given predicate."""

    @add_doc(f"star({predicate!r})")
    def _star(iterable: Iterable, *, predicates: list[Callable]) -> bool:
        if not iterable:
            return not predicates
        item, *rest = iterable
        if predicate(item):
            if _star(rest, predicates=predicates):
                return True
            if predicates:
                matched = match(rest, predicates=predicates)
                return match(iterable, predicates=predicates) if not matched else True  # backtrack
        return match(iterable, predicates=predicates) if predicates else False

    return _star


@dataclass
class OptionalPredicate[T](Predicate[T]):
    """Match 0 or 1 instances of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Callable]) -> bool:
        if not iterable:
            return True
        item, *rest = iterable
        if predicates:
            return (self.predicate(item) and match(rest, predicates=predicates)) or match(
                iterable, predicates=predicates
            )
        return self.predicate(item)

    def __repr__(self) -> str:
        return f"optional({self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        item, *rest = iterable

        if predicates:
            if not self.predicate(item):
                return reason(iterable, predicates=predicates)
            if not match(rest, predicates=predicates):  # type: ignore
                return reason(rest, predicates=predicates)

        return self.predicate.explain_failure(item)


def optional(predicate: Predicate) -> Callable:
    """Match 0 or 1 instances of the given predicate."""
    return OptionalPredicate(predicate=predicate)


wildcard = star(always_true_p)
