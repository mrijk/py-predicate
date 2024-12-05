import random
import sys
import uuid
from collections.abc import Iterator
from datetime import datetime, timedelta
from functools import singledispatch
from itertools import cycle

import exrex  # type: ignore
from more_itertools import interleave, powerset_of_sets, random_combination_with_replacement, take

from predicate.any_predicate import AnyPredicate
from predicate.generator.helpers import (
    generate_anys,
    generate_ints,
    generate_strings,
    generate_uuids,
    random_anys,
    random_complex_numbers,
    random_datetimes,
    random_dicts,
    random_floats,
    random_ints,
    random_strings,
    random_uuids,
)
from predicate.has_key_predicate import HasKeyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    IsEmptyPredicate,
    IsFalsyPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    IsTruthyPredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    OrPredicate,
    Predicate,
    always_false_p,
)
from predicate.regex_predicate import RegexPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import InPredicate, IsRealSubsetPredicate, IsSubsetPredicate, NotInPredicate
from predicate.standard_predicates import AllPredicate
from predicate.tuple_of_predicate import TupleOfPredicate


@singledispatch
def generate_true[T](predicate: Predicate[T]) -> Iterator[T]:
    """Generate values that satisfy this predicate."""
    raise ValueError("Please register generator for correct predicate type")


@generate_true.register
def generate_all_p(all_predicate: AllPredicate) -> Iterator:
    yield []

    predicate = all_predicate.predicate

    while True:
        max_length = random.randint(1, 10)

        values = take(max_length, generate_true(predicate))
        yield random_combination_with_replacement(values, max_length)

        values = take(max_length, generate_true(predicate))
        yield set(random_combination_with_replacement(values, max_length))

        values = take(max_length, generate_true(predicate))
        yield list(random_combination_with_replacement(values, max_length))


@generate_true.register
def generate_always_true(_predicate: AlwaysTruePredicate) -> Iterator:
    yield True


@generate_true.register
def generate_and(predicate: AndPredicate) -> Iterator:
    if optimize(predicate) == always_false_p:
        yield from []
    else:
        yield from (item for item in generate_true(predicate.left) if predicate.right(item))
        yield from (item for item in generate_true(predicate.right) if predicate.left(item))


@generate_true.register
def generate_eq(predicate: EqPredicate) -> Iterator:
    yield predicate.v


@generate_true.register
def generate_false(_predicate: AlwaysFalsePredicate) -> Iterator:
    yield from []


@generate_true.register
def generate_ge(predicate: GePredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt + timedelta(days=days) for days in range(0, 5))
        case float():
            yield from random_floats(lower=predicate.v)
        case int():
            yield from random_ints(lower=predicate.v)
        case str():
            yield from generate_strings(predicate)
        case uuid.UUID():
            yield from generate_uuids(predicate)


@generate_true.register
def generate_gt(predicate: GtPredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt + timedelta(days=days) for days in range(1, 6))
        case float():
            yield from random_floats(lower=predicate.v + sys.float_info.epsilon)
        case int():
            yield from random_ints(lower=predicate.v + 1)
        case str():
            yield from generate_strings(predicate)
        case uuid.UUID():
            yield from generate_uuids(predicate)


@generate_true.register
def generate_has_key(predicate: HasKeyPredicate) -> Iterator:
    key = predicate.key
    for random_dict, value in zip(random_dicts(), random_anys(), strict=False):
        yield random_dict | {key: value}


@generate_true.register
def generate_le(predicate: LePredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt - timedelta(days=days) for days in range(0, 5))
        case float():
            yield from random_floats(upper=predicate.v)
        case int():
            yield from random_ints(upper=predicate.v)
        case str():
            yield from generate_strings(predicate)
        case uuid.UUID():
            yield from generate_uuids(predicate)


@generate_true.register
def generate_subset(predicate: IsSubsetPredicate) -> Iterator:
    yield from powerset_of_sets(predicate.v)


@generate_true.register
def generate_real_subset(predicate: IsRealSubsetPredicate) -> Iterator:
    yield from (v for v in powerset_of_sets(predicate.v) if v != predicate.v)


@generate_true.register
def generate_in(predicate: InPredicate) -> Iterator:
    yield from predicate.v


@generate_true.register
def generate_is_empty(_predicate: IsEmptyPredicate) -> Iterator:
    yield from ([], {}, (), "", set())


@generate_true.register
def generate_lt(predicate: LtPredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt - timedelta(days=days) for days in range(0, 5))
        case float():
            yield from random_floats(upper=predicate.v - sys.float_info.epsilon)
        case int():
            yield from random_ints(upper=predicate.v - 1)
        case str():
            yield from generate_strings(predicate)
        case uuid.UUID():
            yield from generate_uuids(predicate)


@generate_true.register
def generate_ne(predicate: NePredicate) -> Iterator:
    yield not predicate.v


@generate_true.register
def generate_none(_predicate: IsNonePredicate) -> Iterator:
    yield None


@generate_true.register
def generate_not_in(predicate: NotInPredicate) -> Iterator:
    for item in predicate.v:
        match item:
            case int():
                yield from generate_ints(predicate)
            case str():
                yield from generate_strings(predicate)


@generate_true.register
def generate_not_none(predicate: IsNotNonePredicate) -> Iterator:
    yield from generate_anys(predicate)


@generate_true.register
def generate_or(predicate: OrPredicate) -> Iterator:
    yield from interleave(generate_true(predicate.left), generate_true(predicate.right))


@generate_true.register
def generate_regex(predicate: RegexPredicate) -> Iterator:
    yield from exrex.generate(predicate.pattern)


@generate_true.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from (False, 0, (), "", {})


@generate_true.register
def generate_truthy(_predicate: IsTruthyPredicate) -> Iterator:
    yield from (True, 1, "true", {1}, 3.14)


@generate_true.register
def generate_is_instance_p(predicate: IsInstancePredicate) -> Iterator:
    klass = predicate.klass[0]  # type: ignore
    if klass is str:
        yield from random_strings()
    elif klass is bool:
        yield from cycle((False, True))
    elif klass is complex:
        yield from random_complex_numbers()
    elif klass == datetime:
        yield from random_datetimes()
    elif klass is dict:
        yield from random_dicts()
    elif klass is float:
        yield from random_floats()
    elif klass == uuid.UUID:
        yield from random_uuids()
    elif klass is int:
        yield from random_ints()
    elif klass is set:
        yield from (set(), {1, 2, 3}, {"foo", "bar"})


@generate_true.register
def generate_any_p(any_predicate: AnyPredicate) -> Iterator:
    predicate = any_predicate.predicate
    values = take(10, generate_true(predicate))

    # TODO: also add some values for which predicate isn't valid

    yield random_combination_with_replacement(values, 5)

    yield set(random_combination_with_replacement(values, 5))


@generate_true.register
def generate_tuple_of_p(tuple_of_predicate: TupleOfPredicate) -> Iterator:
    predicates = tuple_of_predicate.predicates

    yield from zip(*(generate_true(predicate) for predicate in predicates), strict=False)


@generate_true.register
def generate_set_of_p(set_of_predicate: SetOfPredicate) -> Iterator:
    predicate = set_of_predicate.predicate

    values = take(10, generate_true(predicate))

    yield set(random_combination_with_replacement(values, 5))
