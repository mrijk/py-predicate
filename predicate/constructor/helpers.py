from typing import Any

from predicate.predicate import Predicate


def predicate_accepts_value(predicate: Predicate, value: Any) -> bool:
    try:
        klass = predicate.klass
    except NotImplementedError:
        return True
    if klass is type(Any):
        return True
    if isinstance(klass, tuple):
        return True
    if isinstance(value, bool) and klass is int:
        return False
    return isinstance(value, klass)


def safe_call_false(predicate: Predicate, value: Any) -> bool:
    # For performance reasons type checking is not part of the predicate itself
    try:
        return predicate(value)
    except TypeError:
        return True


def safe_call_true(predicate: Predicate, value: Any) -> bool:
    # For performance reasons type checking is not part of the predicate itself
    try:
        return predicate_accepts_value(predicate, value) and predicate(value)
    except TypeError:
        return False


def predicate_match(predicate: Predicate, false_set: list, true_set: list) -> dict[str, int]:
    false_misses = sum(safe_call_false(predicate, value) for value in false_set)
    false_matches = len(false_set) - false_misses

    true_matches = sum(safe_call_true(predicate, value) for value in true_set)
    true_misses = len(true_set) - true_matches

    return {
        "false_matches": false_matches,
        "false_misses": false_misses,
        "true_matches": true_matches,
        "true_misses": true_misses,
    }


def sort_by_match(predicates: list[Predicate], false_set: list, true_set: list) -> list[Predicate]:
    def best_match(predicate) -> int:
        match = predicate_match(predicate, false_set=false_set, true_set=true_set)

        return match["false_matches"] + match["true_matches"]

    return sorted(predicates, key=best_match, reverse=True)


def perfect_match(predicate: Predicate, false_set: list, true_set: list) -> bool:
    match = predicate_match(predicate, false_set=false_set, true_set=true_set)
    return match["false_misses"] + match["true_misses"] == 0
