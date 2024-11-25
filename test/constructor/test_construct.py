import pytest
from more_itertools import take

from predicate import (
    generate_false,
    generate_true,
    is_int_p,
    is_str_p,
)
from predicate.constructor.construct import construct


@pytest.mark.parametrize(
    "predicate",
    [
        # always_true_p,
        # is_falsy_p,
        # is_bool_p,
        # is_float_p,
        is_int_p,
        is_str_p,
        # is_truthy_p,
        is_int_p | is_str_p,
    ],
)
def test_construct(predicate):
    true_set = take(5, generate_true(predicate))
    false_set = take(5, generate_false(predicate))

    assert true_set

    created = take(6, construct(false_set=false_set, true_set=true_set))

    assert predicate in created
