from helpers import is_and_p

from predicate import ge_p, gt_p, le_p, lt_p


def test_and():
    ge_2 = ge_p(2)
    le_3 = le_p(3)

    between_2_and_3 = ge_2 & le_3

    assert is_and_p(between_2_and_3)

    assert between_2_and_3(2) is True
    assert between_2_and_3(3) is True
    assert between_2_and_3(0) is False
    assert between_2_and_3(4) is False


def test_and_commutative():
    #  p & q == q & p
    gt_2 = gt_p(2)
    lt_4 = lt_p(4)

    p_1 = gt_2 & lt_4
    assert p_1(2) is False
    assert p_1(4) is False
    assert p_1(3) is True

    p_2 = lt_4 & gt_2
    assert p_2(2) is False
    assert p_2(4) is False
    assert p_2(3) is True


def test_and_associative():
    # TODO
    pass
