from helpers import is_and_p

from predicate import ge_p, gt_p, le_p, lt_p
from predicate.explain import explain


def test_and():
    ge_2 = ge_p(2)
    le_3 = le_p(3)

    between_2_and_3 = ge_2 & le_3

    assert is_and_p(between_2_and_3)

    assert not between_2_and_3(0)
    assert not between_2_and_3(4)
    assert between_2_and_3(2)
    assert between_2_and_3(3)


def test_and_commutative():
    #  p & q == q & p
    gt_2 = gt_p(2)
    lt_4 = lt_p(4)

    p_1 = gt_2 & lt_4
    assert not p_1(2)
    assert not p_1(4)
    assert p_1(3)

    p_2 = lt_4 & gt_2
    assert not p_2(2)
    assert not p_2(4)
    assert p_2(3)


def test_and_eq(p, q):
    # p & q == q & p
    p = gt_p(2)
    q = lt_p(4)

    assert p & q == q & p


def test_and_associative(p, q, r):
    # assert (p & q) & r == p & (q & r)
    pass


def test_and_explain():
    p = gt_p(2)
    q = lt_p(4)

    predicate = p & q

    expected = {"left": {"explanation": {"reason": "2 is not greater than 2", "result": False}, "result": False}}

    assert explain(predicate, 2) == expected
