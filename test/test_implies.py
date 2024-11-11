from predicate import eq_p, ge_p, in_p
from predicate.implies import implies


def test_implies_ge_ge():
    p = ge_p(2)
    q = ge_p(3)

    assert not implies(p, q)
    assert implies(q, p)


def test_implies_ge_eq():
    p = eq_p(3)

    assert not implies(p, ge_p(4))
    assert implies(p, ge_p(2))
    assert implies(p, ge_p(3))


def test_implies_eq_eq():
    p = eq_p(3)

    assert not implies(p, eq_p(4))
    assert implies(p, eq_p(3))


def test_implies_eq_in():
    p = eq_p(3)

    assert not implies(p, in_p(2))
    assert implies(p, in_p(3))
