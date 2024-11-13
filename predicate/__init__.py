"""The py-predicate module."""

__version__ = "0.0.1"

from predicate.formatter.format_dot import to_dot
from predicate.formatter.format_json import to_json
from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsEmptyPredicate,
    IsInstancePredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
    always_false_p,
    always_true_p,
    is_empty_p,
)
from predicate.standard_predicates import (
    all_p,
    any_p,
    comp_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    fn_p,
    ge_p,
    gt_p,
    in_p,
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_datetime_p,
    is_dict_p,
    is_float_p,
    is_instance_p,
    is_int_p,
    is_iterable_of_p,
    is_iterable_p,
    is_list_of_p,
    is_list_p,
    is_none_p,
    is_not_none_p,
    is_predicate_p,
    is_set_of_p,
    is_set_p,
    is_str_p,
    is_tuple_of_p,
    is_tuple_p,
    is_uuid_p,
    lazy_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
    regex_p,
)

__all__ = [
    "AllPredicate",
    "AlwaysFalsePredicate",
    "AlwaysTruePredicate",
    "AndPredicate",
    "AnyPredicate",
    "EqPredicate",
    "FnPredicate",
    "GePredicate",
    "GtPredicate",
    "InPredicate",
    "IsEmptyPredicate",
    "IsInstancePredicate",
    "IsNonePredicate",
    "IsNotNonePredicate",
    "LePredicate",
    "LtPredicate",
    "NePredicate",
    "NotInPredicate",
    "NotPredicate",
    "OrPredicate",
    "Predicate",
    "XorPredicate",
    "all_p",
    "always_false_p",
    "always_true_p",
    "any_p",
    "can_optimize",
    "comp_p",
    "eq_false_p",
    "eq_p",
    "eq_true_p",
    "falsy_p",
    "fn_p",
    "ge_p",
    "gt_p",
    "in_p",
    "is_bool_p",
    "is_callable_p",
    "is_complex_p",
    "is_datetime_p",
    "is_dict_p",
    "is_empty_p",
    "is_float_p",
    "is_instance_p",
    "is_int_p",
    "is_iterable_p",
    "is_iterable_of_p",
    "is_list_p",
    "is_list_of_p",
    "is_none_p",
    "is_not_none_p",
    "is_predicate_p",
    "is_set_p",
    "is_set_of_p",
    "is_str_p",
    "is_tuple_p",
    "is_tuple_of_p",
    "is_uuid_p",
    "lazy_p",
    "le_p",
    "lt_p",
    "ne_p",
    "not_in_p",
    "optimize",
    "regex_p",
    "to_dot",
    "to_json",
]
