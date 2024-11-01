"""The py-predicate module."""

__version__ = "0.0.1"

from predicate.optimizer.predicate_optimizer import can_optimize, optimize
from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    EqPredicate,
    FnPredicate,
    InPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
    always_false_p,
    always_true_p,
)
from predicate.standard_predicates import ge_p, gt_p, le_p, lt_p

__all__ = [
    "ge_p",
    "gt_p",
    "le_p",
    "lt_p",
    "can_optimize",
    "optimize",
    "always_true_p",
    "AllPredicate",
    "AndPredicate",
    "AnyPredicate",
    "InPredicate",
    "FnPredicate",
    "NePredicate",
    "NotInPredicate",
    "XorPredicate",
    "always_false_p",
    "AlwaysTruePredicate",
    "AlwaysFalsePredicate",
    "EqPredicate",
    "NotPredicate",
    "OrPredicate",
    "Predicate",
]
