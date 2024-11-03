from typing import Any

from predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    FnPredicate,
    NePredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)


def to_json(predicate: Predicate) -> dict[str, Any]:
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
            case NePredicate(v):
                return "ne", {"v": v}
            case NotPredicate(not_predicate):
                return "not", {"predicate": to_json(not_predicate)}
            case OrPredicate(left, right):
                return "or", {"left": to_json(left), "right": to_json(right)}
            case XorPredicate(left, right):
                return "xor", {"left": to_json(left), "right": to_json(right)}
            case _:
                return "unknown", {}

    return dict([to_value(predicate)])
