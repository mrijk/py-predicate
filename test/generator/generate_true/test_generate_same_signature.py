# mypy: disable-error-code="empty-body"
from collections.abc import Sequence
from typing import Any

from generator.generate_true.helpers import assert_generated_true
from predicate import same_signature_p


def test_generate_same_signature_no_params():
    def f() -> None: ...

    assert_generated_true(same_signature_p(f))


def test_generate_same_signature_all_kinds():
    def f(a: int, /, b: list[Any], *args: int, c: str = "", **kwargs: int) -> Sequence[Any]: ...

    assert_generated_true(same_signature_p(f))


def test_generate_same_signature_keyword_only():
    def f(x: int, *, extra0: str) -> int: ...

    assert_generated_true(same_signature_p(f))
