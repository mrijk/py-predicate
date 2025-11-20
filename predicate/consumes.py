from typing import Any, Iterable, Iterator

from more_itertools import spy

from predicate.predicate import Predicate


def consumes(predicate: Predicate, iterable: Iterable[Any]) -> Iterator[int]:
    head, _ = spy(iterable, 1)
    if head:
        yield from predicate.consumes(iterable)
    else:
        yield 0
