from helpers import is_not_p

from predicate import always_false_p, always_true_p, ge_p
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.standard_predicates import all_p, eq_p, gt_p, in_p, is_none_p, is_not_none_p, le_p, lt_p, ne_p, not_in_p


def test_optimize_not_not():
    # ~~p == p
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert is_not_p(ge_2_to)
    assert can_optimize(ge_2_to)

    optimized = optimize(ge_2_to)

    assert optimized == ge_2


def test_not_optimize_always_true():
    # ~False == True
    always_true = ~always_false_p

    assert is_not_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert optimized == always_true_p


def test_not_optimize_always_false():
    # ~True == False
    always_false = ~always_true_p

    assert is_not_p(always_false)
    assert can_optimize(always_false)

    optimized = optimize(always_false)

    assert optimized == always_false_p


def test_not_optimize_ge():
    # ~ge(v) => lt(v)
    ge_2 = ge_p(2)
    predicate = ~ge_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(2)


def test_not_optimize_gt():
    # ~gt(v) => le(v)
    gt_2 = gt_p(2)
    predicate = ~gt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == le_p(2)


def test_not_optimize_le():
    # ~lt(v) => ge(v)
    le_2 = le_p(2)
    predicate = ~le_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_p(2)


def test_not_optimize_lt():
    # ~lt(v) => ge(v)
    lt_2 = lt_p(2)
    predicate = ~lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_p(2)


def test_not_optimize_eq():
    # ~(x == v) => x != v
    eq_2 = eq_p(2)
    predicate = ~eq_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(2)


def test_not_optimize_ne():
    # ~(x != v) => x == v
    ne_2 = ne_p(2)
    predicate = ~ne_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(2)


def test_not_optimize_none():
    predicate = ~is_none_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_not_none_p


def test_not_optimize_not_none():
    predicate = ~is_not_none_p

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_none_p


def test_not_optimize_all():
    predicate = ~all_p(is_none_p)

    assert not can_optimize(predicate)


def test_not_in():
    not_in_234 = not_in_p(2, 3, 4)
    predicate = ~not_in_234

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == in_p(2, 3, 4)


def test_not_not_in():
    in_234 = in_p(2, 3, 4)
    predicate = ~in_234

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == not_in_p(2, 3, 4)
