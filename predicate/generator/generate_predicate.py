from typing import Any, Callable, Iterator

from predicate.all_predicate import AllPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate, XorPredicate


def generate_predicate(predicate_type: type[Predicate], max_depth: int, klass: type) -> Iterator[Predicate]:
    predicate_type_registry: dict[type, Any] = {
        # TODO: AllPredicate works on iterables
        # AllPredicate: generate_all_predicates,
        AndPredicate: generate_and_predicates,
        EqPredicate: generate_eq_predicates,
        GePredicate: generate_ge_predicates,
        GtPredicate: generate_gt_predicates,
        LePredicate: generate_le_predicates,
        LtPredicate: generate_lt_predicates,
        NePredicate: generate_ne_predicates,
        NotPredicate: generate_not_predicates,
        OrPredicate: generate_or_predicates,
        XorPredicate: generate_xor_predicates,
    }

    if generator := predicate_type_registry.get(predicate_type):
        yield from generator(max_depth=max_depth, klass=klass)
    else:
        yield from []
        # raise ValueError(f"No generator defined for predicate type {predicate_type}")


def random_values_of_type(klass: type) -> Iterator:
    from predicate.generator.helpers import random_bools, random_floats, random_ints, random_strings

    type_registry: dict[type, Callable[[], Iterator]] = {
        bool: random_bools,
        int: random_ints,
        float: random_floats,
        str: random_strings,
    }

    if generator := type_registry.get(klass):
        yield from generator()
    else:
        raise ValueError(f"No generator found for {klass}")


def generate_random_predicate_pairs(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_predicates

    left_predicates = random_predicates(max_depth=max_depth - 1, klass=klass)
    right_predicates = random_predicates(max_depth=max_depth - 1, klass=klass)

    return zip(left_predicates, right_predicates, strict=False)


def generate_all_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1, klass=klass)

    yield from (AllPredicate(predicate) for predicate in predicates)


def generate_and_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    yield from (left & right for left, right in generate_random_predicate_pairs(max_depth=max_depth, klass=klass))


def generate_eq_predicates(max_depth: int, klass: type) -> Iterator:
    yield from (EqPredicate(value) for value in random_values_of_type(klass))


def generate_ge_predicates(max_depth: int, klass: type) -> Iterator:
    yield from (GePredicate(value) for value in random_values_of_type(klass))


def generate_gt_predicates(max_depth: int, klass: type) -> Iterator:
    yield from (GtPredicate(value) for value in random_values_of_type(klass))


def generate_le_predicates(max_depth: int, klass: type) -> Iterator:
    yield from (LePredicate(value) for value in random_values_of_type(klass))


def generate_lt_predicates(max_depth: int, klass: type) -> Iterator:
    yield from (LtPredicate(value) for value in random_values_of_type(klass))


def generate_ne_predicates(max_depth: int, klass: type) -> Iterator:
    yield from (NePredicate(value) for value in random_values_of_type(klass))


def generate_not_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1, klass=klass)
    yield from (~predicate for predicate in predicates)


def generate_or_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    yield from (left | right for left, right in generate_random_predicate_pairs(max_depth=max_depth, klass=klass))


def generate_xor_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    yield from (left ^ right for left, right in generate_random_predicate_pairs(max_depth=max_depth, klass=klass))
