from typing import Iterator

from predicate.eq_predicate import EqPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate, XorPredicate


def generate_predicate(predicate_type: type[Predicate], max_depth: int) -> Iterator[Predicate]:
    predicate_type_registry = {
        AndPredicate: generate_and_predicates,
        EqPredicate: generate_eq_predicates,
        NePredicate: generate_ne_predicates,
        NotPredicate: generate_not_predicates,
        OrPredicate: generate_or_predicates,
        XorPredicate: generate_xor_predicates,
    }

    if generator := predicate_type_registry.get(predicate_type):
        yield from generator(max_depth=max_depth)
    else:
        yield from []
        # raise ValueError(f"No generator defined for predicate type {predicate_type}")


def generate_and_predicates(max_depth: int) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    left_predicates = random_predicates(max_depth=max_depth - 1)
    right_predicates = random_predicates(max_depth=max_depth - 1)

    while True:
        yield AndPredicate(left=next(left_predicates), right=next(right_predicates))


def generate_eq_predicates(max_depth: int) -> Iterator:
    while True:
        yield EqPredicate(2)


def generate_ne_predicates(max_depth: int) -> Iterator:
    while True:
        yield NePredicate(2)


def generate_not_predicates(max_depth: int) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1)
    while True:
        yield NotPredicate(predicate=next(predicates))


def generate_or_predicates(max_depth: int) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    left_predicates = random_predicates(max_depth=max_depth - 1)
    right_predicates = random_predicates(max_depth=max_depth - 1)

    while True:
        yield OrPredicate(left=next(left_predicates), right=next(right_predicates))


def generate_xor_predicates(max_depth: int) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    left_predicates = random_predicates(max_depth=max_depth - 1)
    right_predicates = random_predicates(max_depth=max_depth - 1)

    while True:
        yield XorPredicate(left=next(left_predicates), right=next(right_predicates))
