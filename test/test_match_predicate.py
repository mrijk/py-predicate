from predicate import eq_p, is_float_p, is_int_p, is_str_p
from predicate.match_predicate import exactly_n, match_p, optional, plus, repeat, star, wildcard


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


def test_match_optional():
    maybe_int = optional(is_int_p)
    predicate = match_p(maybe_int, is_str_p)

    assert not predicate([1, 2])
    assert predicate(["foo"])
    assert predicate([1, "foo"])


def test_match_exactly_and_optional():
    maybe_int = optional(is_int_p)
    three_ints = exactly_n(3, is_int_p)

    predicate = match_p(maybe_int, three_ints, maybe_int)

    assert predicate([1, 2, 3])


def test_match_repeat():
    one_to_three = repeat(1, 3, is_int_p)

    predicate = match_p(one_to_three)

    assert not predicate([])
    assert predicate([1])
    assert predicate([1, 2])
    assert predicate([1, 2, 3])


def test_match_repeat_and_exactly():
    one_to_three = repeat(1, 3, is_int_p)

    predicate = match_p(one_to_three, is_int_p)

    assert not predicate([])
    assert not predicate([1])
    assert predicate([1, 2])


def test_repeat_and_exactly_and_repeat():
    one_to_three_ints = repeat(1, 3, is_int_p)
    two_to_three_strings = repeat(2, 3, is_str_p)

    predicate = match_p(one_to_three_ints, is_float_p, two_to_three_strings)

    assert not predicate([1, 2, 3.0, "foo"])
    assert predicate([1, 2, 3.0, "foo", "bar"])


def test_match_star():
    zero_or_more_ints = star(is_int_p)

    predicate = match_p(zero_or_more_ints)

    assert not predicate(["foo"])
    assert predicate([])
    assert predicate([1, 2])


def test_match_star_and_str():
    zero_or_more_ints = star(is_int_p)

    predicate = match_p(zero_or_more_ints, is_str_p)

    assert predicate(["foo"])
    assert predicate([1, 2, "foo"])


def test_match_any_int():
    predicate = match_p(wildcard, is_int_p, wildcard)

    assert not predicate(["foo", "bar"])
    assert predicate(["foo", "bar", 1, "foo", "bar"])


def test_match_int_followed_by_str():
    predicate = match_p(wildcard, is_int_p, is_str_p, wildcard)

    assert not predicate(["foo", 1])
    assert predicate([3.14, 1, "foo", 3.14])


def test_match_exactly_with_not():
    two_strings = exactly_n(2, is_str_p)

    predicate = match_p(two_strings, optional(~is_str_p))

    assert not predicate(["foo", "bar", "foobar"])
    assert predicate(["foo", "bar"])


def test_match_plus():
    one_or_more_ints = plus(is_int_p)

    predicate = match_p(one_or_more_ints)

    assert not predicate([])
    assert not predicate(["foo"])
    assert predicate([1])
    assert predicate([1, 2])


def test_match_plus_and_str():
    one_or_more_ints = plus(is_int_p)

    predicate = match_p(one_or_more_ints, is_str_p)

    assert not predicate([])
    assert not predicate(["foo"])
    assert not predicate([1])
    assert predicate([1, "foo"])
