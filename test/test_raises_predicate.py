import pytest

from predicate import raises_exception_p, raises_p


def test_raises_p_true():
    assert raises_p(lambda: 1 / 0)


def test_raises_p_false():
    assert not raises_p(lambda: 1)


def test_raises_exception_p_correct_type():
    assert raises_exception_p(ValueError)(lambda: int("x"))


def test_raises_exception_p_wrong_type():
    assert not raises_exception_p(ValueError)(lambda: 1 / 0)


def test_raises_exception_p_no_exception():
    assert not raises_exception_p(ValueError)(lambda: 1)


def test_raises_exception_p_subclass():
    assert raises_exception_p(Exception)(lambda: int("x"))


def test_raises_p_repr():
    assert repr(raises_p) == "raises_p"


def test_raises_exception_p_repr():
    predicate = raises_exception_p(ValueError)
    assert repr(predicate) == "raises_exception_p(ValueError)"


@pytest.mark.parametrize(
    "thunk",
    [
        lambda: 1,
        lambda: "foo",
        lambda: None,
    ],
)
def test_raises_p_false_parametrized(thunk):
    assert not raises_p(thunk)


@pytest.mark.parametrize(
    "thunk",
    [
        lambda: 1 / 0,
        lambda: int("x"),
        lambda: [][0],
    ],
)
def test_raises_p_true_parametrized(thunk):
    assert raises_p(thunk)


def test_explain_failure_no_exception():
    result = raises_p.explain_failure(lambda: 1)
    assert result == {"reason": "callable did not raise an exception"}


def test_explain_failure_wrong_exception_type():
    result = raises_exception_p(ValueError).explain_failure(lambda: 1 / 0)
    assert "ZeroDivisionError" in result["reason"]
    assert "ValueError" in result["reason"]


async def _async_no_raise_for_explain():
    return 42


def test_explain_failure_async_no_exception():
    result = raises_p.explain_failure(_async_no_raise_for_explain)
    assert result == {"reason": "callable did not raise an exception"}


async def _async_raises():
    raise ValueError("async error")


async def _async_no_raise():
    return 42


def test_raises_p_async_true():
    assert raises_p(_async_raises)


def test_raises_p_async_false():
    assert not raises_p(_async_no_raise)


def test_raises_exception_p_async_correct_type():
    assert raises_exception_p(ValueError)(_async_raises)


def test_raises_exception_p_async_wrong_type():
    assert not raises_exception_p(TypeError)(_async_raises)
