from typing import Any

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.fn_predicate import FnPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
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
            case FnPredicate(predicate_fn):
                name = predicate_fn.__code__.co_name
                return "fn", {"name": name}
            case IsFalsyPredicate():
                return "is_falsy", None
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
