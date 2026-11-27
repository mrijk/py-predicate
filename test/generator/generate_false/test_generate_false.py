import uuid
from datetime import datetime, timedelta

import pytest
from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from generator.helpers import combinations_of_2
from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    generate_false,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    in_p,
    intersects_p,
    is_bool_p,
    is_bytes_p,
    is_callable_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_dict_of_p,
    is_dict_p,
    is_empty_p,
    is_even_p,
    is_falsy_p,
    is_float_p,
    is_frozendict_of_p,
    is_frozendict_p,
    is_frozenset_of_p,
    is_frozenset_p,
    is_hashable_p,
    is_inf_p,
    is_int_p,
    is_iterable_of_p,
    is_iterable_p,
    is_list_of_p,
    is_list_p,
    is_mapping_p,
    is_module_p,
    is_nan_p,
    is_none_p,
    is_normal_p,
    is_not_empty_p,
    is_not_none_p,
    is_number_p,
    is_odd_p,
    is_p,
    is_predicate_p,
    is_real_subset_p,
    is_real_superset_p,
    is_regex_p,
    is_sentinel_p,
    is_sequence_p,
    is_set_of_p,
    is_set_p,
    is_str_p,
    is_subnormal_p,
    is_subset_p,
    is_superset_p,
    is_template_p,
    is_timedelta_p,
    is_truthy_p,
    is_tuple_of_p,
    is_tuple_p,
    is_uuid_p,
    le_p,
    lt_p,
    ne_p,
    neg_p,
    not_in_p,
    pos_p,
    tee_p,
    zero_p,
)
from predicate.is_callable_predicate import is_callable_p as is_callable_signature_p


