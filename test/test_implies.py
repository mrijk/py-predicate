from predicate import always_false_p, always_true_p, eq_p, ge_p, gt_p, in_p, le_p, lt_p, ne_p, not_in_p
from predicate.implies import implies
from predicate.set_predicates import is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p


def test_implies_false():
    p = always_false_p

    assert implies(p, ge_p(2))


def test_implies_true():
    p = always_true_p

    assert not implies(p, ge_p(2))
    assert implies(p, always_true_p)


def test_implies_and(p, q):
    assert implies(p & q, p)
    assert implies(p & q, q)


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


def test_implies_le_eq():
    p = eq_p(3)

    assert not implies(p, le_p(2))
    assert implies(p, le_p(3))


def test_implies_eq_eq():
    p = eq_p(3)

    assert not implies(p, eq_p(4))
    assert implies(p, eq_p(3))


def test_implies_eq_gt():
    p = eq_p(3)

    assert not implies(p, gt_p(3))
    assert implies(p, gt_p(2))


def test_implies_eq_lt():
    p = eq_p(3)

    assert not implies(p, lt_p(3))
    assert implies(p, lt_p(4))


def test_implies_eq_in():
    p = eq_p(3)

    assert not implies(p, in_p({2}))
    assert implies(p, in_p({3}))


def test_implies_eq_not_in():
    p = eq_p(3)

    assert not implies(p, not_in_p({3}))
    assert implies(p, not_in_p({2}))


def test_implies_eq_ne():
    p = eq_p(3)

    assert implies(p, ne_p(2))


def test_implies_eq_false():
    p = eq_p(3)

    assert not implies(p, always_true_p)


def test_implies_is_real_subset_subset():
    p = is_real_subset_p({1, 2, 3})

    assert not implies(p, is_subset_p({1, 2}))
    assert implies(p, is_subset_p({1, 2, 3}))


def test_implies_is_real_subset_false():
    p = is_real_subset_p({1, 2, 3})

    assert not implies(p, always_true_p)


def test_implies_is_real_super_superset():
    p = is_real_superset_p({1, 2, 3})

    assert not implies(p, is_superset_p({1, 2}))
    assert implies(p, is_superset_p({1, 2, 3}))


def test_implies_is_real_super_false():
    p = is_real_superset_p({1, 2, 3})

    assert not implies(p, always_true_p)


def test_implies_in_in():
    p = in_p({1, 2, 3})

    assert not implies(p, in_p({1, 2}))
    assert implies(p, in_p({1, 2, 3, 4}))
