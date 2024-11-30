from predicate import ge_p, is_bool_p, is_int_p, is_str_p, is_tuple_of_p


def test_is_tuple_of_p():
    predicate = is_tuple_of_p(is_str_p, is_int_p & ge_p(2), is_bool_p)

    assert not predicate(("foo",))
    assert not predicate(("foo", 13))
    assert not predicate(("foo", 13, None))
    assert not predicate(("foo", 1, False))

    assert predicate(("foo", 2, False))
