from collections.abc import Callable

import reactivex as rx
import reactivex.operators as ops

from predicate.predicate import Predicate


def filter_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that only lets through items satisfying the predicate."""
    return ops.filter(predicate)
