from collections.abc import Callable

import reactivex as rx
import reactivex.operators as ops

from predicate.predicate import Predicate


def filter_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that only lets through items satisfying the predicate."""
    return ops.filter(predicate)


def take_while_p[T](predicate: Predicate[T], inclusive: bool = False) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that lets through items as long as the predicate holds."""
    return ops.take_while(predicate, inclusive)


def skip_while_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that skips items as long as the predicate holds."""
    return ops.skip_while(predicate)


def partition_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], list[rx.Observable[T]]]:
    """Return an Rx operator that splits a stream into [matching, non-matching] observables."""
    return ops.partition(predicate)


def all_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[bool]]:
    """Return an Rx operator that emits whether all items satisfy the predicate (wraps ops.all)."""
    return ops.all(predicate)


def some_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[bool]]:
    """Return an Rx operator that emits whether any item satisfies the predicate (wraps ops.some)."""
    return ops.some(predicate)


def count_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[int]]:
    """Return an Rx operator that emits the number of items satisfying the predicate."""
    return ops.count(predicate)


def first_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that emits the first item satisfying the predicate, or errors if there is none."""
    return ops.first(predicate)


def last_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that emits the last item satisfying the predicate, or errors if there is none."""
    return ops.last(predicate)


def single_p[T](predicate: Predicate[T]) -> Callable[[rx.Observable[T]], rx.Observable[T]]:
    """Return an Rx operator that emits the only item satisfying the predicate, or errors if not exactly one."""
    return ops.single(predicate)
