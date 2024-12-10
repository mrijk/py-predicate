from predicate import explain, is_set_of_p, is_str_p


def test_is_set_of_p():
    is_set_of_str = is_set_of_p(is_str_p)

    assert not is_set_of_str({"one", "two", 3})
    assert is_set_of_str(set())
    assert is_set_of_str({"foo"})


def test_is_set_of_explain():
    predicate = is_set_of_p(is_str_p)

    expected = {"reason": "Item '3' didn't match predicate is_str_p", "result": False}
    assert explain(predicate, {"one", "two", 3}) == expected
