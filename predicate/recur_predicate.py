from dataclasses import dataclass
from itertools import pairwise, takewhile
from typing import Callable, Iterable, Iterator, override

from more_itertools import ilen, spy

from predicate import always_true_p
from predicate.predicate import Explanation, Predicate


@dataclass
class RecurPredicate[T](Predicate[Iterable[T]]):
    """A predicate class that models the 'recursive' predicate."""

    empty: bool
    predicate_1: Predicate[T]
    predicate_n: Callable[[T], Predicate[T]]

    def __call__(self, iterable: Iterable[T]) -> bool:
        head, _ = spy(iterable, 2)

        match head:
            case []:
                return self.empty
            case [x]:
                return self.predicate_1(x)
            case _:
                return all(self.predicate_n(a)(b) for a, b in pairwise(iterable))

    @override
    def explain_failure(self, iterable: Iterable[T]) -> Explanation:
        items = list(iterable)

        match items:
            case []:
                return {"reason": "Empty iterable is not allowed"}
            case [x]:
                return {"reason": self.predicate_1.explain(x)}
            case _:
                a, b = next(pair for pair in pairwise(items) if not self.predicate_n(pair[0])(pair[1]))
                return {"reason": self.predicate_n(a).explain(b), "pair": (a, b)}

    @override
    def consumes(self, iterable: Iterable[T]) -> Iterator[int]:
        head, _ = spy(iterable, 2)

        match head:
            case []:
                yield 0
            case [x]:
                yield 0
                yield 1 if self.predicate_1(x) else 0
            case _:
                consumed = takewhile(lambda pair: self.predicate_n(pair[0])(pair[1]), pairwise(iterable))
                yield from range(ilen(consumed) + 2)


def recur_p[T](
    predicate_n: Callable[[T], Predicate[T]],
    empty: bool = True,
    predicate_1: Predicate[T] = always_true_p,
) -> Predicate[Iterable[T]]:
    """Return True if the recursively evaluated predicate is True, otherwise False."""
    return RecurPredicate(empty=empty, predicate_1=predicate_1, predicate_n=predicate_n)
