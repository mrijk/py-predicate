from typing import Protocol, runtime_checkable

from predicate import implements_protocol_p


def test_implements_protocol_p_ok():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    predicate = implements_protocol_p(SupportsClose, args_match=True)

    class Foo:
        def close(self) -> None:
            pass

    assert predicate(Foo)


def test_implements_protocol_p_nok():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    predicate = implements_protocol_p(SupportsClose)

    class MissingMethod:
        def closer(self) -> None:
            pass

    assert not predicate(MissingMethod)


def test_implements_protocol_p_with_args_match_nok():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    predicate = implements_protocol_p(SupportsClose, args_match=True)

    class AdditionalArg:
        def close(self, x: int) -> None:
            pass

    class DifferentReturn:
        def close(self) -> int:
            return 13

    assert not predicate(AdditionalArg)
    assert not predicate(DifferentReturn)
