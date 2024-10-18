from predicate.predicate import (
    ge_p,
    always_false_p,
    NotPredicate,
    AlwaysTruePredicate,
    always_true_p,
    AlwaysFalsePredicate,
)
from predicate.optimizer.predicate_optimizer import optimize, can_optimize


def test_not():
    ge_2 = ge_p(2)
    lt_2 = ~ge_2

    assert isinstance(lt_2, NotPredicate)

    assert lt_2(2) is False
    assert lt_2(1) is True


def test_not_not():
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert isinstance(ge_2_to, NotPredicate)

    assert ge_2_to(2) is True
    assert ge_2_to(1) is False


def test_optimize_not_not():
    """~~p == p"""
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert isinstance(ge_2_to, NotPredicate)

    optimized = optimize(ge_2_to)

    assert isinstance(optimized, NotPredicate) is False

    assert optimized(2) is True
    assert optimized(1) is False


def test_not_optimize_always_true():
    """~False == True"""
    always_true = ~always_false_p

    assert isinstance(always_true, NotPredicate)
    assert can_optimize(always_true)

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)


def test_not_optimize_always_false():
    """~True == False"""
    always_false = ~always_true_p

    assert isinstance(always_false, NotPredicate)
    assert can_optimize(always_false)

    optimized = optimize(always_false)

    assert isinstance(optimized, AlwaysFalsePredicate)
