from typing import AsyncIterator, Generator, Iterator

import pytest

from predicate.spec.instrument import instrument
from predicate.spec.spec import SpecViolationError


@instrument
def good_gen(n) -> Iterator[int]:
    yield from range(n)


@instrument
def bad_gen(n) -> Iterator[int]:
    yield "a"


@instrument
def bad_generator(n) -> Generator[int, None, None]:
    yield "a"


@instrument
async def bad_async_gen(n) -> AsyncIterator[int]:
    yield "a"


def test_good_gen():
    assert list(good_gen(3)) == [0, 1, 2]


def test_bad_gen():
    with pytest.raises(SpecViolationError, match="Yield predicate"):
        list(bad_gen(1))


def test_bad_generator():
    with pytest.raises(SpecViolationError, match="Yield predicate"):
        list(bad_generator(1))


async def test_bad_async_gen():
    with pytest.raises(SpecViolationError, match="Yield predicate"):
        [x async for x in bad_async_gen(1)]
