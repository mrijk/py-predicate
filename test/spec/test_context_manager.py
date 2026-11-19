import contextlib
from collections.abc import Iterator

from more_itertools import take

from predicate import exercise, instrument


@contextlib.contextmanager
def ctx() -> Iterator[int]:
    yield 1


def test_exercise_context_manager():
    assert len(take(1, exercise(ctx))) == 1


def test_instrument_context_manager():
    @instrument
    @contextlib.contextmanager
    def ctx2() -> Iterator[int]:
        yield 1

    with ctx2() as value:
        assert value == 1
