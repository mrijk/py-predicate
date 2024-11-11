from predicate import eq_p, ge_p, gt_p, is_none_p, is_not_none_p, le_p, lt_p, ne_p
from predicate.negate import negate


def test_negate_eq():
    eq_2 = eq_p(2)

    negated = negate(eq_2)

    assert negated == ne_p(2)


def test_negate_ne():
    ne_2 = ne_p(2)

    negated = negate(ne_2)

    assert negated == eq_p(2)


def test_negate_lt():
    lt_2 = lt_p(2)

    negated = negate(lt_2)

    assert negated == ge_p(2)


def test_negate_le():
    le_2 = le_p(2)

    negated = negate(le_2)

    assert negated == gt_p(2)


def test_negate_gt():
    gt_2 = gt_p(2)

    negated = negate(gt_2)

    assert negated == le_p(2)


def test_negate_ge():
    ge_2 = ge_p(2)

    negated = negate(ge_2)

    assert negated == lt_p(2)


def test_negate_is_none_p():
    negated = negate(is_none_p)

    assert negated == is_not_none_p


def test_negate_is_not_none_p():
    negated = negate(is_not_none_p)

    assert negated == is_none_p
