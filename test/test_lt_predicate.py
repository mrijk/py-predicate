from predicate import lt_p
from predicate.explain import explain


def test_lt_p():
    lt_2 = lt_p(2)

    assert not lt_2(2)
    assert lt_2(1)


def test_lt_explain():
    predicate = lt_p(2)

    expected = {"reason": "2 is not less than 2", "result": False}
    assert explain(predicate, 2) == expected
