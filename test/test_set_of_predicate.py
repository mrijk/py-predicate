from predicate import is_set_of_p, is_str_p


def test_is_set_of_p():
    is_set_of_str = is_set_of_p(is_str_p)

    assert not is_set_of_str({1, 2, 3})
    assert is_set_of_str(set())
    assert is_set_of_str({"foo"})
