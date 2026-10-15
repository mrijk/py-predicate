# mypy: disable-error-code="empty-body"
from collections.abc import Sequence
from typing import Any

from predicate import explain, same_signature_p


def test_same_signature_p_ok():
    def f() -> int | str: ...

    def ok_1() -> int: ...

    def ok_2() -> str: ...

    def ok_3() -> str | int: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)
    assert predicate(ok_2)
    assert predicate(ok_3)


def test_same_signature_p_idempotent():
    def f() -> int | str: ...

    predicate = same_signature_p(f)

    assert predicate(f)


def test_same_signature_p_abc():
    def f(x: list) -> Sequence: ...

    def ok_1(x: Sequence) -> list: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_return_type_nok():
    def f() -> None: ...

    def fail_1() -> int: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Return type <class 'int'> is not a subtype of None", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_args_len_nok():
    def f() -> None: ...

    def fail_1(x: int) -> None: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Expected 0 parameter(s), got 1", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_args_name_nok():
    def f(x: int) -> None: ...

    def fail_1(y: int) -> None: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Expected parameter 'x', got 'y'", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_args_type_ok():
    def f(x: int) -> int | float: ...

    def ok_1(x: int | float) -> int: ...
    def ok_2(x: int | None) -> int: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)
    assert predicate(ok_2)


def test_same_signature_p_with_additional_default_args():
    def f(x: int) -> int | float: ...

    def ok_1(x: int | float, z: int | None = None) -> int: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_args_type_nok():
    def f(x: float) -> None: ...

    def fail_1(x: str) -> None: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Parameter 'x' has type <class 'str'>, expected <class 'float'>", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_with_additional_named_args():
    def f(x: int, *, y: int, z: int) -> int | float: ...

    def ok_1(x: int, *, z: int, y: int) -> int: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_with_additional_named_args_nok():
    def f(x: int, *, y: int, z: int) -> int | float: ...

    def fail_1(x: int, *, z: int, y: str) -> int: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Parameter 'y' has type <class 'str'>, expected <class 'int'>", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_repr():
    def f() -> None: ...

    assert repr(same_signature_p(f)) == "same_signature_p(f)"


def test_same_signature_p_generic():
    def f(x: list[int]) -> list[int]: ...

    predicate = same_signature_p(f)

    assert predicate(f)


def test_same_signature_p_string_annotation():
    def f(x: "int") -> None: ...

    def ok_1(x: int) -> None: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_any():
    def f(x: int) -> Any: ...

    def ok_1(x: Any) -> int: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_unannotated():
    def f(x): ...

    def ok_1(x: int) -> None: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_with_additional_var_args():
    def f(x: int) -> None: ...

    def ok_1(x: int, *args: int) -> None: ...

    def ok_2(x: int, **kwargs: int) -> None: ...

    predicate = same_signature_p(f)

    assert predicate(ok_1)
    assert predicate(ok_2)


def test_same_signature_p_positional_only_nok():
    def f(x: int) -> None: ...

    def fail_1(x: int, /) -> None: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Parameter 'x' is positional-only, expected positional or keyword", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_keyword_only_nok():
    def f(x: int, y: int) -> None: ...

    def fail_1(x: int, *, y: int) -> None: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Parameter 'y' is keyword-only, expected positional or keyword", "result": False}
    assert explain(predicate, fail_1) == expected


def test_same_signature_p_missing_default_nok():
    def f(x: int = 1) -> None: ...

    def fail_1(x: int) -> None: ...

    predicate = same_signature_p(f)

    assert not predicate(fail_1)

    expected = {"reason": "Parameter 'x' has no default value", "result": False}
    assert explain(predicate, fail_1) == expected
