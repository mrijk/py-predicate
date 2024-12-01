import random
import string
import sys
from datetime import datetime
from random import choices
from typing import Iterator
from uuid import UUID, uuid4

from more_itertools import interleave, take

from predicate.predicate import Predicate


def random_complex_numbers() -> Iterator:
    yield complex(1, 1)


def random_dicts() -> Iterator:
    yield {}
    while True:
        keys = take(5, random_strings())
        values = take(5, random_anys())
        yield dict(zip(keys, values, strict=False))


def random_datetimes(lower: datetime | None = None, upper: datetime | None = None) -> Iterator:
    # TODO
    yield datetime.now()


def random_strings() -> Iterator:
    population = string.ascii_letters + string.digits
    while True:
        length = random.randint(0, 100)
        yield "".join(choices(population, k=length))


def random_floats(lower: float = -1e-6, upper: float = 1e6) -> Iterator:
    yield lower
    yield upper
    # TODO: maybe first generate_true some smaller float
    while True:
        yield random.uniform(lower, upper)


def random_ints(lower: int = -sys.maxsize, upper: int = sys.maxsize) -> Iterator[int]:
    # yield lower
    # yield upper
    # TODO: maybe first generate_true some smaller ints

    def between(limit: int) -> Iterator[int]:
        low = max(-limit, lower)
        high = min(limit, upper)
        if high >= low:
            yield from (random.randint(low, high) for _ in range(0, limit))

    while True:
        yield from between(1)
        yield from between(10)
        yield from between(100)


def random_uuids() -> Iterator[UUID]:
    while True:
        yield uuid4()


def random_anys() -> Iterator:
    yield from interleave(random_ints(), random_strings(), random_floats())


def generate_strings(predicate: Predicate[str]) -> Iterator[str]:
    yield from (item for item in random_strings() if predicate(item))


def generate_ints(predicate: Predicate[int]) -> Iterator[int]:
    yield from (item for item in random_ints() if predicate(item))


def generate_uuids(predicate: Predicate[UUID]) -> Iterator[UUID]:
    yield from (item for item in random_uuids() if predicate(item))


def generate_anys(predicate: Predicate) -> Iterator:
    yield from (item for item in random_anys() if predicate(item))
