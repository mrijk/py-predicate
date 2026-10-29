import collections.abc
import inspect
import sys
import typing
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta
from ipaddress import IPv4Network

import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
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
    generate_true,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    in_p,
    is_bool_p,
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
    is_instance_p,
    is_int_p,
    is_iterable_of_p,
    is_iterable_p,
    is_list_of_p,
    is_list_p,
    is_module_p,
    is_nan_p,
    is_none_p,
    is_normal_p,
    is_not_empty_p,
    is_not_none_p,
    is_number_p,
    is_odd_p,
    is_p,
    is_predicate_of_p,
    is_predicate_p,
    is_regex_p,
    is_sentinel_p,
    is_set_of_p,
    is_set_p,
    is_str_p,
    is_subnormal_p,
    is_template_p,
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
    regex_p,
    tee_p,
    zero_p,
)
from predicate.and_predicate import AndPredicate
from predicate.in_predicate import InPredicate
from predicate.not_predicate import NotPredicate
from predicate.predicate import Predicate
from predicate.set_predicates import intersects_p, is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p
from predicate.tee_predicate import TeePredicate


def foo(self) -> bool:
    return True


@pytest.mark.parametrize(
    "predicate",
    [
        any_p(is_uuid_p),
        any_p(is_tuple_of_p(is_uuid_p, in_p({"foo", "bar"}), is_truthy_p)),
        eq_false_p,
        eq_true_p,
        has_key_p(eq_p("foo")),
        is_bool_p,
        is_callable_p,
        is_complex_p,
        is_container_p,
        is_datetime_p,
        is_dict_p,
        is_falsy_p,
        is_empty_p,
        is_even_p,
        is_float_p,
        is_hashable_p,
        is_inf_p,
        is_iterable_p,
        is_list_p,
        is_nan_p,
        is_none_p,
        is_number_p,
        is_not_empty_p,
        is_not_none_p,
        is_odd_p,
        is_regex_p,
        is_truthy_p,
        is_int_p,
        is_predicate_p,
        is_frozenset_p,
        is_set_p,
        is_str_p,
        is_tuple_p,
        ~is_int_p,
        is_int_p ^ is_str_p,
        is_uuid_p,
        ne_p(2),
        not_in_p([2, "foo", uuid.uuid4()]),
        regex_p("^foo"),
        neg_p,
        pos_p,
        # property_p(cast(Callable, property(fget=foo))),
        zero_p,
        intersects_p({1, 2, 3}),
        is_real_subset_p({1, 2, 3}),
        is_real_superset_p({1, 2, 3}),
        is_subset_p({1, 2, 3}),
        is_superset_p({1, 2, 3}),
    ],
)
def test_generate_true(predicate):
    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "predicate",
    [
        is_module_p,
        is_normal_p,
        is_subnormal_p,
        pytest.param(
            is_template_p, marks=pytest.mark.skipif(sys.version_info < (3, 14), reason="requires Python 3.14+")
        ),
        pytest.param(
            is_frozendict_p, marks=pytest.mark.skipif(sys.version_info < (3, 15), reason="requires Python 3.15+")
        ),
        pytest.param(
            is_sentinel_p, marks=pytest.mark.skipif(sys.version_info < (3, 15), reason="requires Python 3.15+")
        ),
    ],
)
def test_generate_true_new_python_types(predicate):
    assert_generated_true(predicate)


@pytest.mark.parametrize("predicate_pair", combinations_of_2())
def test_generate_true_or(predicate_pair):
    predicate_1, predicate_2 = predicate_pair
    predicate = predicate_1 | predicate_2
    assert_generated_true(predicate)


def test_generate_tee():
    predicate = tee_p(fn=lambda x: x) & eq_p(2)

    assert_generated_true(predicate)


@pytest.mark.parametrize("all_predicate", [ge_p(2), is_str_p, is_list_p])
def test_generate_all(all_predicate):
    predicate = all_p(all_predicate)

    assert_generated_true(predicate)


@pytest.mark.parametrize("value", [2, "foo", "3.14", "complex(1, 2)"])
def test_generate_eq(value):
    predicate = eq_p(value)

    assert_generated_true(predicate)


