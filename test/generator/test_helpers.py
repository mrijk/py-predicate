import sys
from datetime import datetime
from typing import Any
from uuid import UUID

import pytest
from more_itertools import first, take

from predicate import (
    all_p,
    always_true_p,
    eq_p,
    ge_le_p,
    ge_p,
    has_length_p,
    in_p,
    is_bool_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_dict_p,
    is_even_p,
    is_float_p,
    is_frozendict_p,
    is_frozenset_p,
    is_hashable_p,
    is_instance_p,
    is_int_p,
    is_list_p,
    is_odd_p,
    is_sentinel_p,
    is_set_p,
    is_str_p,
    is_template_p,
    is_tuple_p,
    is_uuid_p,
)
from predicate.generator.generate_predicate import generate_in_predicates, generate_not_in_predicates
from predicate.generator.helpers import (
    generate_anys,
    generate_even_numbers,
    generate_ints,
    generate_odd_numbers,
    ignore_unknown_kwargs,
    random_anys,
    random_bools,
    random_bytes,
    random_callable_objects,
    random_complex_numbers,
    random_containers,
    random_datetimes,
    random_dicts,
    random_first_from_iterables,
    random_floats,
    random_frames,
    random_frozensets,
    random_functions,
    random_hashables,
    random_ints,
    random_iterables,
    random_lengths,
    random_lists,
    random_named_tuple_instances,
    random_predicates,
    random_sets,
    random_signatures,
    random_strings,
    random_strings_greater,
    random_strings_lower,
    random_tuples,
    random_uuids,
    random_uuids_between,
    random_values_of_type,
    sample_optional_fields,
)


def test_random_anys():
    anys = take(10, random_anys())

    all_any = all_p(is_bool_p | is_datetime_p | is_float_p | is_int_p | is_str_p | is_dict_p)

    assert all_any(anys)


def test_random_bools():
    bools = take(10, random_bools())

    all_bool = all_p(is_bool_p)

    assert bools[0] is False
    assert bools[1] is True
    assert all_bool(bools)


def test_random_complex_numbers():
    complex_numbers = take(10, random_complex_numbers())

    all_complex = all_p(is_complex_p)

    assert all_complex(complex_numbers)


def test_random_containers():
    containers = take(10, random_containers())

    all_container = all_p(is_container_p)

    assert all_container(containers)


def test_random_functions():
    from inspect import signature

    functions = take(10, random_functions())

    assert all(callable(f) and f.__name__ != "<lambda>" for f in functions)
    assert all(0 <= len(signature(f).parameters) <= 5 for f in functions)


def test_random_signatures_have_no_keyword_names():
    import keyword

    # the names come from [a-z]{2,3}, which includes keywords like 'as': inspect.Parameter rejects them
    signatures = take(2000, random_signatures(ge_p(10)))

    assert not any(keyword.iskeyword(name) for sig in signatures for name in sig.parameters)


def test_random_callable_objects():
    from inspect import isfunction, signature

    objects = take(10, random_callable_objects())

    assert all(callable(obj) and not isfunction(obj) for obj in objects)
    assert all(0 <= len(signature(obj).parameters) <= 5 for obj in objects)


def test_random_dicts():
    dicts = take(10, random_dicts())

    all_dict = all_p(is_dict_p)

    assert first(dicts) == {}
    assert all_dict(dicts)


if sys.version_info >= (3, 15):

    def test_random_frozendicts():
        from predicate.generator.helpers import random_frozendicts

        dicts = take(10, random_frozendicts())

        all_frozendicts = all_p(is_frozendict_p)

        assert first(dicts) == frozendict()  # noqa: F821
        assert all_frozendicts(dicts)

    def test_random_sentinels():
        from predicate.generator.helpers import random_sentinels

        sentinels = take(10, random_sentinels())

        assert all_p(is_sentinel_p)(sentinels)


if sys.version_info >= (3, 14):

    def test_random_templates():
        from predicate.generator.helpers import random_templates

        templates = take(10, random_templates())

        assert all_p(is_template_p)(templates)


def test_random_dicts_with_value_p():
    value_p = in_p({"foo", "bar", "foobar"})
    dicts = take(10, random_dicts(value_p=value_p))

    all_dict = all_p(is_dict_p)

    assert first(dicts) == {}
    assert all_dict(dicts)


def test_random_datetimes():
    datetimes = take(10, random_datetimes())

    all_datetime = all_p(is_datetime_p)

    assert all_datetime(datetimes)


def test_random_datetimes_with_limits():
    lower = datetime(year=2025, month=1, day=1)
    upper = datetime(year=2026, month=12, day=31)

    datetimes = take(10, random_datetimes(lower=lower, upper=upper))

    all_datetime = all_p(is_datetime_p)

    assert all_datetime(datetimes)


def test_random_hashables():
    hashables = take(10, random_hashables())

    all_hashable = all_p(is_hashable_p)

    assert all_hashable(hashables)


def test_random_list():
    lists = take(10, random_lists())

    all_lists = all_p(is_list_p)

    assert first(lists) == []
    assert all_lists(lists)


