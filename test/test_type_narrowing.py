"""Tests to verify TypeGuard / type narrowing support (issue #157).

The reveal_type() calls are for mypy only (run: mypy test/test_type_narrowing.py).
"""

from predicate import is_int_p, is_list_of_p, is_none_p, is_not_none_p, is_str_p


def test_is_int_p_narrows() -> None:
    assert is_int_p(42)
    assert not is_int_p("hello")
    assert not is_int_p(True)  # bool is not int in py-predicate


def test_is_str_p_narrows() -> None:
    assert is_str_p("hello")
    assert not is_str_p(42)


def test_is_none_p_narrows() -> None:
    assert is_none_p(None)
    assert not is_none_p(42)


def test_is_not_none_p_narrows() -> None:
    assert is_not_none_p(42)
    assert not is_not_none_p(None)


def test_is_list_of_p_narrows() -> None:
    assert is_list_of_p(is_int_p)([1, 2, 3])
    assert not is_list_of_p(is_int_p)(["a", "b"])
    assert not is_list_of_p(is_int_p)("not a list")
