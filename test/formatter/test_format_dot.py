from dataclasses import dataclass

import pytest

from predicate import (
    Predicate,
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    comp_p,
    eq_p,
    fn_p,
    ge_p,
    gt_p,
    in_p,
    is_instance_p,
    is_list_p,
    is_none_p,
    is_str_p,
    lazy_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
    to_dot,
)


def test_format_dot_false():
    predicate = always_false_p

    dot = to_dot(predicate, "test")

    assert dot


def test_format_dot_true():
    predicate = always_true_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_and():
    predicate = always_true_p & always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_or():
    predicate = always_true_p | always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_xor():
    predicate = always_true_p ^ always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_all():
    predicate = all_p(predicate=always_true_p)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_any():
    predicate = any_p(predicate=always_true_p)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_not():
    predicate = ~always_true_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_eq():
    predicate = eq_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_ge():
    predicate = ge_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_gt():
    predicate = gt_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_in():
    predicate = in_p(1, 2, 3)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_le():
    predicate = le_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_lt():
    predicate = lt_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_ne():
    predicate = ne_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_not_in():
    predicate = not_in_p(1, 2, 3)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_is_none():
    predicate = is_none_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_show_optimized():
    predicate = always_true_p & always_false_p

    dot = to_dot(predicate, show_optimized=True)

    assert dot


def test_format_dot_fn():
    predicate = fn_p(lambda x: x)

    dot = to_dot(predicate)

    assert dot


def test_format_comp_p():
    predicate = comp_p(lambda x: 2 * x, predicate=ge_p(2))

    dot = to_dot(predicate)

    assert dot


def test_format_dot_is_instance():
    predicate = is_instance_p(str)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_lazy():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str")))

    dot = to_dot(str_or_list_of_str)

    assert dot


def test_format_dot_laz_unknown():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str_unknown_ref")))

    dot = to_dot(str_or_list_of_str)

    assert dot


def test_format_dot_unknown():
    @dataclass
    class UnknownPredicate[T](Predicate[T]):
        def __call__(self, *args, **kwargs) -> bool:
            return False

    predicate = UnknownPredicate()

    with pytest.raises(ValueError):
        to_dot(predicate)
