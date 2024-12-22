from predicate import ge_p, gt_p, is_none_p, is_not_none_p, le_p, lt_p
from predicate.explain import explain


def test_or():
    ge_4 = ge_p(4)
    le_2 = le_p(2)

    le_2_or_ge_4 = le_2 | ge_4

    assert not le_2_or_ge_4(3)
    assert le_2_or_ge_4(2)
    assert le_2_or_ge_4(4)


def test_or_commutative():
    lt_2 = lt_p(2)
    gt_4 = gt_p(4)

    p_1 = lt_2 | gt_4

    assert not p_1(3)
    assert p_1(1)
    assert p_1(5)

    p_2 = gt_4 | lt_2

    assert not p_2(3)
    assert p_2(1)
    assert p_2(5)


def test_or_eq():
    # p | q == q | p
    p = gt_p(2)
    q = lt_p(4)

    assert p | q == q | p


def test_or_always_true():
    always_true = is_none_p | is_not_none_p

    assert always_true(13)
    assert always_true(None)


def test_or_contains(p, q, r):
    predicate = p | q

    assert r not in predicate
    assert p in predicate
    assert q in predicate


def test_or_explain():
    p = gt_p(4)
    q = lt_p(3)

    predicate = p | q

    expected = {
        "left": {"reason": "3 is not greater than 4", "result": False},
        "result": False,
        "right": {"reason": "3 is not less than 3", "result": False},
    }

    assert explain(predicate, 3) == expected
