import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    comp_p,
    eq_p,
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
    is_bool_p,
    is_dict_of_p,
    is_empty_p,
    is_falsy_p,
    is_lambda_p,
    is_list_of_p,
    is_none_p,
    is_not_empty_p,
    is_not_none_p,
    is_set_of_p,
    is_str_p,
    is_truthy_p,
    is_tuple_of_p,
    lazy_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
    regex_p,
    tee_p,
)
from predicate.implies_predicate import implies_p
from predicate.ip_address_predicates import is_ipv4_network_global_p
from predicate.is_callable_predicate import is_callable_p
from predicate.named_predicate import NamedPredicate
from predicate.set_predicates import is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p
from predicate.standard_predicates import (
    is_int_p,
    this_p,
)


@pytest.mark.parametrize(
    ("predicate", "representation"),
    [
        (always_false_p, "always_false_p"),
        (always_true_p, "always_true_p"),
        (always_false_p & always_true_p, "always_false_p & always_true_p"),
        (always_false_p | always_true_p, "always_false_p | always_true_p"),
        (always_false_p ^ always_true_p, "always_false_p ^ always_true_p"),
        (~always_false_p, "~always_false_p"),
        (all_p(eq_p(2)), "all_p(eq_p(2))"),
        (any_p(eq_p(2)), "any_p(eq_p(2))"),
        (comp_p(lambda x: x, eq_p(2)), "comp_p(eq_p(2))"),
        (eq_p(2), "eq_p(2)"),
        (fn_p(lambda x: x), "fn_p(predicate_fn=<lambda>)"),
        (ge_p(2), "ge_p(2)"),
        (gt_p(2), "gt_p(2)"),
        (ge_le_p(2, 3), "ge_le_p(2, 3)"),
        (gt_le_p(2, 3), "gt_le_p(2, 3)"),
        (ge_lt_p(2, 3), "ge_lt_p(2, 3)"),
        (gt_lt_p(2, 3), "gt_lt_p(2, 3)"),
        (has_key_p("foo"), 'has_key_p("foo")'),
        (has_length_p(eq_p(42)), "has_length_p(eq_p(42))"),
        (has_path_p(is_str_p), "has_path_p(is_str_p)"),
        (implies_p(ge_p(2)), "implies_p(ge_p(2))"),
        (in_p(2, 3, 4), "in_p(2, 3, 4)"),
        (is_callable_p([int], bool), "is_callable_p([], bool)"),
        (is_empty_p, "has_length_p(eq_p(0))"),
        (is_lambda_p, "is_lambda_p"),
        (is_not_empty_p, "has_length_p(gt_p(0))"),
        (is_none_p, "is_none_p"),
        (is_not_none_p, "is_not_none_p"),
        (is_str_p, "is_str_p"),
        (is_real_subset_p({1, 2, 3}), "is_real_subset_p({1, 2, 3})"),
        (is_subset_p({1, 2, 3}), "is_subset_p({1, 2, 3})"),
        (is_real_superset_p({1, 2, 3}), "is_real_superset_p({1, 2, 3})"),
        (is_superset_p({1, 2, 3}), "is_superset_p({1, 2, 3})"),
        (is_falsy_p, "is_falsy_p"),
        (is_truthy_p, "is_truthy_p"),
        (is_dict_of_p(), "is_dict_of_p()"),
        (is_dict_of_p(("x", is_str_p), ("y", is_int_p)), "is_dict_of_p(('x', is_str_p), ('y', is_int_p))"),
        (is_list_of_p(is_str_p), "is_list_of_p(is_str_p)"),
        (is_set_of_p(is_str_p), "is_set_of_p(is_str_p)"),
        (is_tuple_of_p(is_str_p, is_bool_p), "is_tuple_of_p(is_str_p, is_bool_p)"),
        (lazy_p("ref"), 'lazy_p("ref")'),
        (le_p(2), "le_p(2)"),
        (lt_p(2), "lt_p(2)"),
        (ne_p(2), "ne_p(2)"),
        (not_in_p(2, 3, 4), "not_in_p(2, 3, 4)"),
        (regex_p("^foo.*bar$"), 'regex_p("^foo.*bar$")'),
        (tee_p(lambda x: None), "tee_p"),
        (this_p, "this_p"),
        (NamedPredicate(name="foo"), "foo"),
        (is_ipv4_network_global_p, "property_p()"),
    ],
)
def test_repr_standard(predicate, representation):
    assert repr(predicate) == representation


@pytest.mark.parametrize(
    ("predicate", "representation"),
    [(always_false_p & in_p(2, 3, 4) & not_in_p(3), "always_false_p & in_p(2, 3, 4) & not_in_p(3)")],
)
def test_repr_combined(predicate, representation):
    assert repr(predicate) == representation