@pytest.mark.parametrize("value", [True])
def test_generate_is(value):
    predicate = is_p(value)

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_ge_le(lower, upper):
    predicate = ge_le_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_ge_lt(lower, upper):
    predicate = ge_lt_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_gt_le(lower, upper):
    predicate = gt_le_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "lower, upper",
    [
        (2, 5),
        # ("bar", "foo"),
        (3.14, 42.1),
        (datetime.now(), datetime.now() + timedelta(days=1)),
        # uuid.uuid4(),
    ],
)
def test_generate_gt_lt(lower, upper):
    predicate = gt_lt_p(lower, upper)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "key_value_predicates",
    [
        ([(is_str_p, is_int_p)]),
    ],
)
def test_dict_of(key_value_predicates):
    predicate = is_dict_of_p(*key_value_predicates)

    assert_generated_true(predicate)


@pytest.mark.skipif(sys.version_info < (3, 15), reason="frozendict requires Python 3.15+")
def test_frozendict_of():
    predicate = is_frozendict_of_p((is_str_p, is_int_p))

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "iterable_of_p",
    [
        is_int_p,
    ],
)
def test_iterable_of(iterable_of_p):
    predicate = is_iterable_of_p(iterable_of_p)

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


@pytest.mark.parametrize("klass", [bool, float, int, str])
def test_predicate_of(klass):
    predicate = is_predicate_of_p(klass)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "tuple_types_p",
    [
        (is_bool_p,),
        (is_int_p,),
        (is_str_p,),
        (is_int_p, is_int_p),
        (is_uuid_p, in_p({"foo", "bar"}), is_truthy_p),
    ],
)
def test_tuple_of(tuple_types_p):
    predicate = is_tuple_of_p(*tuple_types_p)

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


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

    assert_generated_true(predicate)


def test_generate_always_false_p():
    predicate = always_false_p

    assert not list(generate_true(predicate))


def test_generate_xor_always_false():
    predicate = always_true_p ^ always_true_p

    assert not list(generate_true(predicate))


def test_generate_always_true_p():
    predicate = always_true_p

    assert_generated_true(predicate)


def test_generate_fn_p():
    def generate_true_fn():
        yield from [1, 3]

    predicate = fn_p(lambda x: x % 2, generate_true_fn=generate_true_fn)

    assert_generated_true(predicate)


def test_generate_fn_with_missing_generate():
    predicate = fn_p(lambda x: x % 2)

    with pytest.raises(ValueError):
        take(5, generate_true(predicate))


def test_generate_true_unknown(unknown_p):
    with pytest.raises(ValueError):
        take(5, generate_true(unknown_p))


@pytest.mark.parametrize(
    "compare_predicate",
    [
        ge_p,
        gt_p,
        le_p,
        lt_p,
    ],
)
def test_generate_true_unknown_compare(compare_predicate):
    predicate = compare_predicate(v=None)
    with pytest.raises(ValueError):
        take(5, generate_true(predicate))


@pytest.mark.parametrize(
    "range_predicate",
    [
        ge_le_p,
        ge_lt_p,
        gt_le_p,
        gt_lt_p,
    ],
)
def test_generate_true_unknown_range(range_predicate):
    predicate = range_predicate(lower="bar", upper="foo")
    with pytest.raises(ValueError):
        take(5, generate_true(predicate))


@pytest.mark.parametrize(
    "klass",
    [
        Predicate[int],
        typing.Callable,
        typing.Callable[[int], int],
        collections.abc.Callable[[int], int],
        typing.Iterable,
        collections.abc.Iterable[int],
        inspect.Signature,
        type,
    ],
)
def test_generate_true_is_instance_generic(klass):
    assert_generated_true(is_instance_p(klass))


def test_generate_true_is_instance_type_of():
    values = take(5, generate_true(is_instance_p(type[Exception])))
    assert all(issubclass(value, Exception) for value in values)


def test_generate_true_is_instance_unknown():
    predicate = is_instance_p(IPv4Network)
    with pytest.raises(ValueError, match="No generator found"):
        take(5, generate_true(predicate))


