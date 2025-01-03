from collections.abc import Iterator
from functools import singledispatch
from random import choice, randint

from predicate import eq_p, ge_p, gt_p, le_p, lt_p, ne_p
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import Predicate


@singledispatch
def mutations(predicate: Predicate, false_set: list, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    """Return nr of mutations."""
    yield predicate


def int_value_mutations(n: int, values: list, nr: int) -> Iterator[int]:
    yield choice(values)
    yield n - randint(0, 10)
    yield n + randint(0, 10)


@mutations.register
def _(predicate: EqPredicate, false_set: list, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (eq_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _(predicate: NePredicate, false_set, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (ne_p(v) for v in int_value_mutations(n, false_set, nr))
        case _:
            pass


@mutations.register
def _(predicate: GePredicate, false_set, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (ge_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _(predicate: GtPredicate, false_set, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (gt_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _(predicate: LePredicate, false_set, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (le_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _(predicate: LtPredicate, false_set, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (lt_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass
