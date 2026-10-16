from typing import Protocol

from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from predicate import generate_false, implements_protocol_p


class SupportsOpenClose(Protocol):
    name: str

    def open(self, path: str, *, mode: str = "r") -> int: ...

    def close(self) -> None: ...


def test_generate_implements_protocol():
    assert_generated_false(implements_protocol_p(SupportsOpenClose))


def test_generate_implements_protocol_args_match():
    predicate = implements_protocol_p(SupportsOpenClose, args_match=True)

    assert_generated_false(predicate)
    # Classes with all members, but a wrong signature, only fail when args_match is set
    assert any(implements_protocol_p(SupportsOpenClose)(value) for value in take(5, generate_false(predicate)))
