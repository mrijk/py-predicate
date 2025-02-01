from predicate import eq_p, is_int_p, is_str_p
from predicate.match_predicate import exactly_n, match_p, optional, repeat


def test_match_first():
    predicate = match_p(is_int_p)

    assert not predicate(["foo", "bar"])
    assert predicate([1, "foo", "bar"])


def test_match_first_two():
    predicate = match_p(eq_p(42), is_str_p)

    assert not predicate([1, "foo", "bar"])
    assert not predicate([42, 1, "bar"])
    assert predicate([42, "foo", "bar"])


def test_match_first_n():
    three_ints = exactly_n(3, is_int_p)
    predicate = match_p(three_ints)

    assert not predicate([1, "foo"])
    assert not predicate([1, 2, "foo"])
    assert predicate([1, 2, 3, "foo"])


def test_match_first_n_followed_by_m():
    three_ints = exactly_n(3, is_int_p)
    two_strings = exactly_n(2, is_str_p)
    predicate = match_p(three_ints, two_strings)

    assert not predicate([1, "foo"])
    assert not predicate([1, 2, "foo"])
    assert predicate([1, 2, 3, "foo", "bar"])


def test_optional():
    maybe_int = optional(is_int_p)
    predicate = match_p(maybe_int, is_str_p)

    assert not predicate([1, 2])
    assert predicate(["foo"])
    assert predicate([1, "foo"])


def test_exactly_and_optional():
    maybe_int = optional(is_int_p)
    three_ints = exactly_n(3, is_int_p)

    predicate = match_p(maybe_int, three_ints, maybe_int)

    assert predicate([1, 2, 3])


def test_repeat():
    one_to_three = repeat(1, 3, is_int_p)

    predicate = match_p(one_to_three)

    assert predicate([1])
