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


def test_implements_protocol_p_repr():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    assert repr(implements_protocol_p(SupportsClose)) == "implements_protocol_p(SupportsClose)"
    assert repr(implements_protocol_p(SupportsClose, args_match=True)) == (
        "implements_protocol_p(SupportsClose, args_match=True)"
    )


def test_implements_protocol_p_explain():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    class MissingMethod:
        pass

    class AdditionalArg:
        def close(self, x: int) -> None:
            pass

    assert implements_protocol_p(SupportsClose).explain(MissingMethod) == {
        "result": False,
        "reason": f"{MissingMethod} does not implement SupportsClose",
    }
    assert implements_protocol_p(SupportsClose, args_match=True).explain(AdditionalArg) == {
        "result": False,
        "reason": "Method 'close': Expected 1 parameter(s), got 2",
    }


def test_implements_protocol_p_without_args_match_ok():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    class Foo:
        def close(self) -> None:
            pass

    assert implements_protocol_p(SupportsClose)(Foo)


def test_implements_protocol_p_args_match_only_with_flag():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    class Door:
        def close(self, force: bool) -> None:
            pass

    assert implements_protocol_p(SupportsClose)(Door)
    assert not implements_protocol_p(SupportsClose, args_match=True)(Door)


def test_implements_protocol_p_explain_ok():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    class Foo:
        def close(self) -> None:
            pass

    assert implements_protocol_p(SupportsClose, args_match=True).explain(Foo) == {"result": True}


def test_implements_protocol_p_data_members():
    @runtime_checkable
    class Named(Protocol):
        name: str

        def close(self) -> None: ...

    class WithValue:
        name = "foo"

        def close(self) -> None:
            pass

    class WithAnnotation:
        name: str

        def close(self) -> None:
            pass

    class MissingName:
        def close(self) -> None:
            pass

    predicate = implements_protocol_p(Named, args_match=True)

    assert predicate(WithValue)
    assert predicate(WithAnnotation)
    assert not predicate(MissingName)


def test_implements_protocol_p_multiple_methods():
    @runtime_checkable
    class SupportsOpenClose(Protocol):
        def open(self) -> None: ...

        def close(self) -> None: ...

    class WrongClose:
        def open(self) -> None:
            pass

        def close(self, x: int) -> None:
            pass

    assert implements_protocol_p(SupportsOpenClose, args_match=True).explain(WrongClose) == {
        "result": False,
        "reason": "Method 'close': Expected 1 parameter(s), got 2",
    }


def test_implements_protocol_p_compatible_signatures():
    class Base: ...

    class Derived(Base): ...

    @runtime_checkable
    class SupportsCreate(Protocol):
        def create(self, x: Derived) -> Base: ...

    class NarrowerReturn:
        def create(self, x: Derived) -> Derived:
            return x

    class WiderParameter:
        def create(self, x: Base) -> Base:
            return x

    class ExtraOptional:
        def create(self, x: Derived, y: int = 0) -> Base:
            return x

    predicate = implements_protocol_p(SupportsCreate, args_match=True)

    assert predicate(NarrowerReturn)
    assert predicate(WiderParameter)
    assert predicate(ExtraOptional)


def test_implements_protocol_p_init_with_args():
    @runtime_checkable
    class SupportsClose(Protocol):
        def close(self) -> None: ...

    class NeedsArg:
        def __init__(self, a: int) -> None:
            self.a = a

        def close(self) -> None:
            pass

    assert implements_protocol_p(SupportsClose, args_match=True)(NeedsArg)
