from predicate import explain, ge_p, is_bool_p, is_dict_of_p, is_int_p, is_str_p, is_tuple_of_p


def test_is_tuple_of_p():
    predicate = is_tuple_of_p(is_str_p, is_int_p & ge_p(2), is_bool_p)

    assert not predicate(("foo",))
    assert not predicate(("foo", 13))
    assert not predicate(("foo", 13, None))
    assert not predicate(("foo", 1, False))

    assert predicate(("foo", 2, False))


def test_is_tuple_of_with_dict_p():
    predicate = is_tuple_of_p(is_int_p, is_dict_of_p(("n", is_int_p), ("s", is_str_p)))

    assert not predicate((13, {"n": 13, "s": 12}))
    assert predicate((13, {"n": 13, "s": "foo"}))


def test_is_tuple_of_explain_incorrect_length():
    predicate = is_tuple_of_p(is_str_p, is_int_p & ge_p(2), is_bool_p)

    expected = {"reason": "Incorrect tuple size, expected: 3, actual: 2", "result": False}
    assert explain(predicate, ("foo", 1)) == expected


def test_is_tuple_of_explain_incorrect_value():
    predicate = is_tuple_of_p(is_str_p, is_int_p & ge_p(2), is_bool_p)

    expected = {"reason": "Predicate is_int_p & ge_p(2) failed for value 1", "result": False}
    assert explain(predicate, ("foo", 1, False)) == expected
