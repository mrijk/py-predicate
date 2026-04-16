"""The py-predicate module."""

__version__ = "1.6.0"

from predicate.all_predicate import all_p
from predicate.always_false_predicate import always_false_p, never_p
from predicate.always_true_predicate import always_p, always_true_p
from predicate.analysis import are_equivalent, is_satisfiable, is_tautology
from predicate.any_predicate import any_p
from predicate.comp_predicate import comp_p
from predicate.count_predicate import count_p, exactly_one_p, exactly_zero_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.eq_predicate import eq_false_p, eq_p, eq_true_p, zero_p
from predicate.exactly_predicate import exactly_n
from predicate.exception_predicate import PredicateError, exception_p
from predicate.compile_predicate import CompiledPredicate, NotCompilableError, compile_predicate, try_compile_predicate
from predicate.explain import explain
from predicate.fn_predicate import fn_p, is_even_p, is_finite_p, is_inf_p, is_nan_p, is_odd_p
from predicate.formatter import to_dot, to_json, to_latex, to_yaml
from predicate.ge_predicate import ge_p
from predicate.generator.generate_false import generate_false
from predicate.generator.generate_true import generate_true
from predicate.gt_predicate import gt_p, pos_p
from predicate.has_key_predicate import has_key_p
from predicate.has_length_predicate import has_length_p, is_empty_p, is_not_empty_p
from predicate.has_path_predicate import has_path_p
from predicate.implies_predicate import implies_p
from predicate.in_predicate import in_p
from predicate.is_async_predicate import is_async_p
from predicate.is_close_predicate import is_close_p
from predicate.is_falsy_predicate import is_falsy_p
from predicate.is_instance_predicate import (
    is_bool_p,
    is_bytes_p,
    is_callable_p,
    is_complex_p,
    is_container_p,
    is_date_p,
    is_datetime_p,
    is_frozenset_p,
    is_hashable_p,
    is_instance_p,
    is_iterable_p,
    is_mapping_p,
    is_path_p,
    is_predicate_p,
    is_range_p,
    is_sequence_p,
    is_set_p,
    is_time_p,
    is_timedelta_p,
    is_tuple_p,
    is_uuid_p,
)
from predicate.is_lambda_predicate import is_lambda_p, is_lambda_with_signature_p
from predicate.is_none_predicate import is_none_p, none_is_exception_p, none_is_true_p
from predicate.is_not_none_predicate import is_not_none_p, none_is_false_p
from predicate.is_predicate import is_p
from predicate.is_predicate_of_p import is_predicate_of_p
from predicate.is_same_predicate import is_same_p
from predicate.is_subclass_predicate import is_enum_p, is_int_enum_p, is_str_enum_p, is_subclass_p
from predicate.is_truthy_predicate import is_truthy_p
from predicate.juxt_predicate import juxt_p
from predicate.lazy_predicate import lazy_p
from predicate.le_predicate import le_p
from predicate.list_of_predicate import is_list_of_p
from predicate.lt_predicate import lt_p, neg_p
from predicate.match_predicate import match_p
from predicate.mutual_recur_predicate import mutual_recur_p
from predicate.ne_predicate import ne_p
from predicate.not_in_predicate import not_in_p
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.optional_predicate import optional
from predicate.plus_predicate import plus
from predicate.predicate import and_p, or_p, xor_p
from predicate.raises_predicate import RaisesPredicate, raises_exception_p, raises_p
from predicate.range_predicate import ge_le_p, ge_lt_p, gt_le_p, gt_lt_p
from predicate.recur_predicate import recur_p
from predicate.reduce_predicate import reduce_p
from predicate.regex_predicate import regex_p
from predicate.repeat_predicate import repeat
from predicate.set_of_predicate import is_set_of_p
from predicate.set_predicates import (
    IntersectsPredicate,
    intersects_p,
    is_real_subset_p,
    is_real_superset_p,
    is_subset_p,
    is_superset_p,
)
from predicate.spec.exercise import exercise
from predicate.spec.instrument import (
    instrument,
    instrument_class,
    instrument_function,
    instrument_module,
    is_instrumented,
)
from predicate.spec.spec import Spec
from predicate.standard_predicates import (
    is_dict_p,
    is_float_p,
    is_int_p,
    is_iterable_of_p,
    is_list_p,
    is_number_p,
    is_str_p,
    root_p,
    this_p,
)
from predicate.star_predicate import star
from predicate.struct_predicate import is_struct_p
from predicate.tee_predicate import tee_p
from predicate.tuple_of_predicate import is_tuple_of_p