def test_random_list_with_limits():
    length_p = ge_le_p(lower=3, upper=5)
    lists = take(10, random_lists(length_p=length_p))

    all_lists = all_p(is_list_p & has_length_p(length_p))

    assert all_lists(lists)


@pytest.mark.parametrize("value_p", [is_int_p])
def test_random_list_with_value_p(value_p):
    lists = take(10, random_lists(value_p=value_p))

    all_lists = all_p(is_list_p & all_p(value_p))

    assert all_lists(lists)


def test_random_sets():
    sets = take(10, random_sets())

    all_sets = all_p(is_set_p)

    assert first(sets) == set()
    assert all_sets(sets)


def test_random_frozensets():
    sets = take(10, random_frozensets())

    all_frozensets = all_p(is_frozenset_p)

    assert first(sets) == frozenset()
    assert all_frozensets(sets)


def test_random_sets_with_limits():
    length_p = ge_le_p(lower=3, upper=5)
    sets = take(10, random_sets(length_p=length_p))

    all_sets = all_p(is_set_p & has_length_p(length_p=length_p))

    assert all_sets(sets)


@pytest.mark.parametrize("value_p", [ge_p(2)])
def test_random_sets_with_value_p(value_p):
    sets = take(10, random_sets(value_p=value_p))

    all_sets = all_p(is_set_p & all_p(value_p))

    assert all_sets(sets)


def test_random_strings():
    strings = take(10, random_strings())

    all_str = all_p(is_str_p)

    assert all_str(strings)


def test_random_strings_with_limits():
    strings = take(10, random_strings(length_p=ge_le_p(1, 3)))

    all_str = all_p(is_str_p & has_length_p(length_p=ge_le_p(lower=1, upper=3)))

    assert all_str(strings)


def test_random_tuples():
    tuples = take(10, random_tuples())

    all_tuples = all_p(is_tuple_p)

    assert first(tuples) == ()
    assert all_tuples(tuples)


def test_random_tuples_with_limits():
    length_p = ge_le_p(lower=3, upper=5)

    tuples = take(10, random_tuples(length_p=length_p))

    all_tuples = all_p(is_tuple_p & has_length_p(length_p=length_p))

    assert all_tuples(tuples)


@pytest.mark.parametrize("value_p", [ge_p(2)])
def test_random_tuples_with_value_p(value_p):
    tuples = take(10, random_tuples(value_p=value_p))

    all_tuples = all_p(is_tuple_p & all_p(value_p))

    assert all_tuples(tuples)


def test_random_floats():
    floats = take(10, random_floats())

    all_float = all_p(is_float_p)

    assert all_float(floats)


def test_random_floats_with_limits():
    floats = take(10, random_floats(lower=-1.0, upper=1.0))

    all_float = all_p(is_float_p & ge_le_p(lower=-1.0, upper=1.0))

    assert all_float(floats)


def test_random_ints():
    ints = take(10, random_ints())

    all_int = all_p(is_int_p)

    assert all_int(ints)


def test_random_ints_with_limits():
    ints = take(10, random_ints(lower=10, upper=13))

    all_int = all_p(is_int_p & ge_le_p(lower=10, upper=13))

    assert all_int(ints)


def test_random_uuids():
    uuids = take(10, random_uuids())

    all_uuid = all_p(is_uuid_p)

    assert all_uuid(uuids)


def test_even_numbers():
    even_numbers = take(10, generate_even_numbers())

    all_even = all_p(is_even_p)

    assert all_even(even_numbers)


def test_odd_numbers():
    odd_numbers = take(10, generate_odd_numbers())

    all_odd = all_p(is_odd_p)

    assert all_odd(odd_numbers)


@pytest.mark.parametrize("klass", [bool, datetime, int, float, str])
def test_random_values_of_type(klass):
    values = take(10, random_values_of_type(klass))

    all_of_klass = all_p(is_instance_p(klass))

    assert all_of_klass(values)


def test_random_values_of_type_any():
    values = take(10, random_values_of_type(Any))

    all_any = all_p(is_bool_p | is_datetime_p | is_float_p | is_int_p | is_str_p | is_dict_p)

    assert all_any(values)


@pytest.mark.parametrize("generate", [generate_ints, generate_anys])
def test_generate_with_unsatisfiable_predicate_ends(generate):
    # No random value is ever equal to this one, so filtering must give up instead of looping forever
    assert list(generate(eq_p("never generated"))) == []


def test_random_uuids_between():
    lower, upper = UUID(int=100), UUID(int=200)

    assert all(lower <= uuid <= upper for uuid in take(50, random_uuids_between(lower.int, upper.int)))


@pytest.mark.parametrize(("lower", "upper"), [(5, 4), (-1, -1), (2**128, 2**128)])
def test_random_uuids_between_empty_range(lower, upper):
    assert list(random_uuids_between(lower, upper)) == []


