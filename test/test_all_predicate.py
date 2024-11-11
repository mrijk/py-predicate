from predicate import all_p, eq_p, fn_p, is_int_p, is_str_p


def test_all():
    all_int = all_p(is_int_p)

    assert all_int([1, 2, 3])
    assert not all_int([None, 2, 3])


def test_all_combined_1():
    all_eq_2_or_3 = all_p((is_int_p & (eq_p(2) | eq_p(3))) | eq_p("3"))

    assert not all_eq_2_or_3([1, 3, 2, 3])
    assert all_eq_2_or_3([2, "3", 2, 3]) is True


def test_all_combined_2():
    str_len_3_p = fn_p(lambda x: len(x) == 3)
    all_len_3_p = all_p(is_str_p & str_len_3_p)

    assert not all_len_3_p(["aaa", 3, "ccc"])
    assert not all_len_3_p(["aaa", "bbbb", "ccc"])
    assert all_len_3_p(["aaa", "bbb", "ccc"])
