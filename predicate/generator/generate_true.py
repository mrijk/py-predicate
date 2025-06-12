import random
import sys
from collections.abc import Callable, Container, Iterable, Iterator
from datetime import datetime, timedelta
from functools import singledispatch
from itertools import repeat
from typing import Any, Final
from uuid import UUID

import exrex  # type: ignore
from more_itertools import (
    chunked,
    flatten,
    powerset_of_sets,
    random_combination_with_replacement,
    random_permutation,
    take,
)

from predicate import generate_false
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.fn_predicate import FnPredicate
from predicate.ge_predicate import GePredicate
from predicate.generator.helpers import (
    default_length_p,
    generate_anys,
    generate_ints,
    generate_strings,
    generate_uuids,
    random_anys,
    random_bools,
    random_callables,
    random_complex_numbers,
    random_containers,
    random_datetimes,
    random_dicts,
    random_first_from_iterables,
    random_floats,
    random_ints,
    random_iterables,
    random_lambdas,
    random_lists,
    random_predicates,
    random_sets,
    random_strings,
    random_tuples,
    random_uuids,
    random_values_of_type,
    set_from_list,
)
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.has_path_predicate import HasPathPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_lambda_predicate import IsLambdaPredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_predicate_of_p import IsPredicateOfPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.property_predicate import PropertyPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.regex_predicate import RegexPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import InPredicate, IsRealSubsetPredicate, IsSubsetPredicate, NotInPredicate
from predicate.standard_predicates import (
    AllPredicate,
    eq_p,
    ge_le_p,
    ge_p,
    is_dict_of_p,
    is_int_p,
    is_list_of_p,
    is_list_p,
)
from predicate.tee_predicate import TeePredicate
from predicate.tuple_of_predicate import TupleOfPredicate


@singledispatch
def generate_true[T](predicate: Predicate[T], **_kwargs) -> Iterator[T]:
    """Generate values that satisfy this predicate."""
    raise ValueError(f"Please register generator for correct predicate type: {predicate}")


@generate_true.register
def generate_all_p(all_predicate: AllPredicate, *, length_p: Predicate = default_length_p) -> Iterator:
    if length_p(0):
        yield []

    predicate = all_predicate.predicate

    valid_max_lengths = generate_true(length_p)

    while True:
        max_length = next(valid_max_lengths)

        values = take(max_length, generate_true(predicate))
        yield random_combination_with_replacement(values, max_length)

        values = take(max_length, generate_true(predicate))
        yield set(random_combination_with_replacement(values, max_length))

        values = take(max_length, generate_true(predicate))
        yield list(random_combination_with_replacement(values, max_length))


default_any_length_p: Final = ge_le_p(lower=1, upper=10)


@generate_true.register
def generate_any_p(any_predicate: AnyPredicate, *, length_p: Predicate = default_any_length_p) -> Iterator:
    predicate = any_predicate.predicate

    valid_lengths = generate_true(length_p)

    while True:
        length = next(valid_lengths)

        nr_true_values = random.randint(1, length) if length > 1 else 1
        nr_false_values = length - nr_true_values

        false_values = take(nr_false_values, generate_false(predicate))
        true_values = take(nr_true_values, generate_true(predicate))

        combined_values = false_values + true_values

        yield random_permutation(combined_values)
        yield from set_from_list(combined_values)


@generate_true.register
def generate_always_true(_predicate: AlwaysTruePredicate, **_kwargs) -> Iterator:
    yield from random_anys()


@generate_true.register
def generate_and(predicate: AndPredicate) -> Iterator:
    if optimize(predicate) == always_false_p:
        yield from []
    else:
        attempts = 100
        try_left = (item for item in take(attempts, generate_true(predicate.left)) if predicate.right(item))
        try_right = (item for item in take(attempts, generate_true(predicate.right)) if predicate.left(item))

        range_1 = (item for item in generate_true(predicate.left) if predicate.right(item)) if try_left else ()
        range_2 = (item for item in generate_true(predicate.right) if predicate.left(item)) if try_right else ()

        if range_1 or range_2:
            yield from random_first_from_iterables(range_1, range_2)

        raise ValueError(f"Couldn't generate values that statisfy {predicate}")


@generate_true.register
def generate_eq(predicate: EqPredicate, **_kwargs) -> Iterator:
    yield from repeat(predicate.v)


@generate_true.register
def generate_always_false(_predicate: AlwaysFalsePredicate) -> Iterator:
    yield from []


