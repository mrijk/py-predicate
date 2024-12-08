from predicate import ge_le_p, ge_lt_p, gt_le_p, gt_lt_p
from predicate.explain import explain


def test_ge_le_p():
    ge_2_le_3 = ge_le_p(2, 3)

    assert not ge_2_le_3(1)
    assert not ge_2_le_3(4)
    assert ge_2_le_3(2)
    assert ge_2_le_3(3)


def test_ge_le_explain():
    predicate = ge_le_p(2, 3)

    expected = {"reason": "1 is not greater equal 2 and less equal 3", "result": False}
    assert explain(predicate, 1) == expected


def test_ge_lt_p():
    ge_2_lt_3 = ge_lt_p(2, 3)

    assert not ge_2_lt_3(1)
    assert not ge_2_lt_3(3)
    assert ge_2_lt_3(2)


def test_ge_lt_explain():
    predicate = ge_lt_p(2, 3)

    expected = {"reason": "1 is not greater equal 2 and less than 3", "result": False}
    assert explain(predicate, 1) == expected


def test_gt_le_p():
    gt_2_le_3 = gt_le_p(2, 3)

    assert not gt_2_le_3(2)
    assert not gt_2_le_3(4)
    assert gt_2_le_3(3)


def test_gt_le_explain():
    predicate = gt_le_p(2, 3)

    expected = {"reason": "1 is not greater than 2 and less than or equal to 3", "result": False}
    assert explain(predicate, 1) == expected


def test_gt_lt_p():
    gt_2_lt_3 = gt_lt_p(2, 4)

    assert not gt_2_lt_3(2)
    assert not gt_2_lt_3(4)
    assert gt_2_lt_3(3)


def test_gt_lt_explain():
    predicate = gt_lt_p(2, 4)

    expected = {"reason": "2 is not greater than 2 and less than 4", "result": False}
    assert explain(predicate, 2) == expected