@pytest.mark.parametrize(
    "predicate",
    [
        all_p(is_int_p),
        any_p(is_uuid_p),
        eq_false_p,
        eq_true_p,
        has_key_p(eq_p("foo")),
        has_key_p(le_p(5)),  # keys of the type key_p is about, not str keys: le_p(5) raises for those
        has_key_p(ge_le_p(0, 10) | eq_p(20)),
        has_key_p(always_true_p),
        has_key_p(ne_p(3)),  # the only dicts without a key != 3 hold the key 3
        in_p([2, 3, 4]),
        is_bool_p,
        is_bytes_p,
        is_callable_p,
        is_complex_p,
        is_container_p,
        is_datetime_p,
        is_dict_p,
        is_empty_p,
        is_even_p,
        is_falsy_p,
        is_float_p,
        is_frozenset_p,
        is_hashable_p,
        is_inf_p,
        is_iterable_p,
        is_list_p,
        is_mapping_p,
        is_nan_p,
        is_none_p,
        is_not_empty_p,
        is_not_none_p,
        is_number_p,
        is_odd_p,
        is_predicate_p,
        is_regex_p,
        is_sequence_p,
        is_truthy_p,
        is_int_p,
        is_set_p,
        is_str_p,
        is_timedelta_p,
        is_tuple_p,
        is_uuid_p,
        ne_p(2),
        not_in_p([2, "foo", 4]),
        ne_p(2) & ne_p(3),
        ~is_int_p,
        neg_p,
        pos_p,
        zero_p,
        intersects_p({1, 2, 3}),
        is_real_subset_p({1, 2, 3}),
        is_real_superset_p({1, 2, 3}),
        is_subset_p({1, 2, 3}),
        is_superset_p({1, 2, 3}),
    ],
)
def test_generate_false(predicate):
    assert_generated_false(predicate)


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_generate_false_and(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 & predicate_2
    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "predicate",
    [
        is_module_p,
        is_normal_p,
        is_subnormal_p,
        is_template_p,
        is_frozendict_p,
        is_sentinel_p,
    ],
)
def test_generate_false_new_python_types(predicate):
    assert_generated_false(predicate)


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_generate_false_or(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 | predicate_2
    assert_generated_false(predicate)


def test_generate_tee():
    predicate = tee_p(fn=lambda x: x) & eq_p(2)

    assert_generated_false(predicate)


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_generate_false_xor(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 ^ predicate_2
    assert_generated_false(predicate)


def test_generate_false_or_with_3():
    predicate = is_int_p | is_str_p | is_float_p

    assert_generated_false(predicate)


@pytest.mark.parametrize("value", [2, "foo", "3.14", "complex(1, 2)"])
def test_generate_eq(value):
    predicate = eq_p(value)

    assert_generated_false(predicate)


@pytest.mark.parametrize("value", [True])
def test_generate_is(value):
    predicate = is_p(value)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_ge(value):
    predicate = ge_p(value)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_gt(value):
    predicate = gt_p(value)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_le(value):
    predicate = le_p(value)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_lt(value):
    predicate = lt_p(value)

    assert_generated_false(predicate)


now = datetime.now()


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (now, now + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_ge_le(lower, upper):
    predicate = ge_le_p(lower, upper)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (now, now + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_ge_lt(lower, upper):
    predicate = ge_lt_p(lower, upper)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (now, now + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_gt_le(lower, upper):
    predicate = gt_le_p(lower, upper)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (now, now + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_gt_lt(lower, upper):
    predicate = gt_lt_p(lower, upper)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "key_value_predicates",
    [
        ([(is_str_p, is_int_p), (is_str_p, is_int_p)]),
        ([(is_str_p, is_int_p), (is_str_p, is_bool_p)]),
    ],
)
def test_dict_of(key_value_predicates):
    predicate = is_dict_of_p(*key_value_predicates)

    assert_generated_false(predicate)


def test_dict_of_without_key_value_predicates():
    # nothing satisfies it, so any dict is false
    assert_generated_false(is_dict_of_p())
    assert_generated_false(is_frozendict_of_p())


def test_frozendict_of():
    predicate = is_frozendict_of_p((is_str_p, is_int_p))

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "iterable_of_p",
    [
        is_int_p,
    ],
)
def test_iterable_of(iterable_of_p):
    predicate = is_iterable_of_p(iterable_of_p)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "list_type_p",
    [
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_int_p | is_str_p,
        is_bool_p | is_datetime_p | is_str_p,
    ],
)
def test_list_of(list_type_p):
    predicate = is_list_of_p(list_type_p)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "tuple_types_p",
    [
        (),
        (is_bool_p,),
        (is_int_p,),
        (is_str_p,),
        (is_int_p, is_int_p),
        (is_int_p, is_str_p, is_float_p),
    ],
)
def test_tuple_of(tuple_types_p):
    predicate = is_tuple_of_p(*tuple_types_p)

    assert_generated_false(predicate)


def test_generate_always_false_p():
    predicate = always_false_p

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "predicate",
    [
        always_true_p,
        always_true_p & always_true_p,
    ],
)
def test_generate_always_true_p(predicate):
    assert not list(generate_false(predicate))


@pytest.mark.parametrize(
    "set_type_p",
    [
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_int_p | is_str_p,
        is_bool_p | is_datetime_p | is_str_p,
    ],
)
def test_set_of(set_type_p):
    predicate = is_set_of_p(set_type_p)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "set_type_p",
    [
        is_bool_p,
        is_datetime_p,
        is_float_p,
        is_int_p,
        is_str_p,
        is_int_p | is_str_p,
        is_bool_p | is_datetime_p | is_str_p,
    ],
)
def test_frozenset_of(set_type_p):
    predicate = is_frozenset_of_p(set_type_p)

    assert_generated_false(predicate)


def test_generate_fn_p():
    def generate_false_fn():
        yield from [2, 4]

    predicate = fn_p(lambda x: x % 2, generate_false_fn=generate_false_fn)

    assert_generated_false(predicate)


def test_generate_false_unknown(unknown_p):
    with pytest.raises(ValueError):
        take(5, generate_false(unknown_p))


@pytest.mark.parametrize(
    "compare_predicate",
    [
        ge_p,
        gt_p,
        le_p,
        lt_p,
    ],
)
def test_generate_false_unknown_compare(compare_predicate):
    predicate = compare_predicate(v=None)
    with pytest.raises(ValueError):
        take(5, generate_false(predicate))


@pytest.mark.parametrize(
    "range_predicate",
    [
        ge_le_p,
        ge_lt_p,
        gt_le_p,
        gt_lt_p,
    ],
)
def test_generate_false_unknown_range(range_predicate):
    predicate = range_predicate(lower="bar", upper="foo")
    with pytest.raises(ValueError):
        take(5, generate_false(predicate))


def test_generate_false_xor_always_true():
    # XOR that optimizes to always_true_p — generate_false yields nothing
    predicate = is_int_p ^ ~is_int_p

    values = list(take(5, generate_false(predicate)))
    assert values == []


def test_generate_false_or_always_true():
    predicate = eq_p(False) | ~eq_p(False)

    assert list(take(5, generate_false(predicate))) == []


