from typing import Any, Iterable

from more_itertools import spy

from predicate.predicate import Predicate


def consumes(predicate: Predicate, iterable: Iterable[Any]) -> tuple[int, int]:
    head, _ = spy(iterable, 1)
    return predicate.consumes(iterable) if head else (0, 0)
