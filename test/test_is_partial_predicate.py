from functools import partial

from predicate import explain
from predicate.is_partial_predicate import is_partial_p, is_partial_with_signature_p


def test_is_partial():
    def func(x: int, y: int = 0) -> int:
        return x + y

    predicate = is_partial_p

    assert not predicate(func)
    assert not predicate(lambda x: x)
    assert predicate(partial(func, 1))
    assert predicate(partial(func, y=2))


def test_is_partial_with_len():
    def func(x: int, y: int) -> int:
        return x + y

    predicate = is_partial_with_signature_p(nr_of_parameters=1)

    assert not predicate(partial(func))  # two free params
    assert predicate(partial(func, 1))  # one free param
    assert not predicate(func)


def test_is_partial_explain():
    def foobar(x: int) -> bool:
        return True

    predicate = is_partial_p

    expected = {"reason": "Function foobar is not a partial", "result": False}
    assert explain(predicate, foobar) == expected


def test_is_partial_not_a_function_explain():
    predicate = is_partial_p

    expected = {"reason": "Value 13 is not a partial", "result": False}
    assert explain(predicate, 13) == expected


def test_is_partial_with_signature_fail_explain():
    def func(x: int, y: int) -> int:
        return x + y

    predicate = is_partial_with_signature_p(nr_of_parameters=1)

    expected = {"reason": "Partial has 2 parameters, expected: 1", "result": False}
    assert explain(predicate, partial(func)) == expected
