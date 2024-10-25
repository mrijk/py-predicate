from helpers import is_not_p, is_false_p, is_true_p
from predicate import always_false_p, ge_p, always_true_p
from predicate.optimizer.predicate_optimizer import optimize, can_optimize
from predicate.standard_predicates import all_p, ne_p, eq_p, any_p, lt_p, gt_p, le_p


def test_not():
    ge_2 = ge_p(2)
    lt_2 = ~ge_2

    assert is_not_p(lt_2)

    assert lt_2(2) is False
    assert lt_2(1) is True


def test_not_not():
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert is_not_p(ge_2_to)

    assert ge_2_to(2) is True
    assert ge_2_to(1) is False


def test_optimize_not_not():
    """~~p == p"""
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert is_not_p(ge_2_to)
    assert can_optimize(ge_2_to)

    optimized = optimize(ge_2_to)

    assert optimized == ge_2


def test_not_optimize_always_true():
    """~False == True"""
    always_true = ~always_false_p

    assert is_not_p(always_true)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert is_true_p(optimized)


def test_not_optimize_always_false():
    """~True == False"""
    always_false = ~always_true_p

    assert is_not_p(always_false)
    assert can_optimize(always_false)

    optimized = optimize(always_false)

    assert is_false_p(optimized)


def test_not_optimize_all():
    """"""
    eq_2 = eq_p(2)
    predicate = all_p(predicate=~eq_2)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ~any_p(predicate=eq_2)


def test_not_optimize_ge():
    """~ge(v) => lt(v)"""
    ge_2 = ge_p(2)
    predicate = ~ge_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == lt_p(2)


def test_not_optimize_gt():
    """~gt(v) => le(v)"""
    gt_2 = gt_p(2)
    predicate = ~gt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == le_p(2)


def test_not_optimize_le():
    """~lt(v) => ge(v)"""
    le_2 = le_p(2)
    predicate = ~le_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == gt_p(2)


def test_not_optimize_lt():
    """~lt(v) => ge(v)"""
    lt_2 = lt_p(2)
    predicate = ~lt_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ge_p(2)


def test_not_optimize_eq():
    """~(x == v) => x != v"""
    eq_2 = eq_p(2)
    predicate = ~eq_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == ne_p(2)


def test_not_optimize_ne():
    """~(x != v) => x == v"""
    ne_2 = ne_p(2)
    predicate = ~ne_2

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == eq_p(2)
