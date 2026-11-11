from functools import singledispatch
from random import choice, randint
from typing import Any, Iterator

from predicate import eq_p, ge_p, gt_p, le_p, lt_p, ne_p
from predicate.and_predicate import AndPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.xor_predicate import XorPredicate


@singledispatch
def mutations[T](predicate: Predicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    """Return nr of mutations."""
    yield predicate


def int_value_mutations(n: int, values: list[Any], nr: int) -> Iterator[int]:
    yield choice(values)
    yield n - randint(0, 10)
    yield n + randint(0, 10)


@mutations.register
def _[T](predicate: AndPredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    yield from mutations(predicate.left, false_set=false_set, true_set=true_set, nr=nr)
    yield from mutations(predicate.right, false_set=false_set, true_set=true_set, nr=nr)


@mutations.register
def _[T](predicate: OrPredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    yield from mutations(predicate.left, false_set=false_set, true_set=true_set, nr=nr)
    yield from mutations(predicate.right, false_set=false_set, true_set=true_set, nr=nr)


@mutations.register
def _[T](predicate: XorPredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    yield from mutations(predicate.left, false_set=false_set, true_set=true_set, nr=nr)
    yield from mutations(predicate.right, false_set=false_set, true_set=true_set, nr=nr)


@mutations.register
def _[T](predicate: EqPredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (eq_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _[T](predicate: NePredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (ne_p(v) for v in int_value_mutations(n, false_set, nr))
        case _:
            pass


@mutations.register
def _[T](predicate: GePredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (ge_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _[T](predicate: GtPredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (gt_p(v) for v in int_value_mutations(n, false_set, nr))
        case _:
            pass


@mutations.register
def _[T](predicate: LePredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (le_p(v) for v in int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register
def _[T](predicate: LtPredicate, false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield from (lt_p(v) for v in int_value_mutations(n, false_set, nr))
        case _:
            pass
