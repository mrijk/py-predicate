from typing import Protocol

from predicate import is_protocol_p


def test_is_protocol_p_ok():
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    predicate = is_protocol_p()

    assert predicate(Protocol)
    assert predicate(SupportsClose)


def test_is_protocol_p_not_ok():
    class SupportsClose:
        def close(self) -> None: ...

    predicate = is_protocol_p()
    assert not predicate(int)
    assert not predicate(SupportsClose)
