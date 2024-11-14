from predicate import is_list_of_p, is_str_p, this_p


def test_this_predicate():
    str_or_list_of_str = is_str_p | is_list_of_p(this_p)

    # assert not str_or_list_of_str(1)
    # assert not str_or_list_of_str([1])

    assert str_or_list_of_str("foo")
    assert str_or_list_of_str([])
    assert str_or_list_of_str(["foo"])
    # assert str_or_list_of_str(["foo", ["foo", ["foo"], "bar"]])