@generate_true.register
def generate_ge_le(predicate: GeLePredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from random_datetimes(lower=lower, upper=upper)
        case int(), _:
            yield from random_ints(lower=lower, upper=upper)
        case float(), _:
            yield from random_floats(lower=lower, upper=upper)
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_true.register
def generate_ge_lt(predicate: GeLtPredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from random_datetimes(lower=lower, upper=upper - timedelta(seconds=1))
        case int(), _:
            yield from random_ints(lower=lower, upper=upper - 1)
        case float(), _:
            yield from random_floats(lower=lower, upper=upper - 0.01)  # TODO
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_true.register
def generate_gt_le(predicate: GtLePredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from random_datetimes(lower=lower + timedelta(seconds=1), upper=upper)
        case int(), _:
            yield from random_ints(lower=lower + 1, upper=upper)
        case float(), _:
            yield from random_floats(lower=lower + 0.01, upper=upper)
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_true.register
def generate_gt_lt(predicate: GtLtPredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from random_datetimes(lower=lower + timedelta(seconds=1), upper=upper - timedelta(seconds=1))
        case int(), _:
            yield from random_ints(lower=lower + 1, upper=upper - 1)
        case float(), _:
            yield from random_floats(lower=lower + 0.01, upper=upper - 0.01)  # TODO
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_true.register
def generate_ge(predicate: GePredicate, **_kwargs) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(lower=predicate.v)
        case float():
            yield from random_floats(lower=predicate.v)
        case int():
            yield from random_ints(lower=predicate.v)
        case str():
            yield v
            yield from generate_strings(predicate)
        case UUID():
            yield from generate_uuids(predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_true.register
def generate_gt(predicate: GtPredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(lower=predicate.v + timedelta(seconds=1))
        case float():
            yield from random_floats(lower=predicate.v + sys.float_info.epsilon)
        case int():
            yield from random_ints(lower=predicate.v + 1)
        case str():
            yield from generate_strings(predicate)
        case UUID():
            yield from generate_uuids(predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_true.register
def generate_has_key(predicate: HasKeyPredicate) -> Iterator:
    key = predicate.key
    for random_dict, value in zip(random_dicts(), random_anys(), strict=False):
        yield random_dict | {key: value}


@generate_true.register
def generate_has_length(predicate: HasLengthPredicate, *, value_p=is_int_p) -> Iterator:
    yield from random_iterables(length_p=predicate.length_p, value_p=value_p)


def create_value_predicate(path: list[Predicate]) -> Predicate:
    match path:
        case [head]:
            return head
        case [root, *rest] if root == is_list_p:
            valid_value = create_value_predicate(rest)
            return is_list_of_p(valid_value)
        case [root, *rest]:
            valid_keys = generate_true(root)
            valid_key = next(valid_keys)
            valid_value = create_value_predicate(rest)
            return is_dict_of_p((valid_key, valid_value))
        case []:
            return always_true_p
        case _:
            raise ValueError("Unreachable")


@generate_true.register
def generate_has_path(predicate: HasPathPredicate) -> Iterator:
    root, *rest = predicate.path

    valid_keys = generate_true(root)

    while True:
        valid_key = next(valid_keys)
        valid_value = create_value_predicate(rest)
        dict_of = is_dict_of_p((valid_key, valid_value))
        yield from generate_true(dict_of, length_p=ge_p(1))


@generate_true.register
def generate_le(predicate: LePredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(upper=predicate.v)
        case float():
            yield from random_floats(upper=predicate.v)
        case int():
            yield from random_ints(upper=predicate.v)
        case str():
            yield from generate_strings(predicate)
        case UUID():
            yield from generate_uuids(predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_true.register
def generate_subset(predicate: IsSubsetPredicate) -> Iterator:
    yield from powerset_of_sets(predicate.v)


@generate_true.register
def generate_real_subset(predicate: IsRealSubsetPredicate) -> Iterator:
    yield from (v for v in powerset_of_sets(predicate.v) if v != predicate.v)


@generate_true.register
def generate_fn_p(predicate: FnPredicate) -> Iterator:
    yield from predicate.generate_true_fn()


@generate_true.register
def generate_in(predicate: InPredicate) -> Iterator:
    while True:
        yield from predicate.v


@generate_true.register
def generate_lt(predicate: LtPredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(upper=predicate.v - timedelta(seconds=1))
        case float():
            yield from random_floats(upper=predicate.v - sys.float_info.epsilon)
        case int():
            yield from random_ints(upper=predicate.v - 1)
        case str():
            yield from generate_strings(predicate)
        case UUID():
            yield from generate_uuids(predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_true.register
def generate_ne(predicate: NePredicate) -> Iterator:
    klass = type(predicate.v)
    yield from (value for value in random_values_of_type(klass=klass) if value != predicate.v)


@generate_true.register
def generate_none(_predicate: IsNonePredicate) -> Iterator:
    yield from repeat(None)


@generate_true.register
def generate_not(predicate: NotPredicate) -> Iterator:
    from predicate import generate_false

    yield from generate_false(predicate.predicate)


@generate_true.register
def generate_not_in(predicate: NotInPredicate) -> Iterator:
    # TODO: not correct yet
    for item in predicate.v:
        match item:
            case int():
                yield from generate_ints(predicate)
            case str():
                yield from generate_strings(predicate)
            case UUID():
                yield from generate_uuids(predicate)
            case _:
                raise ValueError(f"Can't generate for type {type(item)}")


@generate_true.register
def generate_not_none(predicate: IsNotNonePredicate) -> Iterator:
    yield from generate_anys(predicate)


@generate_true.register
def generate_or(predicate: OrPredicate) -> Iterator:
    yield from random_first_from_iterables(generate_true(predicate.left), generate_true(predicate.right))


@generate_true.register
def generate_regex(predicate: RegexPredicate) -> Iterator:
    yield from exrex.generate(predicate.pattern)


@generate_true.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from (False, 0, (), "", {})


@generate_true.register
def generate_truthy(_predicate: IsTruthyPredicate) -> Iterator:
    yield from (True, 1, "true", {1}, 3.14)


@generate_true.register
def generate_predicate_of(predicate: IsPredicateOfPredicate, **kwargs) -> Iterator:
    yield from random_predicates(**kwargs, klass=predicate.predicate_klass)


@generate_true.register
def generate_is_instance_p(predicate: IsInstancePredicate, **kwargs) -> Iterator:
    klass = predicate.instance_klass[0]  # type: ignore

    type_registry: dict[Any, Callable[[], Iterator]] = {
        Callable: random_callables,
        Container: random_containers,
        Iterable: random_iterables,
        Predicate: random_predicates,
        UUID: random_uuids,
        bool: random_bools,
        complex: random_complex_numbers,
        datetime: random_datetimes,
        dict: random_dicts,
        float: random_floats,
        list: random_lists,
        int: random_ints,
        set: random_sets,
        str: random_strings,
        tuple: random_tuples,
    }

    if generator := type_registry.get(klass):
        yield from generator(**kwargs)
    elif klass == Predicate:  # TODO
        yield from random_predicates(**kwargs)
    else:
        raise ValueError(f"No generator found for {klass}")


@generate_true.register
def generate_is_lambda_p(predicate: IsLambdaPredicate) -> Iterator:
    nr_of_parameters = predicate.nr_of_parameters
    yield from random_lambdas(nr_of_parameters_p=eq_p(nr_of_parameters or 0))


@generate_true.register
def generate_dict_of_p(dict_of_predicate: DictOfPredicate, **kwargs) -> Iterator:
    key_value_predicates = dict_of_predicate.key_value_predicates

    candidates = zip(
        *flatten(((generate_true(key_p), generate_true(value_p, **kwargs)) for key_p, value_p in key_value_predicates)),
        strict=False,
    )

    yield from (dict(chunked(candidate, 2)) for candidate in candidates)


@generate_true.register
def generate_list_of_p(list_of_predicate: ListOfPredicate, *, length_p: Predicate = default_length_p) -> Iterator:
    predicate = list_of_predicate.predicate

    if length_p(0):
        yield []

    valid_lengths = generate_true(length_p)

    while True:
        length = next(valid_lengths)
        yield take(length, generate_true(predicate))


@generate_true.register
def generate_tuple_of_p(tuple_of_predicate: TupleOfPredicate) -> Iterator:
    predicates = tuple_of_predicate.predicates

    yield from zip(*(generate_true(predicate) for predicate in predicates), strict=False)


# property names were introduced in Python 3.13
if sys.version_info.minor > 12:

    @generate_true.register
    def generate_property_p(property_predicate: PropertyPredicate) -> Iterator:
        getter = property_predicate.getter

        attributes = {getter.__name__: getter}  # type: ignore
        klass = type("Foo", (object,), attributes)

        yield klass


@generate_true.register
def generate_set_of_p(
    set_of_predicate: SetOfPredicate, *, length_p: Predicate = default_length_p, order: bool = False
) -> Iterator:
    predicate = set_of_predicate.predicate

    valid_lengths = generate_true(length_p)

    while True:
        length = next(valid_lengths)
        values = take(length, generate_true(predicate))

        yield from set_from_list(values, order)


@generate_true.register
def generate_xor(predicate: XorPredicate) -> Iterator:
    if optimize(predicate) == always_false_p:
        yield from []
    else:
        left_and_not_right = (item for item in generate_true(predicate.left) if not predicate.right(item))
        right_and_not_left = (item for item in generate_true(predicate.right) if not predicate.left(item))
        yield from random_first_from_iterables(left_and_not_right, right_and_not_left)


@generate_true.register
def generate_tee(_predicate: TeePredicate) -> Iterator:
    yield from []
