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
