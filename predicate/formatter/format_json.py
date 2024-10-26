from typing import Any

from predicate import AlwaysFalsePredicate, AlwaysTruePredicate, AndPredicate
from predicate.predicate import Predicate, OrPredicate, XorPredicate, NotPredicate


def to_json(predicate: Predicate) -> dict[str, Any]:
    def to_value(predicate) -> tuple[str, Any]:
        match predicate:
            case AlwaysFalsePredicate():
                return "false", False
            case AlwaysTruePredicate():
                return "true", True
            case AndPredicate(left, right):
                return "and", {"left": to_json(left), "right": to_json(right)}
            case NotPredicate(predicate):
                return "not", {"predicate": to_json(predicate)}
            case OrPredicate(left, right):
                return "or", {"left": to_json(left), "right": to_json(right)}
            case XorPredicate(left, right):
                return "xor", {"left": to_json(left), "right": to_json(right)}

    return dict([to_value(predicate)])
