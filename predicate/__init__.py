"""The py-predicate module."""

__version__ = "0.0.1"

from predicate.all_predicate import all_p
from predicate.always_false_predicate import always_false_p, never_p
from predicate.always_true_predicate import always_p, always_true_p
from predicate.any_predicate import any_p
from predicate.comp_predicate import comp_p
from predicate.count_predicate import count_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.eq_predicate import eq_false_p, eq_p, eq_true_p, zero_p
from predicate.explain import explain
from predicate.fn_predicate import fn_p, is_even_p, is_finite_p, is_inf_p, is_nan_p, is_odd_p
from predicate.formatter import to_dot, to_json, to_latex
from predicate.ge_predicate import ge_p
from predicate.generator.generate_false import generate_false
from predicate.generator.generate_true import generate_true
from predicate.gt_predicate import gt_p, pos_p
from predicate.has_key_predicate import has_key_p
from predicate.has_length_predicate import has_length_p, is_empty_p, is_not_empty_p
from predicate.has_path_predicate import has_path_p
from predicate.implies_predicate import implies_p
from predicate.in_predicate import in_p
from predicate.is_falsy_predicate import is_falsy_p
from predicate.is_instance_predicate import (
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_hashable_p,
    is_instance_p,
    is_iterable_p,
    is_predicate_p,
    is_range_p,
    is_set_p,
    is_tuple_p,
    is_uuid_p,
)
from predicate.is_lambda_predicate import is_lambda_p, is_lambda_with_signature_p
from predicate.is_none_predicate import is_none_p
from predicate.is_not_none_predicate import is_not_none_p
from predicate.is_predicate_of_p import is_predicate_of_p
from predicate.is_subclass_predicate import is_enum_p, is_int_enum_p, is_str_enum_p
from predicate.is_truthy_predicate import is_truthy_p
from predicate.lazy_predicate import lazy_p
from predicate.le_predicate import le_p
from predicate.list_of_predicate import is_list_of_p
from predicate.lt_predicate import lt_p, neg_p
from predicate.match_predicate import exactly_n, match_p, optional, plus, repeat, star
from predicate.ne_predicate import ne_p
from predicate.not_in_predicate import not_in_p
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.range_predicate import ge_le_p, ge_lt_p, gt_le_p, gt_lt_p
from predicate.regex_predicate import regex_p
from predicate.set_of_predicate import is_set_of_p
from predicate.set_predicates import (
    is_real_subset_p,
    is_real_superset_p,
    is_subset_p,
    is_superset_p,
)
from predicate.spec.exercise import exercise
from predicate.spec.instrument import instrument_function
from predicate.spec.spec import Spec
from predicate.standard_predicates import (
    is_dict_p,
    is_float_p,
    is_int_p,
    is_iterable_of_p,
    is_list_p,
    is_str_p,
    root_p,
    this_p,
)
from predicate.tee_predicate import tee_p
from predicate.tuple_of_predicate import is_tuple_of_p

__all__ = [
    "all_p",
    "always_false_p",
    "always_p",
    "always_true_p",
    "any_p",
    "can_optimize",
    "comp_p",
    "count_p",
    "eq_false_p",
    "eq_p",
    "eq_true_p",
    "exactly_n",
    "exercise",
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
    "has_path_p",
    "implies_p",
    "in_p",
    "instrument_function",
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
    "is_enum_p",
    "is_even_p",
    "is_falsy_p",
    "is_finite_p",
    "is_float_p",
    "is_hashable_p",
    "is_identifier_p",
    "is_inf_p",
    "is_instance_p",
    "is_int_p",
    "is_int_enum_p",
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
    "is_odd_p",
    "is_predicate_of_p",
    "is_predicate_p",
    "is_range_p",
    "is_set_of_p",
    "is_set_p",
    "is_str_p",
    "is_str_enum_p",
    "is_subclass_predicate",
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
    "match_p",
    "ne_p",
    "neg_p",
    "never_p",
    "not_in_p",
    "optimize",
    "optional",
    "plus",
    "pos_p",
    "regex_p",
    "repeat",
    "root_p",
    "star",
    "tee_p",
    "this_p",
    "to_dot",
    "to_json",
    "to_latex",
    "zero_p",
    "Spec",
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
