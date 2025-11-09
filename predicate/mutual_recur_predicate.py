from dataclasses import dataclass
from typing import Callable, Iterable

from more_itertools import pairwise, spy

from predicate import always_true_p
from predicate.predicate import Predicate


@dataclass
class MutualRecurPredicate[T](Predicate[T]):
    """A predicate class that models the 'mutually recursive' predicate."""

    predicate_0: Predicate[T]
    predicate_1: Predicate[T]
    predicate_n: Callable[[T], tuple]

    def __call__(self, iterable: Iterable[T]) -> bool:
        head, _ = spy(iterable, 2)

        match head:
            case []:
                return self.predicate_0()
            case [x]:
                return self.predicate_1(x)
            case _:
                predicate_n = self.predicate_n
                for a, b in pairwise(iterable):
                    predicate, recur_predicate = predicate_n(a)
                    if not predicate(b):
                        return False
                    predicate_n = recur_predicate.predicate_n
                return True


def mutual_recur_p[T](
    predicate_n: Callable[[T], tuple],
    predicate_0: Predicate[T] = always_true_p,
    predicate_1: Predicate[T] = always_true_p,
) -> Predicate[T]:
    """Return True if the mutually recursive evaluated predicate is True, otherwise False."""
    return MutualRecurPredicate(predicate_0=predicate_0, predicate_1=predicate_1, predicate_n=predicate_n)
