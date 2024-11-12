from predicate import always_false_p, always_true_p, eq_p, ge_p, gt_p, in_p, ne_p
from predicate.implies import implies


def test_implies_false():
    p = always_false_p

    assert implies(p, ge_p(2))


def test_implies_true():
    p = always_true_p

    assert not implies(p, ge_p(2))
    assert implies(p, always_true_p)


def test_implies_ge_ge():
    p = ge_p(2)
    q = ge_p(3)

    assert not implies(p, q)
    assert implies(q, p)


def test_implies_ge_gt():
    p = ge_p(3)
    q = gt_p(2)

    assert not implies(q, p)
    assert implies(p, q)


def test_implies_ge_other():
    p = ge_p(3)

    assert not implies(p, ne_p(2))


def test_implies_ge_eq():
    p = eq_p(3)

    assert not implies(p, ge_p(4))
    assert implies(p, ge_p(2))
    assert implies(p, ge_p(3))


def test_implies_eq_eq():
    p = eq_p(3)

    assert not implies(p, eq_p(4))
    assert implies(p, eq_p(3))


def test_implies_eq_gt():
    p = eq_p(3)

    assert not implies(p, gt_p(3))
    assert implies(p, gt_p(2))


def test_implies_eq_in():
    p = eq_p(3)

    assert not implies(p, in_p(2))
    assert implies(p, in_p(3))


def test_implies_eq_other():
    p = eq_p(3)

    assert not implies(p, ne_p(2))