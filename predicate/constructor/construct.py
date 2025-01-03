from typing import Iterator

from more_itertools import first, gray_product, take

from predicate import (
    always_false_p,
    always_true_p,
    is_datetime_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_not_none_p,
    is_set_p,
    is_str_p,
    is_truthy_p,
)
from predicate.constructor.helpers import perfect_match, sort_by_match
from predicate.constructor.mutate import mutations
from predicate.predicate import Predicate
from predicate.standard_predicates import (
    ge_p,
    gt_p,
    is_bool_p,
    is_dict_p,
    is_list_p,
    is_none_p,
    le_p,
    lt_p,
    ne_p,
    zero_p,
)


def construct(false_set: list, true_set: list, attempts: int = 30) -> Predicate | None:
    predicates = initial_predicates()

    while attempts:
        sorted_by_match = sort_by_match(list(predicates), false_set=false_set, true_set=true_set)

        if perfect_match(matched := first(sorted_by_match), false_set=false_set, true_set=true_set):
            return matched

        predicates = create_mutations(take(20, sorted_by_match), false_set=false_set, true_set=true_set)

        attempts -= 1

    return None


def create_mutations(candidates: list[Predicate], false_set: list, true_set: list) -> Iterator[Predicate]:
    for candidate in candidates:
        yield from mutations(candidate, false_set=false_set, true_set=true_set)

    pairs = gray_product(candidates, candidates)
    for pair in pairs:
        left, right = pair
        if left != right:
            yield left | right
            yield left & right
            yield left ^ right


def initial_predicates() -> Iterator[Predicate]:
    # TODO: probably import from __init__
    yield always_false_p
    yield always_true_p
    yield ge_p(0)
    yield gt_p(0)
    yield is_bool_p
    yield is_datetime_p
    yield is_dict_p
    yield is_falsy_p
    yield is_float_p
    yield is_int_p
    yield is_list_p
    yield is_none_p
    yield is_not_none_p
    yield is_set_p
    yield is_str_p
    yield is_truthy_p
    yield le_p(0)
    yield lt_p(0)
    yield ne_p(0)
    yield zero_p
