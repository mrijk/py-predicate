import pytest

from predicate import exercise, explain, is_falsy_p


@pytest.mark.parametrize("value", [False, None, 0, {}, "", (), []])
def test_is_falsy_p(value):
    assert is_falsy_p(value)


def test_is_falsy_p_explain():
    expected = {"reason": "13 is not a falsy value", "result": False}

    assert explain(is_falsy_p, 13) == expected


def test_is_falsy_exercise():
    assert list(exercise(is_falsy_p))
