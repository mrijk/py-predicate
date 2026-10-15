import pytest

from predicate import explain, is_frozenset_of_p, is_str_p


@pytest.mark.parametrize(
    "value",
    [
        frozenset(),
        frozenset({"foo"}),
    ],
)
def test_is_frozenset_of_p_true(value):
    is_frozenset_of_str = is_frozenset_of_p(is_str_p)
    assert is_frozenset_of_str(value)


@pytest.mark.parametrize(
    "value",
    [
        "one",
        {"one", "two"},
        frozenset({"one", "two", 3}),
        ["one", "two"],
    ],
)
def test_is_frozenset_of_p_false(value):
    is_frozenset_of_str = is_frozenset_of_p(is_str_p)
    assert not is_frozenset_of_str(value)


def test_is_frozenset_of_explain():
    predicate = is_frozenset_of_p(is_str_p)

    expected = {"reason": "Item '3' didn't match predicate is_str_p", "result": False}
    assert explain(predicate, frozenset({"one", "two", 3})) == expected


def test_is_frozenset_of_explain_not_a_frozenset():
    predicate = is_frozenset_of_p(is_str_p)

    expected = {"reason": "[3] is not an instance of a frozenset", "result": False}
    assert explain(predicate, [3]) == expected
