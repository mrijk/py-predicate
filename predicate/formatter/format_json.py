from typing import Any

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.fn_predicate import FnPredicate
from predicate.formatter.fn_source import get_fn_source
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.juxt_predicate import JuxtPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.tee_predicate import TeePredicate


def to_json(predicate: Predicate) -> dict[str, Any]:
    """Format predicate as json."""

    def to_value(predicate) -> tuple[str, Any]:
        match predicate:
            case AllPredicate(all_predicate):
                return "all", {"predicate": to_json(all_predicate)}
            case AlwaysFalsePredicate():
                return "false", False
            case AlwaysTruePredicate():
                return "true", True
            case AndPredicate(left, right):
                return "and", {"left": to_json(left), "right": to_json(right)}
            case AnyPredicate(any_predicate):
                return "any", {"predicate": to_json(any_predicate)}
            case EqPredicate(v):
                return "eq", {"v": v}
            case FnPredicate(predicate_fn):
                name = getattr(predicate_fn, "__name__", str(predicate_fn))
                fn_info: dict[str, Any] = {"name": name}
                fn_info.update(get_fn_source(predicate_fn))
                return "fn", fn_info
            case JuxtPredicate(predicates=predicates, evaluate=evaluate):
                return "juxt", {"predicates": [to_json(p) for p in predicates], "evaluate": to_json(evaluate)}
            case GeLePredicate(lower, upper):
                return "ge_le", {"lower": lower, "upper": upper}
            case GeLtPredicate(lower, upper):
                return "ge_lt", {"lower": lower, "upper": upper}
            case GePredicate(v):
                return "ge", {"v": v}
            case GtLePredicate(lower, upper):
                return "gt_le", {"lower": lower, "upper": upper}
            case GtLtPredicate(lower, upper):
                return "gt_lt", {"lower": lower, "upper": upper}
            case GtPredicate(v):
                return "gt", {"v": v}
            case IsFalsyPredicate():
                return "is_falsy", None
            case IsInstancePredicate(instance_klass):
                return "is_instance", {"klass": [k.__name__ for k in instance_klass]}
            case LePredicate(v):
                return "le", {"v": v}
            case LtPredicate(v):
                return "lt", {"v": v}
            case NamedPredicate(name):
                return "variable", name
            case IsTruthyPredicate():
                return "is_truthy", None
            case NePredicate(v):
                return "ne", {"v": v}
            case NotPredicate(not_predicate):
                return "not", {"predicate": to_json(not_predicate)}
            case OrPredicate(left, right):
                return "or", {"left": to_json(left), "right": to_json(right)}
            case TeePredicate():
                return "tee", None
            case XorPredicate(left, right):
                return "xor", {"left": to_json(left), "right": to_json(right)}
            case _:
                return "unknown", {}

    return dict([to_value(predicate)])
