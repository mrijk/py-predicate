from predicate.predicate import gt_p, NotPredicate, AlwaysFalsePredicate, AlwaysTruePredicate
from predicate.predicate_optimizer import can_optimize, optimize


def test_optimize_not_or():
    """ ~(p | ~p) == False"""
    p = gt_p(2)

    always_false = ~(p | ~p)

    assert isinstance(always_false, NotPredicate)
    assert can_optimize(always_false) is True

    optimized = optimize(always_false)

    assert isinstance(optimized, AlwaysFalsePredicate)


def test_optimize_not_and():
    """ ~(p & ~p) == True"""
    p = gt_p(2)

    always_true = ~(p & ~p)

    assert isinstance(always_true, NotPredicate)
    assert can_optimize(always_true) is True

    optimized = optimize(always_true)

    assert isinstance(optimized, AlwaysTruePredicate)