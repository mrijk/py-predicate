import pytest

from predicate import explain, is_truthy_p


@pytest.mark.parametrize("value", [True, not None, 13, {1}, "foo", (1,), [1]])
def test_is_truthy_p(value):
    assert is_truthy_p(value)


@pytest.mark.parametrize("value", [False, None, {}, "", (), []])
def test_is_truthy_p_explain(value):
    expected = {"reason": f"{value} is not a truthy value", "result": False}

    assert explain(is_truthy_p, value) == expected
