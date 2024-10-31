from typing import Any

from predicate import AlwaysFalsePredicate, AlwaysTruePredicate, AndPredicate
from predicate.predicate import NePredicate, NotPredicate, OrPredicate, Predicate, XorPredicate


def to_json(predicate: Predicate) -> dict[str, Any]:
    def to_value(predicate) -> tuple[str, Any]:
        match predicate:
            case AlwaysFalsePredicate():
                return "false", False
            case AlwaysTruePredicate():
                return "true", True
            case AndPredicate(left, right):
                return "and", {"left": to_json(left), "right": to_json(right)}
            case NePredicate(v):
                return "ne", {"v": v}
            case NotPredicate(not_predicate):
                return "not", {"predicate": to_json(not_predicate)}
            case OrPredicate(left, right):
                return "or", {"left": to_json(left), "right": to_json(right)}
            case XorPredicate(left, right):
                return "xor", {"left": to_json(left), "right": to_json(right)}
        return "unknown", {}

    return dict([to_value(predicate)])