def test_generate_false_xor_without_values():
    # x < 0 xor x >= 0 is always true, but the optimizer doesn't see it: searching for a false value must end
    always_true = lt_p(0) ^ ~(ne_p(0) ^ gt_p(0))

    assert list(take(5, generate_false(always_true))) == []
    # not_in_p([0]) is the only side that can be false, and it is false at 0
    assert set(take(5, generate_false(not_in_p([0]) & always_true))) == {0}


def test_generate_false_xor_overlapping():
    # XOR where AND doesn't optimize to always_false_p — covers the left_and_right path
    predicate = ge_p(2) ^ gt_p(5)

    assert_generated_false(predicate)


def test_generate_false_is_callable_signature():
    predicate = is_callable_signature_p(params=[int], return_type=str)

    assert_generated_false(predicate)


def test_generate_false_ignores_unknown_kwargs():
    assert all(value != 2 for value in take(5, generate_false(eq_p(2), length_p=ge_p(1))))


def test_generate_false_has_length_when_every_length_is_valid():
    assert take(3, generate_false(has_length_p(ge_p(0)))) == []


def test_exactly_n_false_ends_when_the_rest_has_no_false_values():
    from predicate.exactly_predicate import exactly_n
    from predicate.match_predicate import match_p

    # always_true_p has no false values: the stream ends instead of raising (PEP 479)
    assert list(generate_false(match_p(exactly_n(1, eq_p(1)), always_true_p))) == []


def test_match_false_ends_when_the_rest_has_no_false_values():
    from predicate.match_predicate import match_p

    assert list(generate_false(match_p(eq_p(1), always_true_p))) == []


def test_match_false_with_an_empty_pattern():
    from predicate.match_predicate import match_p

    # an empty pattern matches everything, so there is nothing false; unless the whole iterable must match
    assert list(generate_false(match_p())) == []
    assert all(not match_p(full_match=True)(value) for value in take(10, generate_false(match_p(full_match=True))))
    assert take(10, generate_false(match_p(full_match=True)))


def test_set_of_false_ends_when_no_element_can_be_false():
    from predicate import is_frozenset_of_p, is_set_of_p

    # always_true_p has no false values, so no set has an element failing it: the stream ends instead of hanging
    assert list(generate_false(is_set_of_p(always_true_p))) == []
    assert list(generate_false(is_frozenset_of_p(always_true_p))) == []
    assert list(generate_false(is_frozenset_of_p(ge_p(0) | lt_p(0)))) == []


def test_set_of_false_with_a_length_that_is_never_true_or_not_an_int():
    from predicate import fn_p, in_p, is_none_p, is_set_of_p
    from predicate.generator.helpers import random_ints

    # the optimizer can't tell that no length is both in (1, 2) and above 5
    never = in_p([1, 2]) & fn_p(lambda x: x > 5, generate_true_fn=lambda: random_ints(lower=6))
    for length_p in (never, is_none_p):
        values = take(5, generate_false(is_set_of_p(ge_p(0)), length_p=length_p))
        assert values
        assert all(not is_set_of_p(ge_p(0))(value) for value in values)


def test_filtering_false_generators_end_when_no_value_is_false():
    from predicate import comp_p, intersects_p, is_superset_p, juxt_p

    # every set is a superset of the empty set, every comp here is true, and the juxt is always true
    assert list(generate_false(is_superset_p(set()))) == []
    assert list(generate_false(juxt_p(eq_p(1), evaluate=always_true_p))) == []
    assert list(generate_false(comp_p(lambda x: 1, eq_p(1)))) == []
    # a set that has an element in common with every random set
    assert set() in list(generate_false(intersects_p(set(range(-1000, 1000)))))


def test_generate_is_instance_is_exercisable():
    from more_itertools import consume

    from predicate.generator.generate_false import generate_is_instance_p
    from predicate.spec.exercise_function import exercise_function

    # the classes are annotated as types, so exercising never draws a non-type such as 5 for isinstance
    consume(exercise_function(generate_is_instance_p, None, 30))


def test_struct_false_ends_extra_key_values_when_a_required_field_is_never_true():
    from predicate.struct_predicate import StructPredicate

    predicate = StructPredicate(required={"a": always_false_p}, optional={})
    # no dict has a valid "a" to be extended with an extra key: those dicts end instead of raising (PEP 479)
    values = take(10, generate_false(predicate))
    assert values
    assert all(not predicate(value) for value in values)
