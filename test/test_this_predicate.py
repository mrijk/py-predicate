from predicate import is_int_p, is_list_of_p, is_str_p, this_p


def test_this_predicate():
    str_or_list_of_str = is_str_p | is_list_of_p(this_p)

    assert not str_or_list_of_str(13)
    assert not str_or_list_of_str([1])

    assert str_or_list_of_str("foo")
    assert str_or_list_of_str([])
    assert str_or_list_of_str(["foo"])
    assert str_or_list_of_str(["foo", ["foo", ["foo"], "bar"]])


def test_this_predicate_with_or():
    predicate = is_str_p | is_list_of_p(this_p | is_int_p)

    assert not predicate(13)

    assert predicate([13])
    assert predicate("foo")
    assert predicate([])
    assert predicate(["foo"])
    assert predicate(["foo", 13, ["foo", ["foo"]]])


def test_this_predicate_with_different_root():
    str_or_list_of_str = is_str_p | is_list_of_p(this_p)

    predicate = str_or_list_of_str | is_int_p

    assert predicate(13)
    assert predicate("foo")
    assert predicate([])
    assert predicate(["foo"])
    assert predicate(["foo", ["foo", ["foo"], "bar"]])
