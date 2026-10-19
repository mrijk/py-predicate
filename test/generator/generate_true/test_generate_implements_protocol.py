from typing import Protocol

from generator.generate_true.helpers import assert_generated_true
from predicate import implements_protocol_p


class SupportsOpenClose(Protocol):
    name: str

    def open(self, path: str, *, mode: str = "r") -> int: ...

    def close(self) -> None: ...


def test_generate_implements_protocol():
    assert_generated_true(implements_protocol_p(SupportsOpenClose))


def test_generate_implements_protocol_args_match():
    assert_generated_true(implements_protocol_p(SupportsOpenClose, args_match=True))
