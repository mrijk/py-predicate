from collections.abc import Iterator
from functools import singledispatch
from random import choice, randint

from predicate import eq_p, ne_p
from predicate.eq_predicate import EqPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import Predicate


@singledispatch
def mutations(predicate: Predicate, false_set: list, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    """Return nr of mutations."""
    yield predicate


@mutations.register
def _(predicate: EqPredicate, false_set: list, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield eq_p(choice(true_set))
            yield eq_p(n - randint(0, 10))
            yield eq_p(n + randint(0, 10))
        case _:
            pass


@mutations.register
def _(predicate: NePredicate, false_set, true_set: list, nr: int = 3) -> Iterator[Predicate]:
    match predicate.v:
        case int(n):
            yield ne_p(choice(false_set))
            yield ne_p(n - randint(0, 10))
            yield ne_p(n + randint(0, 10))
        case _:
            pass
