from predicate.str_predicates import (
    is_alnum_p,
    is_alpha_p,
    is_decimal_p,
    is_digit_p,
    is_lower_p,
    is_title_p,
    is_upper_p,
)


def test_is_alnum_p():
    assert not is_alnum_p("foo-1")
    assert is_alnum_p("foo1")
    assert is_alnum_p("foo")


def test_is_alpha_p():
    assert not is_alpha_p("foo1")
    assert is_alpha_p("foo")


def test_is_decimal_p():
    assert not is_decimal_p("foo")
    assert is_decimal_p("123")


def test_is_digit_p():
    assert not is_digit_p("Foo")
    assert is_digit_p("123")


def test_is_lower_p():
    assert not is_lower_p("Foo")
    assert is_lower_p("foo")


def test_is_title_p():
    assert not is_title_p("foo")
    assert not is_title_p("FOO")
    assert is_title_p("Foo")


def test_is_upper_p():
    assert not is_upper_p("Foo")
    assert is_upper_p("FOO")
