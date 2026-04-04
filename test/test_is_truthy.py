import pytest
from helpers import exercise_predicate

from predicate import explain, is_truthy_p


@pytest.mark.parametrize("value", [True, not None, 13, {1}, "foo", (1,), [1]])
@pytest.mark.skip
def test_is_truthy_p(value):
    assert is_truthy_p(value)


@pytest.mark.parametrize("value", [False, None, {}, "", (), []])
@pytest.mark.skip
def test_is_truthy_p_explain(value):
    expected = {"reason": f"{value} is not a truthy value", "result": False}

    assert explain(is_truthy_p, value) == expected


@pytest.mark.skip
def test_is_truthy_exercise():
    exercise_predicate(is_truthy_p)
