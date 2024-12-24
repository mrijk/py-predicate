from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.implies_predicate import ImpliesPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_predicates import (
    InPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)


def set_to_latex_set(v: set) -> str:
    items = ", ".join(str(item) for item in v)
    return f"\\{{{items}\\}}"


def to_latex(predicate: Predicate) -> str:
    """Format predicate as LaTeX."""
    match predicate:
        case AllPredicate(all_predicate):
            return f"\\forall x \\in S, {to_latex(all_predicate)}"
        case AlwaysFalsePredicate():
            return "False"
        case AlwaysTruePredicate():
            return "True"
        case AndPredicate(left, right):
            return f"{to_latex(left)} \\wedge {to_latex(right)}"
        case AnyPredicate(all_predicate):
            return f"\\exists x \\in S, {to_latex(all_predicate)}"
        case EqPredicate(v):
            return f"x = {v}"
        case GePredicate(v):
            return f"x \\ge {v}"
        case GeLePredicate(lower, upper):
            return f"{lower} \\le x \\le {upper}"
        case GeLtPredicate(lower, upper):
            return f"{lower} \\le x \\lt {upper}"
        case GtLePredicate(lower, upper):
            return f"{lower} \\lt x \\le {upper}"
        case GtLtPredicate(lower, upper):
            return f"{lower} \\lt x \\lt {upper}"
        case GtPredicate(v):
            return f"x \\gt {v}"
        case ImpliesPredicate(p):
            return f"p \\implies {to_latex(p)}"
        case InPredicate(v):
            return f"x \\in {set_to_latex_set(v)}"
        case IsRealSubsetPredicate(v):
            return f"x \\subseteq {set_to_latex_set(v)}"
        case IsSubsetPredicate(v):
            return f"x \\subset {set_to_latex_set(v)}"
        case IsRealSupersetPredicate(v):
            return f"x \\supseteq {set_to_latex_set(v)}"
        case IsSupersetPredicate(v):
            return f"x \\supset {set_to_latex_set(v)}"
        case LePredicate(v):
            return f"x \\le {v}"
        case LtPredicate(v):
            return f"x \\lt {v}"
        case NePredicate(v):
            return f"x \\neq {v}"
        case NotPredicate(child):
            return f"\\neg {to_latex(child)}"
        case OrPredicate(left, right):
            return f"{to_latex(left)} \\vee {to_latex(right)}"
        case XorPredicate(left, right):
            return f"{to_latex(left)} \\oplus {to_latex(right)}"
        case _:
            raise ValueError(f"Unknown predicate type {predicate}")
