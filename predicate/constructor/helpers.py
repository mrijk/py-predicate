from predicate.predicate import Predicate


def predicate_match(predicate: Predicate, false_set: list, true_set: list) -> dict[str, int]:
    false_misses = sum(predicate(value) for value in false_set)
    false_matches = len(false_set) - false_misses

    true_matches = sum(predicate(value) for value in true_set)
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
