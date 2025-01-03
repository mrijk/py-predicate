import pytest
from generator.helpers import combinations_of_2
from more_itertools import take

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    eq_p,
    ge_p,
    generate_false,
    generate_true,
    gt_p,
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
    le_p,
    lt_p,
    ne_p,
)
from predicate.constructor.construct import construct


@pytest.mark.parametrize(
    "predicate",
    [
        always_false_p,
        always_true_p,
        eq_p(13),
        is_falsy_p,
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_truthy_p,
        is_none_p,
        is_not_none_p,
        is_dict_p,
        is_list_p,
        is_set_p,
        ne_p(42),
        is_int_p | is_str_p | is_float_p,
        ge_p(13),
        gt_p(13),
        le_p(13),
        lt_p(13),
    ],
)
def test_construct(predicate):
    assert_generated(predicate)


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_construct_or(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 | predicate_2

    assert_generated(predicate)


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_construct_and(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 & predicate_2

    assert_generated(predicate)


@pytest.mark.skip(reason="Fix me!")
@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_construct_xor(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 ^ predicate_2

    assert_generated(predicate)


def assert_generated(predicate):
    nr_of_samples = 10
    true_set = take(nr_of_samples, generate_true(predicate))
    false_set = take(nr_of_samples, generate_false(predicate))

    matched = construct(false_set=false_set, true_set=true_set)

    assert matched

    all_false = all_p(~matched)
    all_true = all_p(matched)

    assert all_false(false_set)
    assert all_true(true_set)
