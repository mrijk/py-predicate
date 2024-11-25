import sys
import uuid
from collections.abc import Iterator
from datetime import datetime, timedelta
from functools import singledispatch

from predicate.generator.helpers import (
    generate_anys,
    generate_strings,
    generate_uuids,
    random_floats,
    random_ints,
)
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.predicate import EqPredicate, GePredicate, NotPredicate, OrPredicate, Predicate


@singledispatch
def generate_false[T](predicate: Predicate[T]) -> Iterator[T]:
    """Generate values that don't satisfy this predicate."""
    raise ValueError("Please register generator for correct predicate type")


@generate_false.register
def generate_eq(predicate: EqPredicate) -> Iterator:
    yield from generate_anys(NotPredicate(predicate=predicate))


@generate_false.register
def generate_ge(predicate: GePredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt - timedelta(days=days) for days in range(1, 6))
        case float():
            yield from random_floats(upper=predicate.v - sys.float_info.epsilon)
        case int():
            yield from random_ints(upper=predicate.v - 1)
        case str():
            yield from generate_strings(NotPredicate(predicate=predicate))
        case uuid.UUID():
            yield from generate_uuids(NotPredicate(predicate=predicate))


@generate_false.register
def generate_is_instance_p(predicate: IsInstancePredicate) -> Iterator:
    klass = predicate.klass[0]  # type: ignore
    not_predicate = NotPredicate(predicate=predicate)
    if klass is str:
        yield from generate_anys(not_predicate)
    elif klass is bool:
        yield from generate_anys(not_predicate)
    elif klass is complex:
        yield from (complex(1, 1),)
    elif klass == datetime:
        yield from (datetime.now(),)
    elif klass is dict:
        yield from ({},)
    elif klass is float:
        yield from generate_anys(not_predicate)
    elif klass == uuid.UUID:
        yield from generate_anys(not_predicate)
    elif klass is int:
        yield from generate_anys(not_predicate)
    elif klass is set:
        yield from (set(), {1, 2, 3}, {"foo", "bar"})


@generate_false.register
def generate_or(predicate: OrPredicate) -> Iterator:
    yield from (item for item in generate_false(predicate.left) if not predicate.right(item))
    yield from (item for item in generate_false(predicate.right) if not predicate.left(item))
