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
def mutations[T](predicate: Predicate[T], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    """Return nr of mutations."""
    yield predicate


def _int_value_mutations(n: int, values: list[Any], nr: int) -> Iterator[int]:
    yield choice(values)
    yield n - randint(0, 10)
    yield n + randint(0, 10)


@mutations.register(AndPredicate)
def _[T](predicate: AndPredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    yield from mutations(predicate.left, false_set=false_set, true_set=true_set, nr=nr)
    yield from mutations(predicate.right, false_set=false_set, true_set=true_set, nr=nr)


@mutations.register(OrPredicate)
def _[T](predicate: OrPredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    yield from mutations(predicate.left, false_set=false_set, true_set=true_set, nr=nr)
    yield from mutations(predicate.right, false_set=false_set, true_set=true_set, nr=nr)


@mutations.register(XorPredicate)
def _[T](predicate: XorPredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    yield from mutations(predicate.left, false_set=false_set, true_set=true_set, nr=nr)
    yield from mutations(predicate.right, false_set=false_set, true_set=true_set, nr=nr)


@mutations.register(EqPredicate)
def _[T](predicate: EqPredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[Any]]:
    match predicate.v:
        case int(n):
            yield from (eq_p(v) for v in _int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register(NePredicate)
def _[T](predicate: NePredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[Any]]:
    match predicate.v:
        case int(n):
            yield from (ne_p(v) for v in _int_value_mutations(n, false_set, nr))
        case _:
            pass


@mutations.register(GePredicate)
def _[T](predicate: GePredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    match predicate.v:
        case int(n):
            yield from (ge_p(v) for v in _int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register(GtPredicate)
def _[T](predicate: GtPredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    match predicate.v:
        case int(n):
            yield from (gt_p(v) for v in _int_value_mutations(n, false_set, nr))
        case _:
            pass


@mutations.register(LePredicate)
def _[T](predicate: LePredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    match predicate.v:
        case int(n):
            yield from (le_p(v) for v in _int_value_mutations(n, true_set, nr))
        case _:
            pass


@mutations.register(LtPredicate)
def _[T](predicate: LtPredicate[Any], false_set: list[T], true_set: list[T], nr: int = 3) -> Iterator[Predicate[T]]:
    match predicate.v:
        case int(n):
            yield from (lt_p(v) for v in _int_value_mutations(n, false_set, nr))
        case _:
            pass