__all__ = [
    "PredicateError",
    "Spec",
    "are_equivalent",
    "is_satisfiable",
    "is_tautology",
    "all_p",
    "always_false_p",
    "always_p",
    "always_true_p",
    "and_p",
    "any_p",
    "can_optimize",
    "compile_predicate",
    "CompiledPredicate",
    "comp_p",
    "NotCompilableError",
    "count_p",
    "eq_false_p",
    "eq_p",
    "ends_with_p",
    "eq_true_p",
    "exactly_n",
    "exactly_one_p",
    "exactly_zero_p",
    "exception_p",
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
    "IntersectsPredicate",
    "intersects_p",
    "instrument",
    "instrument_class",
    "instrument_function",
    "instrument_module",
    "is_instrumented",
    "is_alnum_p",
    "is_alpha_p",
    "is_ascii_p",
    "is_async_p",
    "is_bool_p",
    "is_bytes_p",
    "is_callable_p",
    "is_close_p",
    "is_complex_p",
    "is_container_p",
    "is_date_p",
    "is_datetime_p",
    "is_decimal_p",
    "is_digit_p",
    "is_dict_of_p",
    "is_dict_p",
    "is_frozenset_p",
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
    "is_int_enum_p",
    "is_int_p",
    "is_iterable_of_p",
    "is_iterable_p",
    "is_lambda_p",
    "is_lambda_with_signature_p",
    "is_list_of_p",
    "is_list_p",
    "is_lower_p",
    "is_mapping_p",
    "is_same_p",
    "is_nan_p",
    "is_none_p",
    "is_not_empty_p",
    "is_not_none_p",
    "is_numeric_p",
    "is_number_p",
    "is_odd_p",
    "is_p",
    "is_path_p",
    "is_predicate_of_p",
    "is_predicate_p",
    "is_printable_p",
    "is_range_p",
    "is_real_subset_p",
    "is_real_superset_p",
    "is_sequence_p",
    "is_set_of_p",
    "is_set_p",
    "is_space_p",
    "is_str_enum_p",
    "is_str_p",
    "is_struct_p",
    "is_subclass_p",
    "is_subset_p",
    "is_superset_p",
    "is_time_p",
    "is_timedelta_p",
    "is_title_p",
    "is_truthy_p",
    "is_tuple_of_p",
    "is_tuple_p",
    "is_upper_p",
    "is_uuid_p",
    "juxt_p",
    "lazy_p",
    "le_p",
    "lt_p",
    "match_p",
    "mutual_recur_p",
    "ne_p",
    "neg_p",
    "never_p",
    "none_is_exception_p",
    "none_is_false_p",
    "none_is_true_p",
    "not_in_p",
    "optimize",
    "optional",
    "or_p",
    "plus",
    "pos_p",
    "recur_p",
    "reduce_p",
    "RaisesPredicate",
    "raises_exception_p",
    "raises_p",
    "regex_p",
    "repeat",
    "root_p",
    "star",
    "starts_with_p",
    "tee_p",
    "this_p",
    "try_compile_predicate",
    "to_dot",
    "to_json",
    "to_latex",
    "to_yaml",
    "xor_p",
    "zero_p",
]

from predicate.str_predicates import (
    ends_with_p,
    is_alnum_p,
    is_alpha_p,
    is_ascii_p,
    is_decimal_p,
    is_digit_p,
    is_identifier_p,
    is_lower_p,
    is_numeric_p,
    is_printable_p,
    is_space_p,
    is_title_p,
    is_upper_p,
    starts_with_p,
)
