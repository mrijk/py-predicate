from datetime import datetime

import pytest
from constructor.helpers import assert_generated, assert_generated_exact
from generator.helpers import combinations_of_2

from predicate import (
    always_false_p,
    always_true_p,
    eq_p,
    ge_p,
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
    (
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
        is_dict_p,
        is_list_p,
        is_set_p,
    ),
)
def test_construct_exact(predicate):
    assert_generated_exact(predicate)


@pytest.mark.parametrize(
    "predicate",
    (
        ge_p(13),
        gt_p(13),
        le_p(13),
        lt_p(13),
        is_int_p | is_str_p | is_float_p,
    ),
)
def test_construct(predicate):
    assert_generated(predicate)


@pytest.mark.parametrize("value", (42, 3.14, "foo", False, True, datetime.now()))
def test_construct_eq(value):
    predicate = eq_p(value)
    assert_generated_exact(predicate)


@pytest.mark.parametrize("value", [42, True])
def test_construct_ge(value):
    predicate = ge_p(value)
    assert_generated(predicate)


@pytest.mark.parametrize("value", [42, 3.14, "foo", True, datetime.now()])
def test_construct_ne(value):
    predicate = ne_p(value)
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


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_construct_xor(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 ^ predicate_2

    assert_generated(predicate)


def test_create_mutations_skips_incompatible_klasses():
    from predicate.constructor.construct import create_mutations

    candidates = [ge_p(2), eq_p("foo")]
    results = list(create_mutations(candidates, false_set=[1, "bar"], true_set=[3, "foo"]))

    assert ge_p(2) & eq_p("foo") not in results
    assert ge_p(2) ^ eq_p("foo") not in results


def test_construct_not_possible():
    false_set = [0]
    true_set = [0]

    matched = construct(false_set=false_set, true_set=true_set)

    assert matched is None
