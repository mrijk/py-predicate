from predicate.explain import explain
from predicate.standard_predicates import comp_p, ge_p


def test_comp_predicate():
    ge_2 = ge_p(2)

    predicate = comp_p(fn=lambda x: 2 * x, predicate=ge_2)

    assert not predicate(0)
    assert predicate(1)


def test_comp_explain():
    ge_2 = ge_p(2)

    predicate = comp_p(fn=lambda x: 2 * x, predicate=ge_2)

    expected = {"reason": {"reason": "0 is not greater or equal to 2", "result": False}, "result": False}
    assert explain(predicate, 0) == expected
