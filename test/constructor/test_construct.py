import pytest
from more_itertools import take

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    generate_false,
    generate_true,
    is_bool_p,
    is_datetime_p,
    is_dict_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_list_p,
    is_none_p,
    is_not_none_p,
    is_set_p,
    is_str_p,
    is_truthy_p,
    optimize,
)
from predicate.constructor.construct import construct


@pytest.mark.parametrize(
    "predicate",
    [
        always_false_p,
        always_true_p,
        is_falsy_p,
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_truthy_p,
        is_none_p,
        is_not_none_p,
        is_int_p | is_str_p,
        is_int_p | is_float_p,
        is_dict_p,
        is_list_p,
        is_set_p,
        is_int_p & is_str_p,
    ],
)
def test_construct(predicate):
    true_set = take(5, generate_true(predicate))
    false_set = take(5, generate_false(predicate))

    created_predicates = take(6, construct(false_set=false_set, true_set=true_set))

    assert optimize(predicate) in created_predicates

    for created in created_predicates:
        all_true = all_p(created)
        all_false = all_p(~created)

        assert all_false(false_set)
        assert all_true(true_set)
