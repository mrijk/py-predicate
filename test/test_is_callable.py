from predicate import explain
from predicate.is_callable_p import IsCallablePredicate


def is_callable(params, return_value) -> IsCallablePredicate:
    return IsCallablePredicate(params, return_value)


def test_is_callable():
    def correct(x: int) -> bool:
        return True

    def incorrect_param(x: float) -> bool:
        return True

    def incorrect_return(x: int) -> str:
        return "bar"

    predicate = is_callable([int], bool)

    assert not predicate(incorrect_return)
    assert not predicate(incorrect_param)
    assert predicate(correct)


def test_is_callable_explain_wrong_return_type():
    def incorrect_return(x: int) -> str:
        return "bar"

    predicate = is_callable([int], bool)

    expected = {"reason": "Wrong return type: <class 'str'>", "result": False}
    assert explain(predicate, incorrect_return) == expected


def test_is_callable_explain_not_callable():
    predicate = is_callable([int], bool)

    expected = {"reason": "1 is not a Callable", "result": False}
    assert explain(predicate, 1) == expected
