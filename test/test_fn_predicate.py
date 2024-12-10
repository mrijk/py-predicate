from predicate import explain, fn_p, is_not_none_p


def test_fn_p_with_lambda():
    in_123 = fn_p(lambda x: str(x) in ["1", "2", "3"])
    exists_p = is_not_none_p & in_123

    assert not exists_p(None)
    assert not exists_p(4)
    assert exists_p(3)


def test_fn_p_explain():
    predicate = fn_p(lambda x: str(x) in ["1", "2", "3"])

    expected = {"reason": "Function returned False for value 4", "result": False}
    assert explain(predicate, 4) == expected