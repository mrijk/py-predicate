import math

from predicate import explain, fn_p, is_finite_p, is_inf_p, is_not_none_p


def test_fn_p_with_lambda():
    in_123 = fn_p(lambda x: str(x) in ["1", "2", "3"])
    exists_p = is_not_none_p & in_123

    assert not exists_p(None)
    assert not exists_p(4)
    assert exists_p(3)

    assert repr(in_123) == "fn_p(predicate_fn=<lambda>)"


def test_fn_p_with_fun():
    def func(x: int) -> bool:
        return str(x) in ["1", "2", "3"]

    in_123 = fn_p(func)

    assert in_123(3)

    assert repr(in_123) == "fn_p(predicate_fn=func)"


def test_fn_p_explain():
    predicate = fn_p(lambda x: str(x) in ["1", "2", "3"])

    expected = {"reason": "Function returned False for value 4", "result": False}
    assert explain(predicate, 4) == expected


def test_is_finite_p():
    assert not is_finite_p(math.inf)
    assert is_finite_p(13)
    assert is_finite_p(3.14)


def test_is_inf_p():
    assert not is_inf_p(13)

    assert is_inf_p(-math.inf)
    assert is_inf_p(math.inf)
