import random
import string
import sys
from collections.abc import Callable, Iterable
from datetime import datetime, timedelta
from itertools import cycle
from random import choices
from typing import Any, Iterator
from uuid import UUID, uuid4

from more_itertools import first, interleave, random_permutation, repeatfunc, take

from predicate.generator.generate_predicate import generate_predicate
from predicate.predicate import Predicate
from predicate.standard_predicates import is_hashable_p


def random_first_from_iterables(*iterables: Iterable) -> Iterator:
    non_empty_iterables = [it for it in iterables if it]

    while True:
        chosen_iterable = random.choice(non_empty_iterables)
        try:
            yield next(iter(chosen_iterable))
        except StopIteration:
            pass


def set_from_list(value: list, order: bool = False) -> Iterator:
    length = len(value)
    if length and is_hashable_p(first(value)):
        if len(result := set(value)) == length:
            yield result if order else set(random_permutation(result))


def random_complex_numbers() -> Iterator:
    yield from (complex(real, imaginary) for real, imaginary in zip(random_ints(), random_ints(), strict=False))


def random_callables() -> Iterator:
    while True:
        yield from (lambda x: x,)  # TODO: add more Callable's


def random_dicts() -> Iterator:
    yield {}
    while True:
        keys = take(5, random_strings())
        values = take(5, random_anys())
        yield dict(zip(keys, values, strict=False))


def random_datetimes(lower: datetime | None = None, upper: datetime | None = None) -> Iterator:
    start = lower if lower else datetime(year=1980, month=1, day=1)
    end = upper if upper else datetime(year=2050, month=1, day=1)

    now = datetime.now()

    if start <= now <= end:
        yield now

    while True:
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        yield start + timedelta(seconds=random_second)


def random_predicates(*, max_depth: int = 10, klass: type = int) -> Iterator:
    subclasses = Predicate.__subclasses__()

    iterables = [generate_predicate(subclass, max_depth=max_depth, klass=klass) for subclass in subclasses]  # type: ignore

    yield from random_first_from_iterables(*iterables)


def random_sets(min_size: int = 0, max_size: int = 10, klass=Any) -> Iterator:
    if min_size == 0:
        yield set()
    while True:
        length = random.randint(min_size, max_size)
        values = take(length, random_values_of_type(klass=klass))
        if len(result := set(values)) == length:
            yield result


def random_bools() -> Iterator:
    yield from (False, True)
    yield from repeatfunc(random.choice, None, (False, True))


def random_containers() -> Iterator:
    yield from cycle(([], {}))


def random_strings(min_size: int = 0, max_size: int = 10) -> Iterator:
    population = string.ascii_letters + string.digits
    while True:
        length = random.randint(min_size, max_size)
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

    def between(limit: int) -> Iterator[int]:
        low = max(-limit, lower)
        high = min(limit, upper)
        if high >= low:
            yield from (random.randint(low, high) for _ in range(0, limit))

    while True:
        yield from between(1)
        yield from between(10)
        yield from between(100)


def random_iterables(min_size: int = 0, max_size: int = 10, klass=Any) -> Iterator[Iterable]:
    if max_size == 0:
        yield from ([], {}, (), "")
    else:
        iterable_1 = random_sets(min_size=min_size, max_size=max_size, klass=klass)
        iterable_2 = random_lists(min_size=min_size, max_size=max_size, klass=klass)
        iterable_3 = random_tuples(min_size=min_size, max_size=max_size, klass=klass)
        yield from random_first_from_iterables(iterable_1, iterable_2, iterable_3)


def random_lists(min_size: int = 0, max_size: int = 10, klass=Any) -> Iterator[Iterable]:
    if min_size == 0:
        yield []
    while True:
        length = random.randint(min_size, max_size)
        yield take(length, random_values_of_type(klass=klass))


def random_tuples(min_size: int = 0, max_size: int = 10, klass=Any) -> Iterator[Iterable]:
    if min_size == 0:
        yield ()
    while True:
        length = random.randint(min_size, max_size)
        yield tuple(take(length, random_values_of_type(klass=klass)))


def random_uuids() -> Iterator[UUID]:
    yield from repeatfunc(uuid4)


def random_anys() -> Iterator:
    yield from interleave(random_bools(), random_ints(), random_strings(), random_floats(), random_datetimes())


def random_values_of_type(klass: type) -> Iterator:
    type_registry: dict[type, Callable[[], Iterator]] = {
        bool: random_bools,
        datetime: random_datetimes,
        int: random_ints,
        float: random_floats,
        str: random_strings,
    }

    if generator := type_registry.get(klass):
        yield from generator()
    elif klass == Any:
        yield from random_anys()
    else:
        raise ValueError(f"No generator found for {klass}")


def random_constrained_values_of_type(klass: type) -> Iterator:
    type_registry: dict[type, Callable[[], Iterator]] = {
        int: random_ints,
        float: random_floats,
        str: random_strings,
    }

    if generator := type_registry.get(klass):
        yield from generator()
    else:
        yield from []
        # raise ValueError(f"No generator found for {klass}")


def random_constrained_pairs_of_type(klass: type) -> Iterator[tuple]:
    def ordered_tuple(x: Any, y: Any) -> tuple:
        return (x, y) if x <= y else (y, x)

    values_1 = random_constrained_values_of_type(klass)
    values_2 = random_constrained_values_of_type(klass)
    values = zip(values_1, values_2, strict=False)

    yield from (ordered_tuple(x, y) for x, y in values)


def generate_strings(predicate: Predicate[str]) -> Iterator[str]:
    yield from (item for item in random_strings() if predicate(item))


def generate_ints(predicate: Predicate[int]) -> Iterator[int]:
    yield from (item for item in random_ints() if predicate(item))


def generate_uuids(predicate: Predicate[UUID]) -> Iterator[UUID]:
    yield from (item for item in random_uuids() if predicate(item))


def generate_anys(predicate: Predicate) -> Iterator:
    yield from (item for item in random_anys() if predicate(item))
