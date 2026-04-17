import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    comp_p,
    count_p,
    eq_p,
    exactly_n,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    has_path_p,
    in_p,
    is_close_p,
    is_dict_of_p,
    is_falsy_p,
    is_instance_p,
    is_list_of_p,
    is_list_p,
    is_none_p,
    is_not_none_p,
    is_same_p,
    is_set_of_p,
    is_str_p,
    is_subclass_p,
    is_truthy_p,
    is_tuple_of_p,
    lazy_p,
    le_p,
    lt_p,
    match_p,
    ne_p,
    not_in_p,
    optional,
    plus,
    reduce_p,
    regex_p,
    repeat,
    star,
    tee_p,
    to_dot,
)
from predicate.implies import Implies
from predicate.named_predicate import NamedPredicate
from predicate.set_predicates import intersects_p, is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p
from predicate.standard_predicates import (
    is_int_p,
    root_p,
    this_p,
)


@pytest.mark.parametrize(
    "predicate",
    [
        always_false_p,
        always_true_p,
        is_falsy_p,
        is_truthy_p,
        intersects_p({1, 2, 3}),
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


def test_format_dot_implies(p, q):
    predicate = Implies(p, q)

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
    predicate = in_p({1, 2, 3})

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
    predicate = not_in_p({1, 2, 3})

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


def test_format_dot_juxt():
    from predicate import exactly_one_p, juxt_p

    predicate = juxt_p(is_int_p, is_str_p, evaluate=exactly_one_p(predicate=eq_p(True)))

    dot = to_dot(predicate)

    assert dot


def test_format_dot_count():
    assert to_dot(count_p(is_int_p, eq_p(2)))


def test_format_dot_exactly():
    assert to_dot(exactly_n(3, is_int_p))


def test_format_dot_has_key():
    assert to_dot(has_key_p(eq_p("name")))


def test_format_dot_has_length():
    assert to_dot(has_length_p(eq_p(3)))


def test_format_dot_has_path():
    assert to_dot(has_path_p(eq_p("a"), eq_p("b")))


def test_format_dot_is_close():
    assert to_dot(is_close_p(1.0))


def test_format_dot_is_not_none():
    assert to_dot(is_not_none_p)


def test_format_dot_is_same():
    assert to_dot(is_same_p(always_true_p))


def test_format_dot_is_subclass_single():
    assert to_dot(is_subclass_p(int))


def test_format_dot_is_subclass_tuple():
    assert to_dot(is_subclass_p((int, str)))


def test_format_dot_is_subclass_union():
    assert to_dot(is_subclass_p(int | str))


def test_format_dot_list_of():
    assert to_dot(is_list_of_p(is_int_p))


def test_format_dot_match():
    assert to_dot(match_p(is_int_p, is_str_p))


def test_format_dot_optional():
    assert to_dot(optional(is_int_p))


def test_format_dot_plus():
    assert to_dot(plus(is_int_p))


def test_format_dot_reduce():
    assert to_dot(reduce_p(lambda acc, x: (acc + x, ge_p(0)), 0))


def test_format_dot_regex():
    assert to_dot(regex_p(r"\d+"))


def test_format_dot_repeat():
    assert to_dot(repeat(2, 4, is_int_p))


def test_format_dot_set_of():
    assert to_dot(is_set_of_p(is_int_p))


def test_format_dot_star():
    assert to_dot(star(is_int_p))
