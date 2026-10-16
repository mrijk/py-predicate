# mypy: disable-error-code="empty-body"
from generator.generate_false.helpers import assert_generated_false
from predicate import same_signature_p


def test_generate_same_signature_no_params():
    def f() -> None: ...

    assert_generated_false(same_signature_p(f))


def test_generate_same_signature_all_kinds():
    def f(a: int, /, b: list, *args: int, c: str = "", **kwargs: int) -> list: ...

    assert_generated_false(same_signature_p(f))
