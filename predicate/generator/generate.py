import math
import random
import string
import sys
import uuid
from collections.abc import Iterator
from datetime import datetime, timedelta
from functools import singledispatch
from itertools import count
from random import choices

import exrex  # type: ignore
from more_itertools import interleave, random_combination_with_replacement, repeatfunc, take

from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsFalsyPredicate,
    IsInstancePredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    IsTruthyPredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    OrPredicate,
    Predicate,
)
from predicate.regex_predicate import RegexPredicate
from predicate.standard_predicates import AllPredicate, is_int_p, is_str_p, is_uuid_p


@singledispatch
def generate[T](predicate: Predicate[T]) -> Iterator[T]:
    """Generate values that satisfy this predicate."""
    raise ValueError("Please register generator for correct predicate type")


@generate.register
def generate_and(predicate: AndPredicate) -> Iterator:
    yield from (item for item in generate(predicate.left) if predicate.right(item))
    yield from (item for item in generate(predicate.right) if predicate.left(item))


@generate.register
def generate_eq(predicate: EqPredicate) -> Iterator:
    yield predicate.v


@generate.register
def generate_false(_predicate: AlwaysFalsePredicate) -> Iterator:
    raise ValueError("Always false can never generate a true value")


@generate.register
def generate_ge(predicate: GePredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt + timedelta(days=days) for days in range(0, 5))
        case float():
            yield from count(predicate.v, 0.5)
        case int():
            yield from range(predicate.v, predicate.v + 5)
        case str() as v_str:
            yield from (item for item in generate(is_str_p) if item >= v_str)
        case uuid.UUID() as v_uuid:
            yield from (item for item in generate(is_uuid_p) if item >= v_uuid)


@generate.register
def generate_gt(predicate: GtPredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt + timedelta(days=days) for days in range(1, 6))
        case float():
            yield from count(predicate.v + 0.1, 0.5)
        case int():
            yield from range(predicate.v + 1, predicate.v + 6)
        case str() as v_str:
            yield from (item for item in generate(is_str_p) if item > v_str)
        case uuid.UUID() as v_uuid:
            yield from (item for item in generate(is_uuid_p) if item > v_uuid)


@generate.register
def generate_in(predicate: InPredicate) -> Iterator:
    yield from predicate.v


@generate.register
def generate_le(predicate: LePredicate) -> Iterator:
    match predicate.v:
        case int():
            yield from range(predicate.v, predicate.v - 5, -1)


@generate.register
def generate_lt(predicate: LtPredicate) -> Iterator:
    match predicate.v:
        case int():
            yield from range(predicate.v - 1, predicate.v - 6, -1)


@generate.register
def generate_ne(predicate: NePredicate) -> Iterator:
    yield not predicate.v


@generate.register
def generate_none(_predicate: IsNonePredicate) -> Iterator:
    yield None


@generate.register
def generate_not_in(predicate: NotInPredicate) -> Iterator:
    for item in predicate.v:
        match item:
            case int():
                yield from (item for item in generate(is_int_p) if predicate(item))
            case str():
                yield from (item for item in generate(is_str_p) if predicate(item))


@generate.register
def generate_not_none(_predicate: IsNotNonePredicate) -> Iterator:
    yield from ("foo", 3.14, 42)


@generate.register
def generate_or(predicate: OrPredicate) -> Iterator:
    yield from interleave(generate(predicate.left), generate(predicate.right))


@generate.register
def generate_regex(predicate: RegexPredicate) -> Iterator:
    yield from exrex.generate(predicate.pattern)


@generate.register
def generate_true(_predicate: AlwaysTruePredicate) -> Iterator:
    yield True


@generate.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from (False, 0, (), "", {})


@generate.register
def generate_truthy(_predicate: IsTruthyPredicate) -> Iterator:
    yield from (True, 1, "true", {1}, 3.14)


@generate.register
def generate_is_instance_p(predicate: IsInstancePredicate) -> Iterator:
    klass = predicate.klass[0]  # type: ignore
    if klass is str:
        yield from ("", "0", "foobar", "\n")
    elif klass is bool:
        yield from (False, True)
    elif klass is complex:
        yield from (complex(1, 1),)
    elif klass == datetime:
        yield from (datetime.now(),)
    elif klass is float:
        yield from (math.pi, math.e)
    elif klass == uuid.UUID:
        yield from repeatfunc(uuid.uuid4, times=10)
    elif klass is int:
        yield from generate_random_ints()
    elif klass is set:
        yield from (set(), {1, 2, 3}, {"foo", "bar"})


@generate.register
def generate_all_p(all_predicate: AllPredicate) -> Iterator:
    yield []

    predicate = all_predicate.predicate
    values = take(10, generate(predicate))

    yield random_combination_with_replacement(values, 5)

    yield set(random_combination_with_replacement(values, 5))


@generate.register
def generate_any_p(any_predicate: AnyPredicate) -> Iterator:
    predicate = any_predicate.predicate
    values = take(10, generate(predicate))

    # TODO: also add some values for which predicate isn't valid

    yield random_combination_with_replacement(values, 5)

    yield set(random_combination_with_replacement(values, 5))


def generate_random_strings() -> Iterator:
    population = string.ascii_letters + string.digits
    while True:
        length = random.randint(0, 100)
        yield "".join(choices(population, k=length))


def generate_random_ints() -> Iterator:
    # TODO: maybe first generate some smaller ints
    while True:
        yield random.randint(-sys.maxsize, sys.maxsize)


def generate_ints(predicate: Predicate) -> Iterator:
    yield from (item for item in generate_random_ints() if predicate(item))
