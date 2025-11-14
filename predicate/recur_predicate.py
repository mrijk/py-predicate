from dataclasses import dataclass
from itertools import takewhile
from typing import Callable, Iterable, override

from more_itertools import ilen, pairwise, spy

from predicate import always_true_p
from predicate.predicate import Predicate


@dataclass
class RecurPredicate[T](Predicate[Iterable[T]]):
    """A predicate class that models the 'recursive' predicate."""

    predicate_0: Predicate[T]
    predicate_1: Predicate[T]
    predicate_n: Callable[[T], Predicate[T]]

    def __call__(self, iterable: Iterable[T]) -> bool:
        head, _ = spy(iterable, 2)

        match head:
            case []:
                return self.predicate_0()
            case [x]:
                return self.predicate_1(x)
            case _:
                return all(self.predicate_n(a)(b) for a, b in pairwise(iterable))

    @override
    def consumes(self, iterable: Iterable[T]) -> tuple[int, int]:
        head, _ = spy(iterable, 2)

        match head:
            case []:
                return 0, 0
            case [x]:
                return (1, 1) if self.predicate_1(x) else (0, 0)
            case _:
                consumed = takewhile(lambda pair: self.predicate_n(pair[0])(pair[1]), pairwise(iterable))
                return 1, ilen(consumed) + 1


def recur_p[T](
    predicate_n: Callable[[T], Predicate[T]],
    predicate_0: Predicate[T] = always_true_p,
    predicate_1: Predicate[T] = always_true_p,
) -> Predicate[Iterable[T]]:
    """Return True if the recursively evaluated predicate is True, otherwise False."""
    return RecurPredicate(predicate_0=predicate_0, predicate_1=predicate_1, predicate_n=predicate_n)
