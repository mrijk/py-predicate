from predicate import explain
from predicate.is_lambda_predicate import is_lambda_p, is_lambda_with_signature_p


def test_is_lambda():
    def func(x: int) -> bool:
        return True

    predicate = is_lambda_p

    assert not predicate(func)
    assert predicate(lambda x: x)
    assert predicate(lambda: True)


def test_is_lambda_with_len():
    predicate = is_lambda_with_signature_p(nr_of_parameters=1)

    assert not predicate(lambda: True)
    assert not predicate(lambda _x, _y: True)
    assert not predicate(lambda x, *args: x)
    assert predicate(lambda x: x)


def test_is_lambda_explain():
    def foobar(x: int) -> bool:
        return True

    predicate = is_lambda_p

    expected = {"reason": "Function foobar is not a lambda", "result": False}
    assert explain(predicate, foobar) == expected


def test_is_lambda_not_a_function_or_lambda_explain():
    predicate = is_lambda_p

    expected = {"reason": "Value 13 is not a lambda", "result": False}
    assert explain(predicate, 13) == expected


def test_is_lambda_with_signature_fail_explain():
    predicate = is_lambda_with_signature_p(nr_of_parameters=1)

    expected = {"reason": "Lambda has 0 parameters, expected: 1", "result": False}
    assert explain(predicate, lambda: True) == expected
