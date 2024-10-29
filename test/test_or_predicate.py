from predicate import (
    ge_p,
    gt_p,
    le_p,
    lt_p,
)
from predicate.standard_predicates import is_none_p, is_not_none_p


def test_or():
    ge_4 = ge_p(4)
    le_2 = le_p(2)

    le_2_or_ge_4 = le_2 | ge_4

    assert le_2_or_ge_4(2) is True
    assert le_2_or_ge_4(4) is True
    assert le_2_or_ge_4(3) is False


def test_or_commutative():
    lt_2 = lt_p(2)
    gt_4 = gt_p(4)

    p_1 = lt_2 | gt_4
    assert p_1(1) is True
    assert p_1(3) is False
    assert p_1(5) is True

    p_2 = gt_4 | lt_2
    assert p_2(1) is True
    assert p_2(3) is False
    assert p_2(5) is True


def test_or_always_true():
    always_true = is_none_p | is_not_none_p
    assert always_true(13) is True
    assert always_true(None) is True
