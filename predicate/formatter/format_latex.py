from typing import Any, Iterable

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.compile_predicate import CompiledPredicate
from predicate.count_predicate import CountPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.helpers import fn_name, join_as_str
from predicate.implies_predicate import ImpliesPredicate
from predicate.in_predicate import InPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.not_predicate import NotPredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.reduce_predicate import ReducePredicate
from predicate.set_predicates import (
    IntersectsPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)
from predicate.xor_predicate import XorPredicate


def set_to_latex_set(v: Iterable[Any]) -> str:
    return f"\\{{{join_as_str(v)}\\}}"


def to_latex(predicate: Predicate[Any], parameter: str = "x") -> str:  # noqa: C901
    """Format predicate as LaTeX."""
    match predicate:
        case CompiledPredicate(predicate=inner):
            return to_latex(inner, parameter=parameter)
        case AllPredicate(all_predicate):
            return f"\\forall {parameter} \\in S, {to_latex(all_predicate)}"
        case AlwaysFalsePredicate():
            return "False"
        case AlwaysTruePredicate():
            return "True"
        case AndPredicate(left, right):
            return f"{to_latex(left, parameter)} \\wedge {to_latex(right, parameter)}"
        case AnyPredicate(all_predicate):
            return f"\\exists {parameter} \\in S, {to_latex(all_predicate)}"
        case CountPredicate(predicate, length_p):
            return to_latex(HasLengthPredicate(length_p), parameter=f"\\{{x \\mid {to_latex(predicate)}\\}}")
        case EqPredicate(v):
            return f"{parameter} = {v}"
        case GePredicate(v):
            return f"{parameter} \\ge {v}"
        case GeLePredicate(lower, upper):
            return f"{lower} \\le {parameter} \\le {upper}"
        case GeLtPredicate(lower, upper):
            return f"{lower} \\le {parameter} \\lt {upper}"
        case GtLePredicate(lower, upper):
            return f"{lower} \\lt {parameter} \\le {upper}"
        case GtLtPredicate(lower, upper):
            return f"{lower} \\lt {parameter} \\lt {upper}"
        case GtPredicate(v):
            return f"{parameter} \\gt {v}"
        case HasLengthPredicate(length_p):
            return to_latex(length_p, parameter=f"\\left| {parameter} \\right|")
        case ImpliesPredicate(p):
            return f"p \\implies {to_latex(p)}"
        case InPredicate(v) if isinstance(v, Iterable):
            return f"{parameter} \\in {set_to_latex_set(v)}"
        case IntersectsPredicate(v):
            return f"{parameter} \\cap {set_to_latex_set(v)} \\neq \\emptyset"
        case IsRealSubsetPredicate(v):
            return f"{parameter} \\subseteq {set_to_latex_set(v)}"
        case IsSubsetPredicate(v):
            return f"{parameter} \\subset {set_to_latex_set(v)}"
        case IsRealSupersetPredicate(v):
            return f"{parameter} \\supseteq {set_to_latex_set(v)}"
        case IsSupersetPredicate(v):
            return f"{parameter} \\supset {set_to_latex_set(v)}"
        case LePredicate(v):
            return f"{parameter} \\le {v}"
        case LtPredicate(v):
            return f"{parameter} \\lt {v}"
        case NePredicate(v):
            return f"{parameter} \\neq {v}"
        case NotInPredicate(v) if isinstance(v, Iterable):
            return f"{parameter} \\notin {set_to_latex_set(v)}"
        case NotPredicate(child):
            return f"\\neg {to_latex(child, parameter)}"
        case OrPredicate(left, right):
            return f"{to_latex(left, parameter)} \\vee {to_latex(right, parameter)}"
        case XorPredicate(left, right):
            return f"{to_latex(left, parameter)} \\oplus {to_latex(right, parameter)}"
        case ReducePredicate(fn, initial):
            name = fn_name(fn)
            return rf"\text{{reduce}}({name}, {initial!r})"
        case _:
            raise ValueError(f"Unknown predicate type {predicate}")
