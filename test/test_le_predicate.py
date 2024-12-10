from predicate import le_p
from predicate.explain import explain


def test_le_p():
    le_2 = le_p(2)

    assert not le_2(3)
    assert le_2(1)
    assert le_2(2)


def test_le_explain():
    predicate = le_p(2)

    expected = {"reason": "3 is not less than or equal to 2", "result": False}
    assert explain(predicate, 3) == expected
