from dataclasses import dataclass
from typing import Iterable, override

from predicate import always_true_p
from predicate.predicate import Predicate


@dataclass
class MatchPredicate[T](Predicate[T]):
    """A predicate class that models 'match iterable' predicate."""

    predicates: list[Predicate]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return match(iterable, predicates=self.predicates)

    def __repr__(self) -> str:
        param = ", ".join(repr(predicate) for predicate in self.predicates)
        return f"match_p({param})"

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        return {"reason": reason(iterable, predicates=self.predicates)}


def match_p[T](*predicates: Predicate) -> MatchPredicate[T]:
    """Return True if the predicate holds for each item in the iterable, otherwise False."""
    return MatchPredicate(predicates=list(predicates))


def reason(iterable: Iterable, *, predicates: list[Predicate]) -> dict:
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            return predicate.explain(iterable, predicates=rest_predicates)
        case Predicate():
            item, *rest = iterable
            if not predicate(item):
                return predicate.explain(item)
            return reason(rest, predicates=rest_predicates)
        case _:
            raise NotImplementedError


def match(iterable: Iterable, *, predicates: list[Predicate]) -> bool:
    predicate, *rest_predicates = predicates
    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            return predicate(iterable, predicates=rest_predicates)
        case Predicate():
            if not iterable:
                return False
            item, *rest = iterable
            if rest_predicates:
                return predicate(item) and match(rest, predicates=rest_predicates)
            return predicate(item)
        case _:
            raise NotImplementedError


@dataclass
class RepeatPredicate[T](Predicate[T]):
    """Match exactly m to n instances of the given predicate."""

    m: int
    n: int
    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
        for n in range(self.n, self.m - 1, -1):
            f = exactly_n(n, self.predicate)
            if f(iterable, predicates=predicates):
                return True
        return False

    def __repr__(self) -> str:
        return f"repeat({self.m}, {self.n}, {self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        return {"reason": f"Expected between {self.m} and {self.n} matches of predicate `{self.predicate!r}`"}


def repeat(m: int, n: int, predicate: Predicate) -> Predicate:
    """Match exactly m to n instances of the given predicate."""
    return RepeatPredicate(m=m, n=n, predicate=predicate)


@dataclass
class ExactlyPredicate[T](Predicate[T]):
    """Match exactly n instances of the given predicate."""

    n: int
    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
        rest = iterable
        for _ in range(self.n):
            if not rest:
                return False

            item, *rest = rest
            if not self.predicate(item):
                return False
        return match(rest, predicates=predicates) if predicates else True

    def __repr__(self) -> str:
        return f"exactly({self.n}, {self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        rest = iterable
        for _ in range(self.n):
            if not rest:
                return {"reason": f"Not enough items in iterable, expected {self.n}"}

            item, *rest = rest
            if not self.predicate(item):
                return self.predicate.explain(item)

        return reason(rest, predicates=predicates)


def exactly_n(n: int, predicate: Predicate) -> Predicate:
    """Match exactly n instances of the given predicate."""
    return ExactlyPredicate(n=n, predicate=predicate)


@dataclass
class PlusPredicate[T](Predicate[T]):
    """Match at least one instance of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
        if not iterable:
            return False

        item, *rest = iterable
        return self.predicate(item) and star(self.predicate)(rest, predicates=predicates)

    def __repr__(self) -> str:
        return f"plus({self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        if not iterable:
            return {"reason": f"Iterable should have at least one element to match against {self.predicate!r}"}

        item, *rest = iterable
        if not self.predicate(item):
            return {"reason": f"tbd {self.predicate!r}"}

        return {"reason": f"`{self.predicate!r}`"}


def plus(predicate: Predicate) -> Predicate:
    """Match at least one instance of the given predicate."""
    return PlusPredicate(predicate=predicate)


@dataclass
class StarPredicate[T](Predicate[T]):
    """Match any instances of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
        if not iterable:
            return not predicates
        item, *rest = iterable
        if self.predicate(item):
            if self(rest, predicates=predicates):
                return True
            if predicates:
                matched = match(rest, predicates=predicates)
                return match(iterable, predicates=predicates) if not matched else True  # backtrack
        return match(iterable, predicates=predicates) if predicates else False

    def __repr__(self) -> str:
        return f"star({self.predicate!r})"

    @override
    def explain_failure(self, iterable: Iterable[T], *, predicates: list[Predicate]) -> dict:  # type: ignore
        return {"reason": f"tbd {self.predicate!r}"}


def star(predicate: Predicate) -> Predicate:
    """Match any instances of the given predicate."""
    return StarPredicate(predicate=predicate)


@dataclass
class OptionalPredicate[T](Predicate[T]):
    """Match 0 or 1 instances of the given predicate."""

    predicate: Predicate

    def __call__(self, iterable: Iterable, *, predicates: list[Predicate]) -> bool:
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


def optional(predicate: Predicate) -> Predicate:
    """Match 0 or 1 instances of the given predicate."""
    return OptionalPredicate(predicate=predicate)


wildcard = star(always_true_p)
