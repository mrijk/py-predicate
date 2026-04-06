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


def test_implies_ge_ne():
    # x >= 3 implies x != 2 (since 2 < 3)
    assert implies(ge_p(3), ne_p(2))
    # x >= 3 does not imply x != 3 (since x could equal 3)
    assert not implies(ge_p(3), ne_p(3))
    # x >= 3 does not imply x != 4 (since x could equal 4)
    assert not implies(ge_p(3), ne_p(4))


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

    # proper superset of {1,2,3} is also a superset of {1,2}
    assert implies(p, is_superset_p({1, 2}))
    assert implies(p, is_superset_p({1, 2, 3}))
    # proper superset of {1,2,3} does not imply superset of {1,2,3,4}
    assert not implies(p, is_superset_p({1, 2, 3, 4}))


def test_implies_is_real_super_false():
    p = is_real_superset_p({1, 2, 3})

    assert not implies(p, always_true_p)


def test_implies_in_in():
    p = in_p({1, 2, 3})

    assert not implies(p, in_p({1, 2}))
    assert implies(p, in_p({1, 2, 3, 4}))


def test_implies_le_ne():
    # x <= 5 implies x != 6 (since 6 > 5)
    assert implies(le_p(5), ne_p(6))
    # x <= 5 does not imply x != 5 (since x could equal 5)
    assert not implies(le_p(5), ne_p(5))
    # x <= 5 does not imply x != 4 (since x could equal 4)
    assert not implies(le_p(5), ne_p(4))


def test_implies_and_recursive():
    # ge_p(5) & le_p(7) implies ge_p(3) because ge_p(5) implies ge_p(3)
    assert implies(ge_p(5) & le_p(7), ge_p(3))
    # ge_p(5) & le_p(7) implies le_p(9) because le_p(7) implies le_p(9)
    assert implies(ge_p(5) & le_p(7), le_p(9))
    # ge_p(5) & le_p(7) does not imply eq_p(6)
    assert not implies(ge_p(5) & le_p(7), eq_p(6))


def test_implies_is_real_subset_superset():
    # proper subset of {1,2} is also a subset of {1,2,3}
    assert implies(is_real_subset_p({1, 2}), is_subset_p({1, 2, 3}))
    # proper subset of {1,2,3} does not imply subset of {1,2}
    assert not implies(is_real_subset_p({1, 2, 3}), is_subset_p({1, 2}))
