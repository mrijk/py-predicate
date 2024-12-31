"""The py-predicate module."""

__version__ = "0.0.1"

from predicate.always_false_predicate import always_false_p, never_p
from predicate.always_true_predicate import always_p, always_true_p
from predicate.explain import explain
from predicate.formatter import to_dot, to_json, to_latex
from predicate.generator.generate_false import generate_false
from predicate.generator.generate_true import generate_true
from predicate.is_empty_predicate import is_empty_p, is_not_empty_p
from predicate.is_lambda_predicate import is_lambda_p, is_lambda_with_signature_p
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.set_predicates import (
    in_p,
    is_real_subset_p,
    is_real_superset_p,
    is_subset_p,
    is_superset_p,
    not_in_p,
)
from predicate.standard_predicates import (
    all_p,
    any_p,
    comp_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_dict_of_p,
    is_dict_p,
    is_falsy_p,
    is_finite_p,
    is_float_p,
    is_hashable_p,
    is_inf_p,
    is_instance_p,
    is_int_p,
    is_iterable_of_p,
    is_iterable_p,
    is_list_of_p,
    is_list_p,
    is_nan_p,
    is_none_p,
    is_not_none_p,
    is_predicate_p,
    is_range_p,
    is_set_of_p,
    is_set_p,
    is_str_p,
    is_truthy_p,
    is_tuple_of_p,
    is_tuple_p,
    is_uuid_p,
    lazy_p,
    le_p,
    lt_p,
    ne_p,
    neg_p,
    pos_p,
    regex_p,
    root_p,
    tee_p,
    this_p,
    zero_p,
)

__all__ = [
    "all_p",
    "always_false_p",
    "always_p",
    "always_true_p",
    "any_p",
    "can_optimize",
    "comp_p",
    "eq_false_p",
    "eq_p",
    "eq_true_p",
    "explain",
    "fn_p",
    "ge_le_p",
    "ge_lt_p",
    "ge_p",
    "generate_false",
    "generate_true",
    "gt_le_p",
    "gt_lt_p",
    "gt_p",
    "has_key_p",
    "has_length_p",
    "in_p",
    "is_alnum_p",
    "is_alpha_p",
    "is_ascii_p",
    "is_bool_p",
    "is_callable_p",
    "is_complex_p",
    "is_container_p",
    "is_datetime_p",
    "is_decimal_p",
    "is_dict_of_p",
    "is_dict_p",
    "is_empty_p",
    "is_falsy_p",
    "is_finite_p",
    "is_float_p",
    "is_hashable_p",
    "is_identifier_p",
    "is_inf_p",
    "is_instance_p",
    "is_int_p",
    "is_iterable_of_p",
    "is_iterable_p",
    "is_lambda_p",
    "is_lambda_with_signature_p",
    "is_list_of_p",
    "is_list_p",
    "is_lower_p",
    "is_nan_p",
    "is_none_p",
    "is_not_empty_p",
    "is_not_none_p",
    "is_predicate_of_p",
    "is_predicate_p",
    "is_range_p",
    "is_set_of_p",
    "is_set_p",
    "is_str_p",
    "is_subset_p",
    "is_superset_p",
    "is_real_subset_p",
    "is_real_superset_p",
    "is_title_p",
    "is_truthy_p",
    "is_tuple_of_p",
    "is_tuple_p",
    "is_upper_p",
    "is_uuid_p",
    "lazy_p",
    "le_p",
    "lt_p",
    "ne_p",
    "neg_p",
    "never_p",
    "not_in_p",
    "optimize",
    "pos_p",
    "regex_p",
    "root_p",
    "tee_p",
    "this_p",
    "to_dot",
    "to_json",
    "to_latex",
    "zero_p",
]

from predicate.str_predicates import (
    is_alnum_p,
    is_alpha_p,
    is_ascii_p,
    is_decimal_p,
    is_identifier_p,
    is_lower_p,
    is_title_p,
    is_upper_p,
)