@pytest.mark.parametrize("predicate_class", [AndPredicate, InPredicate, NotPredicate])
def test_generate_true_is_instance_predicate_subclass(predicate_class):
    values = take(5, generate_true(is_instance_p(predicate_class)))
    assert values
    assert all(isinstance(value, predicate_class) for value in values)


def test_generate_true_is_instance_predicate_subclass_unknown():
    with pytest.raises(ValueError, match="No generator found for <class 'predicate.tee_predicate.TeePredicate'>"):
        take(5, generate_true(is_instance_p(TeePredicate)))


class Point:
    def __init__(self, x: int, y: int = 0, *, label: str | None = None):
        self.x, self.y, self.label = x, y, label


@dataclass
class Segment:
    start: Point
    end: Point


class Plain:
    pass


class Unannotated:
    def __init__(self, x):
        self.x = x


class AlwaysRaises:
    def __init__(self, x: int):
        raise ValueError("never")


class Shape(ABC):
    def __init__(self, size: int):
        self.size = size

    @abstractmethod
    def area(self) -> float: ...


class Shape2D(Shape, ABC):
    pass


class Square(Shape2D):
    def area(self) -> float:
        return self.size**2


class Broken(ABC):
    @abstractmethod
    def run(self) -> None: ...


class AlwaysBroken(Broken):
    def __init__(self, x: int):
        raise ValueError("broken")

    def run(self) -> None: ...


class NoSubclasses(ABC):
    @abstractmethod
    def run(self) -> None: ...


def test_generate_true_constructed_from_init():
    values = take(10, generate_true(is_instance_p(Point)))
    assert len(values) == 10
    assert all(isinstance(value, Point) and isinstance(value.x, int) for value in values)


def test_generate_true_constructed_without_init():
    assert all(isinstance(value, Plain) for value in take(3, generate_true(is_instance_p(Plain))))


def test_generate_true_constructed_dataclass_with_class_fields():
    values = take(5, generate_true(is_instance_p(Segment)))
    assert all(isinstance(value.start, Point) and isinstance(value.end, Point) for value in values)


def test_generate_true_constructed_abstract_class_uses_subclass():
    values = take(5, generate_true(is_instance_p(Shape)))
    assert all(isinstance(value, Square) for value in values)


def test_generate_true_constructed_abstract_subclasses_keep_raising():
    with pytest.raises(ValueError, match=r"its subclasses keep raising \(ValueError: broken\)"):
        take(1, generate_true(is_instance_p(Broken)))


@pytest.mark.parametrize("klass", [Unannotated, NoSubclasses])
def test_generate_true_constructed_not_possible(klass):
    with pytest.raises(ValueError, match="No generator found"):
        take(1, generate_true(is_instance_p(klass)))


def test_generate_true_constructed_constructor_keeps_raising():
    with pytest.raises(ValueError, match=r"constructor keeps raising \(ValueError: never\)"):
        take(1, generate_true(is_instance_p(AlwaysRaises)))


@pytest.mark.parametrize(
    "length_p",
    [
        eq_p(2),
        ge_le_p(lower=1, upper=3),
    ],
)
def test_generate_has_length_p(length_p):
    predicate = has_length_p(length_p=length_p)

    assert_generated_true(predicate)


@pytest.mark.parametrize(
    "length_p, value_p",
    [
        (eq_p(2), is_int_p),
        (ge_le_p(lower=1, upper=3), is_str_p),
    ],
)
def test_generate_has_length_p_with_klass(length_p, value_p):
    predicate = has_length_p(length_p=length_p)
    values_p = all_p(value_p)

    values = take(5, generate_true(predicate, value_p=value_p))
    assert values

    for value in values:
        assert predicate(value)
        assert values_p(value)


def test_generate_true_ignores_unknown_kwargs():
    assert all(isinstance(value, str) for value in take(5, generate_true(is_str_p, length_p=ge_p(1))))
    assert take(3, generate_true(eq_p(2), length_p=ge_p(1))) == [2, 2, 2]
