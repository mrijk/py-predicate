from predicate import (
    always_false_p,
    always_true_p,
    any_p,
    can_optimize,
    eq_p,
    is_list_of_p,
    is_none_p,
    is_not_none_p,
    is_str_p,
    ne_p,
    optimize,
)
from predicate.has_length_predicate import is_empty_p
from predicate.is_instance_predicate import is_list_p


def test_optimize_list_of_true():
    # is_list_of_p(always_true_p) == is_list_p
    predicate = is_list_of_p(always_true_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_list_p


def test_optimize_list_of_false():
    # is_list_of_p(always_false_p) == is_list_p & is_empty_p
    predicate = is_list_of_p(always_false_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == (is_list_p & is_empty_p)


def test_optimize_list_of_not(p):
    # is_list_of_p(~p) == is_list_p & ~any_p(p)
    predicate = is_list_of_p(~p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == (is_list_p & ~any_p(p))


def test_optimize_list_of_not_none():
    # is_list_of_p(is_not_none_p) == is_list_p & ~any_p(is_none_p)
    predicate = is_list_of_p(is_not_none_p)

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == (is_list_p & ~any_p(is_none_p))


def test_optimize_list_of_inner():
    # inner predicate is optimizable — propagate
    predicate = is_list_of_p(~eq_p(2))

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == is_list_of_p(ne_p(2))


def test_not_optimize_list_of():
    predicate = is_list_of_p(is_str_p)

    assert not can_optimize(predicate)


def test_optimize_list_of_true_semantics():
    optimized = optimize(is_list_of_p(always_true_p))

    assert optimized([1, "x", None])
    assert not optimized("not-a-list")
    assert not optimized(42)


def test_optimize_list_of_false_semantics():
    optimized = optimize(is_list_of_p(always_false_p))

    assert optimized([])
    assert not optimized([1])
    assert not optimized("not-a-list")


def test_optimize_list_of_not_semantics(p):
    optimized = optimize(is_list_of_p(~p))

    original = is_list_of_p(~p)

    for x in [[], [1, 2], ["a"], [True], [None]]:
        assert optimized(x) == original(x)
