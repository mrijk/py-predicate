from predicate import eq_p, explain, ge_p
from predicate.implies_predicate import implies_p


def test_implies_predicate():
    predicate = implies_p(ge_p(2))

    assert not predicate(eq_p(1))
    assert predicate(eq_p(3))


def test_implies_p_explain():
    predicate = implies_p(ge_p(2))

    expected = {"reason": "eq_p(1) doesn't imply ge_p(2)", "result": False}
    assert explain(predicate, eq_p(1)) == expected
