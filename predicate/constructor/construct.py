from typing import Iterator

from more_itertools import gray_product

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
from predicate.predicate import Predicate
from predicate.standard_predicates import all_p, is_bool_p, is_dict_p, is_list_p, is_none_p

# TODO: this is very much work under construction (pun intended) and not ready for public consumption


def construct(false_set: list, true_set: list) -> Iterator[Predicate]:
    predicates = list(initial_predicates())

    while True:
        for predicate in predicates:
            all_true = all_p(predicate)
            all_false = all_p(~predicate)
            if all_true(true_set) and all_false(false_set):
                yield predicate

        predicates = list(create_mutations(predicates))


def create_mutations(candidates: list[Predicate]) -> Iterator[Predicate]:
    pairs = gray_product(candidates, candidates)
    for pair in pairs:
        left, right = pair
        if left != right:
            yield left | right
            yield left & right


def initial_predicates() -> Iterator[Predicate]:
    # TODO: probably import from __init__
    yield always_false_p
    yield always_true_p
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
