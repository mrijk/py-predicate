from predicate import explain, is_list_of_p, is_str_p
from predicate.list_of_predicate import is_single_or_list_of_p


def test_is_list_of_p():
    is_list_of_str = is_list_of_p(is_str_p)

    assert not is_list_of_str(["one", "two", 3])
    assert is_list_of_str([])
    assert is_list_of_str(["foo"])


def test_is_single_or_list_of_p():
    is_single_or_list_of_str = is_single_or_list_of_p(is_str_p)

    assert not is_single_or_list_of_str(None)
    assert not is_single_or_list_of_str([1])

    assert is_single_or_list_of_str("foo")
    assert is_single_or_list_of_str([])
    assert is_single_or_list_of_str(["foo"])


def test_is_list_of_explain():
    predicate = is_list_of_p(is_str_p)

    expected = {"reason": "Item '3' didn't match predicate is_str_p", "result": False}
    assert explain(predicate, ["one", "two", 3]) == expected


def test_is_list_of_explain_not_a_list():
    predicate = is_list_of_p(is_str_p)

    expected = {"reason": "3 is not an instance of a list", "result": False}
    assert explain(predicate, 3) == expected
