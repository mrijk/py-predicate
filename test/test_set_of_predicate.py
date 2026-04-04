import pytest

from predicate import explain, is_set_of_p, is_str_p


@pytest.mark.parametrize(
    "value",
    [
        set(),
        {"foo"},
    ],
)
def test_is_set_of_p_true(value):
    is_set_of_str = is_set_of_p(is_str_p)
    assert is_set_of_str(value)


@pytest.mark.parametrize(
    "value",
    [
        "one",
        {"one", "two", 3},
        ["one", "two"],
    ],
)
def test_is_set_of_p_false(value):
    is_set_of_str = is_set_of_p(is_str_p)
    assert not is_set_of_str(value)


def test_is_set_of_explain():
    predicate = is_set_of_p(is_str_p)

    expected = {"reason": "Item '3' didn't match predicate is_str_p", "result": False}
    assert explain(predicate, {"one", "two", 3}) == expected


def test_is_list_of_explain_not_a_list():
    predicate = is_set_of_p(is_str_p)

    expected = {"reason": "[3] is not an instance of a set", "result": False}
    assert explain(predicate, [3]) == expected
