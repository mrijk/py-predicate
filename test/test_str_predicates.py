from predicate.str_predicates import (
    ends_with_p,
    is_alnum_p,
    is_alpha_p,
    is_decimal_p,
    is_digit_p,
    is_lower_p,
    is_space_p,
    is_title_p,
    is_upper_p,
    starts_with_p,
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


def test_is_space_p():
    assert is_space_p(" ")
    assert is_space_p("\t")


def test_is_title_p():
    assert not is_title_p("foo")
    assert not is_title_p("FOO")
    assert is_title_p("Foo")


def test_is_upper_p():
    assert not is_upper_p("Foo")
    assert is_upper_p("FOO")


def test_ends_with_p():
    predicate = ends_with_p("foo")

    assert not predicate("foobar")
    assert predicate("barfoo")


def test_starts_with_p():
    predicate = starts_with_p("foo")

    assert not predicate("bar")
    assert predicate("foobar")