def test_random_dicts_with_few_distinct_keys():
    # Only one key exists, so the dicts hold at most that key, instead of waiting for more forever
    dicts = take(20, random_dicts(key_p=eq_p(3)))

    assert all(set(d) <= {3} for d in dicts)


def test_random_values_of_type_uuid():
    assert all(isinstance(value, UUID) for value in take(10, random_values_of_type(UUID)))


def test_random_values_of_type_object():
    # every value is an object, so object accepts what Any does
    assert len(take(10, random_values_of_type(object))) == 10


def test_random_values_of_type_unknown():
    with pytest.raises(ValueError, match="No generator found for <class 'complex'"):
        take(10, random_values_of_type(complex))


def test_random_lengths_empty_once_and_first():
    # #356: exercise with a small n only sees the start of the stream
    lengths = take(50, random_lengths(ge_le_p(lower=0, upper=10)))

    assert lengths[0] == 0
    assert all(0 < length <= 10 for length in lengths[1:])


def test_random_lengths_without_zero():
    assert all(length >= 3 for length in take(20, random_lengths(ge_le_p(lower=3, upper=5))))


def test_random_lengths_only_zero():
    assert take(5, random_lengths(eq_p(0))) == [0, 0, 0, 0, 0]


def test_random_lengths_ignores_non_ints():
    assert all(isinstance(length, int) for length in take(50, random_lengths(always_true_p)))


def test_random_lengths_ignores_bools():
    assert not any(isinstance(length, bool) for length in take(50, random_lengths(always_true_p)))


def test_random_lengths_without_ints():
    assert list(random_lengths(is_str_p)) == []


@pytest.mark.parametrize("generator", [random_lists, random_sets, random_tuples, random_dicts, random_iterables])
def test_random_collections_empty_once_and_first(generator):
    values = take(20, generator())

    assert len(values[0]) == 0
    assert all(values[1:])


def test_random_iterables_doesnt_run_out():
    # Used to yield [], {}, (), "" and stop whenever length 0 was allowed
    assert len(take(20, random_iterables())) == 20


def test_random_first_from_iterables_drops_exhausted():
    values = take(10, random_first_from_iterables(iter([1, 2]), iter([3])))

    assert sorted(values) == [1, 2, 3]


@pytest.mark.parametrize("v", ["", "0", "abc", "Zz", "zzzzzzzzzz", "zzzzzzzzzzzz"])
def test_random_strings_greater(v):
    values = take(100, random_strings_greater(v))

    assert len(values) == 100
    assert all(value > v for value in values)


@pytest.mark.parametrize("v", ["0", "a", "abc", "Zz", "zzzzzzzzzz"])
def test_random_strings_lower(v):
    values = take(100, random_strings_lower(v))

    assert len(values) == 100
    assert all(value < v for value in values)


def test_random_strings_lower_empty():
    assert list(random_strings_lower("")) == []


def test_random_strings_and_bytes_with_empty_length_range():
    assert take(5, random_strings(length_p=ge_le_p(8, 7))) == []
    assert take(5, random_bytes(length_p=ge_le_p(1, 0))) == []


def test_random_in_predicates_are_not_empty():
    # An empty in_p() has no type, so its false values were of any type and broke lt_p(0) & co
    for generator in (generate_in_predicates, generate_not_in_predicates):
        assert all(predicate.v for predicate in take(50, generator(max_depth=3, klass=int)))


def test_random_predicates_of_any_accept_any_value():
    values = [0, "a", None, 1.5, [1], datetime(2020, 1, 1)]
    for predicate in take(200, random_predicates(klass=Any)):
        for value in values:
            assert predicate(value) in (True, False)


def test_random_named_tuple_instances_is_exercisable():
    from more_itertools import consume

    from predicate.spec.exercise_function import exercise_function

    # klass is constrained to named tuple classes, so exercising never passes e.g. object
    consume(exercise_function(random_named_tuple_instances, None, 20))


def test_ignore_unknown_kwargs_is_exercisable():
    from more_itertools import consume

    from predicate.spec.exercise_function import exercise_function

    # the argument is constrained to singledispatch functions, so exercising never passes a plain function
    consume(exercise_function(ignore_unknown_kwargs, None, 20))


def test_sample_optional_fields():
    generators = {"a": iter([1]), "b": iter([]), "c": iter(["x", "y"])}

    samples = [sample_optional_fields(generators) for _ in range(20)]

    assert all(set(sample) <= {"a", "c"} for sample in samples)  # b has no value to give
    assert sample_optional_fields({}) == {}


def test_random_frames():
    from types import FrameType

    frames = take(30, random_frames())

    assert all(isinstance(frame, FrameType) for frame in frames)
    assert len({len(list(_frame_chain(frame))) for frame in frames}) > 1  # frames of different depths


def _frame_chain(frame):
    while frame:
        yield frame
        frame = frame.f_back


def test_generate_true_is_instance_frame():
    from types import FrameType

    from predicate import generate_true, is_instance_p

    assert all(isinstance(frame, FrameType) for frame in take(5, generate_true(is_instance_p(FrameType))))
