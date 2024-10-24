from predicate import can_optimize, optimize
from predicate.predicate import Predicate, always_true_p, always_false_p
from predicate.standard_predicates import all_p, is_int_p, eq_p, is_str_p, ge_p
from helpers import is_all_p, is_true_p


def test_all():
    all_int = all_p(is_int_p)

    assert all_int([1, 2, 3]) is True
    assert all_int([None, 2, 3]) is False


def test_all_combined_1():
    all_eq_2_or_3 = all_p((is_int_p & (eq_p(2) | eq_p(3))) | eq_p("3"))

    assert all_eq_2_or_3([2, "3", 2, 3]) is True
    assert all_eq_2_or_3([1, 3, 2, 3]) is False


def test_all_combined_2():
    str_len_3_p = Predicate[str](lambda x: len(x) == 3)
    all_len_3_p = all_p(is_str_p & str_len_3_p)

    assert all_len_3_p(["aaa", "bbb", "ccc"]) is True
    assert all_len_3_p(["aaa", 3, "ccc"]) is False
    assert all_len_3_p(["aaa", "bbbb", "ccc"]) is False


def test_optimize_all_true():
    predicate = all_p(always_true_p)

    assert is_all_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == always_true_p


def test_optimize_all_false():
    predicate = all_p(always_false_p)

    assert is_all_p(predicate)
    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert not is_all_p(optimized)


def test_optimize_and_all():
    all_ge_2 = all_p(ge_p(2))
    all_ge_3 = all_p(ge_p(3))

    predicate = all_ge_2 & all_ge_3

    assert can_optimize(predicate)

    optimized = optimize(predicate)

    assert optimized == all_ge_3
