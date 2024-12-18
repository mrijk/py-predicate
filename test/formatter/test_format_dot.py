import pytest

from predicate import (
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
    is_falsy_p,
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
from predicate.named_predicate import NamedPredicate
from predicate.set_predicates import is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p
from predicate.standard_predicates import (
    ge_le_p,
    ge_lt_p,
    gt_le_p,
    gt_lt_p,
    is_dict_of_p,
    is_int_p,
    is_truthy_p,
    is_tuple_of_p,
    root_p,
    tee_p,
    this_p,
)


@pytest.mark.parametrize(
    "predicate",
    [
        always_false_p,
        always_true_p,
        is_falsy_p,
        is_truthy_p,
        is_subset_p({1, 2, 3}),
        is_real_subset_p({1, 2, 3}),
        is_superset_p({1, 2, 3}),
        is_real_superset_p({1, 2, 3}),
    ],
)
def test_format_dot(predicate):
    dot = to_dot(predicate, "test")

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


def test_format_dot_ge_le():
    predicate = ge_le_p(13, 42)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_ge_lt():
    predicate = ge_lt_p(13, 42)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_gt_le():
    predicate = gt_le_p(13, 42)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_gt_lt():
    predicate = gt_lt_p(13, 42)

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


def test_format_dot_dict_of():
    predicate = is_dict_of_p((is_str_p, is_int_p))

    dot = to_dot(predicate)

    assert dot


def test_format_dot_tuple_of():
    predicate = is_tuple_of_p(is_str_p, is_int_p)

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


def test_format_dot_comp_p():
    predicate = comp_p(lambda x: 2 * x, predicate=ge_p(2))

    dot = to_dot(predicate)

    assert dot


def test_format_dot_named():
    predicate = NamedPredicate(name="p")

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


def test_format_dot_root():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(root_p))

    dot = to_dot(str_or_list_of_str)

    assert dot


def test_format_dot_this():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(this_p))

    dot = to_dot(str_or_list_of_str)

    assert dot


def test_format_dot_tee():
    predicate = tee_p(fn=lambda _: None)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_laz_unknown():
    str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str_unknown_ref")))

    dot = to_dot(str_or_list_of_str)

    assert dot


def test_format_dot_unknown(unknown_p):
    with pytest.raises(ValueError):
        to_dot(unknown_p)
