# mypy: disable-error-code="empty-body"
from typing import Any

from generator.generate_true.helpers import assert_generated_true
from predicate import is_valid_spec_p


def test_generate_is_valid_spec_no_params():
    def f() -> int: ...

    assert_generated_true(is_valid_spec_p(f))


def test_generate_is_valid_spec_annotated():
    def f(x: int, y: list[str]) -> int: ...

    assert_generated_true(is_valid_spec_p(f))


def test_generate_is_valid_spec_unannotated():
    def f(x, y: int): ...

    assert_generated_true(is_valid_spec_p(f))


def test_generate_is_valid_spec_all_kinds():
    def f[T](a: int, /, b: T, *args: int, c: str = "", **kwargs: Any) -> T: ...

    assert_generated_true(is_valid_spec_p(f))
