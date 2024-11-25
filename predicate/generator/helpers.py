import random
import string
import sys
from random import choices
from typing import Iterator
from uuid import UUID, uuid4

from more_itertools import interleave

from predicate.predicate import Predicate


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
    yield lower
    yield upper
    # TODO: maybe first generate_true some smaller ints
    while True:
        yield random.randint(lower, upper)


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
