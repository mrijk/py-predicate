import ast
import asyncio
import gc
import inspect
import io
import ipaddress
import logging
import os
import random
import re
import sys
from collections.abc import (
    Callable,
    Collection,
    Container,
    Generator,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Reversible,
    Sequence,
    Set,
    Sized,
)
from datetime import date, datetime, time, timedelta, timezone, tzinfo
from decimal import Decimal
from enum import Enum
from fractions import Fraction
from functools import singledispatch
from inspect import Parameter, Signature, getmembers, isfunction, signature
from itertools import chain, cycle, islice, repeat
from pathlib import PurePath
from time import struct_time
from types import CodeType, ModuleType, UnionType
from typing import (
    Any,
    Final,
    ForwardRef,
    Protocol,
    SupportsAbs,
    SupportsBytes,
    SupportsComplex,
    SupportsFloat,
    SupportsIndex,
    SupportsInt,
    SupportsRound,
    get_args,
    get_origin,
)
from uuid import UUID

import exrex  # type: ignore
from more_itertools import (
    chunked,
    first,
    flatten,
    powerset_of_sets,
    random_combination_with_replacement,
    random_permutation,
    take,
)

from predicate import generate_false
from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.count_predicate import CountPredicate
from predicate.dict_of_predicate import DictOfPredicate, is_dict_of_p
from predicate.eq_predicate import EqPredicate, eq_p
from predicate.exactly_predicate import ExactlyPredicate
from predicate.exception_predicate import ExceptionPredicate
from predicate.fn_predicate import FnPredicate
from predicate.frozendict_of_predicate import FrozenDictOfPredicate
from predicate.frozenset_of_predicate import FrozenSetOfPredicate
from predicate.ge_predicate import GePredicate, ge_p
from predicate.generator.generate_predicate import generate_predicate, predicate_type_registry
from predicate.generator.helpers import (
    accepted_kwargs,
    default_length_p,
    function_with_signature,
    generate_anys,
    generate_datetimes,
    generate_floats,
    generate_ints,
    generate_lambda,
    generate_strings,
    generate_uuids,
    ignore_unknown_kwargs,
    random_anys,
    random_ast_nodes,
    random_bools,
    random_bytearrays,
    random_bytes,
    random_callables,
    random_code_objects,
    random_complex_numbers,
    random_containers,
    random_dates,
    random_datetimes,
    random_decimals,
    random_dicts,
    random_enum_members,
    random_event_loops,
    random_exceptions,
    random_first_from_iterables,
    random_floats,
    random_forward_refs,
    random_fractions,
    random_frozensets,
    random_hashables,
    random_ints,
    random_ios,
    random_ipv4_addresses,
    random_ipv4_networks,
    random_ipv6_addresses,
    random_ipv6_networks,
    random_iterables,
    random_lambdas,
    random_lengths,
    random_lists,
    random_log_records,
    random_loggers,
    random_modules,
    random_named_tuple_instances,
    random_named_tuples,
    random_parameters,
    random_paths,
    random_patterns,
    random_predicates,
    random_ranges,
    random_sets,
    random_signatures,
    random_sized,
    random_slices,
    random_strings,
    random_struct_times,
    random_supports,
    random_text_ios,
    random_timedeltas,
    random_times,
    random_tuples,
    random_tzinfos,
    random_uuids,
    random_values_of_type,
    sample_optional_fields,
    set_from_list,
    unused_name,
    with_parameters,
)
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.has_path_predicate import HasPathPredicate
from predicate.implements_protocol_predicate import ImplementsProtocolPredicate, protocol_members
from predicate.in_predicate import InPredicate
from predicate.is_async_predicate import IsAsyncPredicate
from predicate.is_callable_predicate import IsCallablePredicate
from predicate.is_close_predicate import IsClosePredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_lambda_predicate import IsLambdaPredicate
from predicate.is_named_tuple_predicate import IsNamedTuplePredicate, is_named_tuple_class
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_predicate import IsPredicate
from predicate.is_predicate_of_p import IsPredicateOfPredicate
from predicate.is_protocol_predicate import IsProtocolPredicate
from predicate.is_regex_predicate import IsRegexPredicate
from predicate.is_subclass_predicate import IsSubclassPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.juxt_predicate import JuxtPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate, is_list_of_p
from predicate.lt_predicate import LtPredicate
from predicate.match_predicate import MatchPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.not_predicate import NotPredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.optional_predicate import OptionalPredicate
from predicate.or_predicate import OrPredicate
from predicate.plus_predicate import PlusPredicate
from predicate.predicate import ConstrainedT, Predicate
from predicate.property_predicate import PropertyPredicate
from predicate.raises_predicate import RaisesPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate, ge_le_p
from predicate.reduce_predicate import ReducePredicate
from predicate.regex_predicate import RegexPredicate
from predicate.repeat_predicate import RepeatPredicate
from predicate.same_signature_predicate import SameSignaturePredicate, same_signature_p
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import (
    IntersectsPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)
from predicate.standard_predicates import is_int_p, is_list_p
from predicate.star_predicate import StarPredicate
from predicate.struct_predicate import StructPredicate
from predicate.tee_predicate import TeePredicate
from predicate.tuple_of_predicate import TupleOfPredicate
from predicate.type_var_predicate import ConstrainedTypeVarPredicate, FreeTypeVarPredicate
from predicate.xor_predicate import XorPredicate


@ignore_unknown_kwargs
@singledispatch
def generate_true[T](predicate: Predicate[T], **_kwargs: Any) -> Iterator[T]:
    """Generate values that satisfy this predicate."""
    raise ValueError(f"Please register generator for correct predicate type: {predicate}")


@generate_true.register
def generate_all_p(all_predicate: AllPredicate, *, length_p: Predicate = default_length_p) -> Iterator:
    predicate = all_predicate.predicate

    for max_length in random_lengths(length_p):
        # One empty value, not an empty tuple, set and list in a row
        yield from _all_p_values(predicate, max_length) if max_length else [[]]


def _all_p_values(predicate: Predicate, max_length: int) -> Iterator:
    values = take(max_length, generate_true(predicate))
    if not values:
        # The item predicate has no values (e.g. ge_lt_p(0, 0)): only an empty collection satisfies all_p
        yield []
        return
    yield random_combination_with_replacement(values, max_length)

    values = take(max_length, generate_true(predicate))
    # isinstance(value, Hashable) isn't enough: a tuple is Hashable even when its items aren't
    if all(_is_hashable(value) for value in values):
        yield set(random_combination_with_replacement(values, max_length))

    values = take(max_length, generate_true(predicate))
    yield list(random_combination_with_replacement(values, max_length))


def _is_hashable(value: Any) -> bool:
    try:
        hash(value)
    except TypeError:
        return False
    return True


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
        if not true_values:
            return  # the item predicate has no values (e.g. ge_lt_p(0, 0)), so no iterable satisfies any_p

        combined_values = false_values + true_values

        yield random_permutation(combined_values)
        yield from set_from_list(combined_values)


@generate_true.register
def generate_free_type_var(_predicate: FreeTypeVarPredicate, **_kwargs: Any) -> Iterator:
    # One kind of value per stream, and each generated collection draws from a fresh stream:
    # list[T] is never a mix of e.g. datetimes and floats, which a sort function can't compare (#375)
    yield from random.choice((random_bools, random_ints, random_strings, random_floats, random_datetimes))()


@generate_true.register
def generate_constrained_type_var(predicate: ConstrainedTypeVarPredicate, **_kwargs: Any) -> Iterator:
    # T is exactly one of its constraints per call, so a list[T] is all ints or all strs, not both (#375)
    # ponytail: with 3+ constraints the nested choice favours the last one, uniform would need the full list
    yield from generate_true(random.choice((predicate.left, predicate.right)))


@generate_true.register
def generate_always_true(_predicate: AlwaysTruePredicate, **_kwargs: Any) -> Iterator:
    yield from random_anys()


@generate_true.register
def generate_exception(_predicate: ExceptionPredicate) -> Iterator:
    yield from []


def _satisfying(values: Iterator, predicate: Predicate, attempts: int) -> Iterator:
    """Return the values that satisfy the predicate; stops after attempts misses in a row, so it can't hang.

    E.g. is_tuple_p & is_empty_p: random tuples are only rarely empty.
    """
    misses = 0
    for value in values:
        if predicate(value):
            misses = 0
            yield value
        else:
            misses += 1
            if misses == attempts:
                return


@generate_true.register
def generate_and(predicate: AndPredicate) -> Iterator:
    if optimize(predicate) == always_false_p:
        yield from []
    else:
        attempts = 100
        _sentinel = object()

        left_values = generate_true(predicate.left)
        right_values = generate_true(predicate.right)
        first_left = next((item for item in islice(left_values, attempts) if predicate.right(item)), _sentinel)
        first_right = next((item for item in islice(right_values, attempts) if predicate.left(item)), _sentinel)

        iterables = []
        if first_left is not _sentinel:
            iterables.append(chain([first_left], _satisfying(left_values, predicate.right, attempts)))
        if first_right is not _sentinel:
            # Both sides often start with the same edge case, e.g. []: yield it once (#356)
            head = [] if first_right == first_left else [first_right]
            iterables.append(chain(head, _satisfying(right_values, predicate.left, attempts)))

        if not iterables:
            raise ValueError(f"Couldn't generate values that satisfy {predicate}")

        yield from random_first_from_iterables(*iterables)


@generate_true.register
def generate_eq(predicate: EqPredicate, **_kwargs: Any) -> Iterator:
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
def generate_ge(predicate: GePredicate, **_kwargs: Any) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(lower=predicate.v)
        case float():
            yield from random_floats(lower=predicate.v)
        case int():
            yield v
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
            yield v + 1
            yield from random_ints(lower=predicate.v + 1)
        case str():
            yield from generate_strings(predicate)
        case UUID():
            yield from generate_uuids(predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_true.register
def generate_is_close_p(predicate: IsClosePredicate) -> Iterator:
    yield from repeat(predicate.target)


@generate_true.register
def generate_has_key(predicate: HasKeyPredicate) -> Iterator:
    keys = generate_true(predicate.key_p)
    yield from (d | {key: v} for d, v, key in zip(random_dicts(), random_anys(), keys, strict=False))


@generate_true.register
def generate_has_length(predicate: HasLengthPredicate, *, value_p: Predicate = is_int_p) -> Iterator:
    yield from random_iterables(length_p=predicate.length_p, value_p=value_p)


def _create_value_predicate(path: list[Predicate]) -> Predicate:
    match path:
        case [head]:
            return head
        case [root, *rest] if root == is_list_p:
            valid_value = _create_value_predicate(rest)
            return is_list_of_p(valid_value)
        case [root, *rest]:
            valid_keys = generate_true(root)
            valid_key = next(valid_keys)
            valid_value = _create_value_predicate(rest)
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
        valid_value = _create_value_predicate(rest)
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
            yield v
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
def generate_superset(predicate: IsSupersetPredicate) -> Iterator:
    yield from (predicate.v | extra for extra in random_sets())


@generate_true.register
def generate_real_superset(predicate: IsRealSupersetPredicate) -> Iterator:
    yield from (candidate for extra in random_sets() if (candidate := predicate.v | extra) > predicate.v)


@generate_true.register
def generate_intersects(predicate: IntersectsPredicate) -> Iterator:
    if not predicate.v:
        return
    elements = list(predicate.v)
    yield from (extra | {random.choice(elements)} for extra in random_sets())


@generate_true.register
def generate_fn_p(predicate: FnPredicate) -> Iterator:
    yield from predicate.generate_true_fn()


@generate_true.register
def generate_in(predicate: InPredicate) -> Iterator:
    if isinstance(predicate.v, Iterable):
        yield from cycle(predicate.v)
        return
    raise ValueError(f"Can't generate true values for type {predicate.v.__class__.__name__}")


@generate_true.register
def generate_lt(predicate: LtPredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(upper=predicate.v - timedelta(seconds=1))
        case float():
            yield from random_floats(upper=predicate.v - sys.float_info.epsilon)
        case int():
            yield v - 1
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
def generate_is_regex(predicate: IsRegexPredicate) -> Iterator:
    yield from generate_strings(predicate)


@generate_true.register
def generate_is_protocol(_predicate: IsProtocolPredicate) -> Iterator:
    yield from cycle([Protocol, SupportsAbs, SupportsBytes, SupportsFloat, SupportsIndex, SupportsInt])


@generate_true.register
def generate_implements_protocol(predicate: ImplementsProtocolPredicate) -> Iterator:
    protocol = predicate.protocol
    members = protocol_members(protocol)
    methods = {
        name: generate_true(same_signature_p(method))
        for name, method in getmembers(protocol, isfunction)
        if name in members
    }
    # Data members only need to exist on the class, so None will do
    while True:
        attributes = {name: next(methods[name]) if name in methods else None for name in members}
        yield type(f"{protocol.__name__}Implementation", (), attributes)


@generate_true.register
def generate_same_signature(predicate: SameSignaturePredicate) -> Iterator:
    sig = signature(predicate.function, eval_str=True)
    kinds = {p.kind for p in sig.parameters.values()}

    optional = Parameter(unused_name(sig), Parameter.KEYWORD_ONLY, default=None)
    var_args = [
        Parameter(name, kind)
        for name, kind in (("args", Parameter.VAR_POSITIONAL), ("kwargs", Parameter.VAR_KEYWORD))
        if kind not in kinds and name not in sig.parameters
    ]
    # Any is compatible with every type, for both parameters and return type
    any_types = sig.replace(
        parameters=[p.replace(annotation=Any) for p in sig.parameters.values()], return_annotation=Any
    )

    signatures = [sig, with_parameters(sig, optional), with_parameters(sig, *var_args), any_types]
    yield from cycle(function_with_signature(s) for s in signatures)


@generate_true.register
def generate_not(predicate: NotPredicate) -> Iterator:
    from predicate import generate_false

    yield from generate_false(predicate.predicate)


def _generator_for_item(item, predicate: NotInPredicate) -> Iterator:
    match item:
        case datetime():
            return generate_datetimes(predicate)
        case float():
            return generate_floats(predicate)
        case int():
            return generate_ints(predicate)
        case str():
            return generate_strings(predicate)
        case UUID():
            return generate_uuids(predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(item)}")


@generate_true.register
def generate_not_in(predicate: NotInPredicate) -> Iterator:
    if isinstance(predicate.v, Iterable):
        generators = {type(item): _generator_for_item(item, predicate) for item in predicate.v}
        if generators:
            yield from random_first_from_iterables(*generators.values())
        else:
            # Nothing is in an empty container, so any value is not in it
            yield from random_anys()


@generate_true.register
def generate_not_none(predicate: IsNotNonePredicate) -> Iterator:
    yield from generate_anys(predicate)


@generate_true.register
def generate_or(predicate: OrPredicate) -> Iterator:
    yield from random_first_from_iterables(generate_true(predicate.left), generate_true(predicate.right))


@generate_true.register
def generate_reduce_p(predicate: ReducePredicate) -> Iterator:
    yield []


@generate_true.register
def generate_regex(predicate: RegexPredicate) -> Iterator:
    yield from exrex.generate(predicate.pattern)


@generate_true.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from cycle((False, 0, (), "", {}))


@generate_true.register
def generate_truthy(_predicate: IsTruthyPredicate) -> Iterator:
    yield from cycle((True, 1, "true", frozenset({1}), 3.14))


@generate_true.register
def generate_predicate_of(predicate: IsPredicateOfPredicate, **kwargs: Any) -> Iterator:
    yield from random_predicates(**kwargs, klass=predicate.predicate_klass)


_supports_protocols: Final = (
    SupportsAbs,
    SupportsBytes,
    SupportsComplex,
    SupportsFloat,
    SupportsIndex,
    SupportsInt,
    SupportsRound,
)


_abc_builtins: Final[dict[Any, Any]] = {
    Collection: list,
    Iterable: list,  # only generated: checking items would consume an iterator argument (#372)
    Sequence: list,
    MutableSequence: list,
    Reversible: list,
    Set: set,
    MutableSet: set,
    Mapping: dict,
    MutableMapping: dict,
}


def _random_iterators(annotation: Any) -> Iterator[Iterator]:
    from predicate.spec.exercise_helpers import annotation_to_predicate

    # A fresh iterator per value: an iterator can only be consumed once. Generator[T, ...] yields T too.
    item_type = first(get_args(annotation), Any)
    lists = generate_true(annotation_to_predicate(list[item_type]))  # type: ignore[valid-type]
    yield from ((item for item in items) for items in lists)


def _random_returning_callables(return_type: Any) -> Iterator[Callable]:
    from predicate.spec.exercise_helpers import annotation_to_predicate

    # Callable[[A], R]: a function returning a fresh R on each call (#296); it accepts any arguments
    return_p = annotation_to_predicate(return_type)
    while True:
        yield _returning(generate_true(return_p))


def _returning(values: Iterator) -> Callable:
    def function(*_args: Any, **_kwargs: Any) -> Any:
        return next(values)

    return function


def _random_classes_with_metaclass(metaclass: type) -> Iterator[type]:
    """Return existing classes whose metaclass is metaclass, e.g. polars' data types for DataTypeClass (#357).

    A metaclass annotation means an existing class with that metaclass: calling the metaclass would create a new class.
    """
    # ponytail: only classes that already exist, found through gc, like the subclass walk for abstract classes (#355)
    classes = [obj for obj in gc.get_objects() if isinstance(obj, type) and isinstance(obj, metaclass)]
    # Base classes are often abstract in all but name (polars' DataType, NumericType), so prefer the leaves
    leaves = [
        klass
        for klass in classes
        if not inspect.isabstract(klass) and not any(isinstance(sub, metaclass) for sub in _all_subclasses(klass))
    ]
    candidates = leaves or classes
    if not candidates:
        raise ValueError(f"No generator found for {metaclass}: no class with this metaclass exists")
    while True:
        yield random.choice(candidates)


def _family_generator(klass: Any, annotation: Any) -> Iterator | None:
    """Return a generator for a whole family of types (enums, paths, Supports* protocols, patterns, ...), or None."""
    if klass is Callable and (args := get_args(annotation)) and args[-1] is not Any:
        return _random_returning_callables(args[-1])
    if isinstance(klass, type) and issubclass(klass, type) and klass is not type:
        return _random_classes_with_metaclass(klass)
    if isinstance(klass, type) and issubclass(klass, Enum):
        return random_enum_members(klass)
    if isinstance(klass, type) and issubclass(klass, PurePath):
        return random_paths(klass)
    if klass in _supports_protocols:
        return random_supports(klass)
    if klass is re.Pattern:
        return random_patterns(first(get_args(annotation), str))
    if is_named_tuple_class(klass):
        return random_named_tuple_instances(klass)
    if isinstance(klass, type) and issubclass(klass, ast.AST):
        return random_ast_nodes(klass)
    return None


# A class built from its __init__ may need another such class as an argument, but not deeper than this
_MAX_CONSTRUCT_DEPTH: Final = 2
# Consecutive constructor failures before giving up on a class
_MAX_CONSTRUCT_ATTEMPTS: Final = 20
_construct_depth = 0


def _constructed_instances(klass: Any) -> Iterator:
    """Return instances of a class built from its fully annotated __init__ (#305); the last resort for a class."""
    candidates = [(c, params) for c in _constructible_classes(klass) if (params := _init_params(c)) is not None]
    if not candidates:
        raise ValueError(f"No generator found for {klass}")
    return _random_constructed(klass, candidates)


def _constructible_classes(klass: Any) -> list[Any]:
    # An abstract class can't be built itself, but its concrete subclasses may be (#354); protocols are left out.
    # A base class with subclasses is often abstract in all but name (e.g. sqlglot's Expr), so it's skipped too (#358)
    if isinstance(klass, type) and not getattr(klass, "_is_protocol", False):
        return _all_subclasses(klass) or [klass]
    return [klass]


def _all_subclasses(klass: type) -> list[type]:
    # ponytail: only subclasses that are already imported, like random_modules
    direct: list[type] = klass.__subclasses__()
    return list(dict.fromkeys(chain(direct, *(_all_subclasses(subclass) for subclass in direct))))


def _init_params(klass: Any) -> list[Parameter] | None:
    """Return the __init__ parameters to generate, or None if the class can't be built from its annotations."""
    if not isinstance(klass, type) or inspect.isabstract(klass) or getattr(klass, "_is_protocol", False):
        return None
    if _construct_depth >= _MAX_CONSTRUCT_DEPTH:
        return None
    from predicate.spec.exercise_helpers import resolved_signature

    try:
        # A class without its own __init__ has object's (self, /, *args, **kwargs): it's built without arguments
        init_signature = resolved_signature(klass.__init__)  # type: ignore[misc]
    except (TypeError, ValueError, NameError):
        return None
    params = [
        param
        for name, param in list(init_signature.parameters.items())[1:]  # skip self
        if param.kind not in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD) and not name.startswith("_")
    ]
    return None if any(param.annotation is Parameter.empty for param in params) else params


def _random_constructed(klass: type, candidates: list[tuple[type, list[Parameter]]]) -> Iterator:
    errors: list[str] = []
    while len(errors) < _MAX_CONSTRUCT_ATTEMPTS:
        value, error = _try_construct(*random.choice(candidates))
        if error:
            errors.append(error)
        else:
            errors.clear()
            yield value
    most_common = max(set(errors), key=errors.count)
    what = "its constructor keeps" if [c for c, _ in candidates] == [klass] else "its subclasses keep"
    raise ValueError(f"No generator found for {klass}: {what} raising ({most_common})")


def _try_construct(klass: type, params: list[Parameter]) -> tuple[Any, str | None]:
    try:
        return _construct(klass, params), None
    except Exception as e:  # noqa: BLE001  any constructor error just rejects this candidate
        return None, f"{type(e).__name__}: {e}"


def _construct(klass: type, params: list[Parameter]) -> Any:
    from predicate.spec.exercise_helpers import param_predicate

    global _construct_depth
    # Optional parameters are left out half the time, so the defaults are used too
    chosen = [param for param in params if param.default is Parameter.empty or random.random() < 0.5]
    _construct_depth += 1
    try:
        values = {param.name: first(generate_true(param_predicate(param))) for param in chosen}
    finally:
        _construct_depth -= 1
    args = [values[param.name] for param in chosen if param.kind == Parameter.POSITIONAL_ONLY]
    kwargs = {param.name: values[param.name] for param in chosen if param.kind != Parameter.POSITIONAL_ONLY}
    return klass(*args, **kwargs)


def _random_predicates_of_type(klass: type[Predicate], kwargs: dict) -> Iterator[Predicate]:
    if klass is Predicate:
        return random_predicates(**kwargs)
    if klass not in predicate_type_registry():
        # No dedicated generator, e.g. ListOfPredicate: build it from its annotated __init__
        return _constructed_instances(klass)
    # A concrete predicate class with a dedicated generator, e.g. InPredicate
    return generate_predicate(klass, **{"max_depth": 10, "klass": int} | accepted_kwargs(random_predicates, kwargs))


def _type_arg_predicate(arg: Any) -> Predicate:
    from predicate.spec.exercise_helpers import type_arg_predicate

    # Same rules as the check: TypeVar -> its bound, None -> NoneType, NamedTuple -> namedtuple classes, ...
    return type_arg_predicate(arg)


@generate_true.register
def generate_is_instance_p(predicate: IsInstancePredicate, **kwargs: Any) -> Iterator:
    annotation = predicate.instance_klass[0]  # type: ignore
    # Generic aliases such as Predicate[int], typing.Callable and Iterable[int] map to their origin class
    klass = get_origin(annotation) or annotation

    type_registry: dict[Any, Callable[[], Iterator]] = {
        Callable: random_callables,
        Container: random_containers,
        Hashable: random_hashables,
        Iterable: random_iterables,
        # Abstract collections map to the builtin that implements them
        Collection: random_iterables,
        Sequence: random_lists,
        Reversible: random_lists,
        MutableSequence: random_lists,
        Set: random_sets,
        MutableSet: random_sets,
        Mapping: random_dicts,
        MutableMapping: random_dicts,
        Predicate: random_predicates,
        UUID: random_uuids,
        ModuleType: random_modules,
        Signature: random_signatures,
        bool: random_bools,
        complex: random_complex_numbers,
        bytearray: random_bytearrays,
        bytes: random_bytes,
        date: random_dates,
        Decimal: random_decimals,
        slice: random_slices,
        Fraction: random_fractions,
        ipaddress.IPv4Address: random_ipv4_addresses,
        ipaddress.IPv6Address: random_ipv6_addresses,
        ipaddress.IPv4Network: random_ipv4_networks,
        ipaddress.IPv6Network: random_ipv6_networks,
        Parameter: random_parameters,
        logging.LogRecord: random_log_records,
        logging.Logger: random_loggers,
        asyncio.AbstractEventLoop: random_event_loops,
        asyncio.BaseEventLoop: random_event_loops,
        io.IOBase: random_ios,
        io.TextIOBase: random_text_ios,
        range: random_ranges,
        struct_time: random_struct_times,
        tzinfo: random_tzinfos,
        timezone: random_tzinfos,
        BaseException: random_exceptions,
        Exception: random_exceptions,
        ForwardRef: random_forward_refs,
        CodeType: random_code_objects,
        Sized: random_sized,
        datetime: random_datetimes,
        os.PathLike: random_paths,
        time: random_times,
        timedelta: random_timedeltas,
        dict: random_dicts,
        float: random_floats,
        list: random_lists,
        int: random_ints,
        set: random_sets,
        frozenset: random_frozensets,
        str: random_strings,
        tuple: random_tuples,
    }

    if sys.version_info >= (3, 15):
        from predicate.generator.helpers import random_frozendicts, random_sentinels

        type_registry[frozendict] = random_frozendicts  # noqa: F821
        type_registry[sentinel] = random_sentinels  # noqa: F821

    if sys.version_info >= (3, 14):
        from string.templatelib import Template

        from predicate.generator.helpers import random_templates

        type_registry[Template] = random_templates

    if klass in (Iterator, Generator):
        yield from _random_iterators(annotation)
    elif (builtin := _abc_builtins.get(klass)) and (args := get_args(annotation)):
        from predicate.spec.exercise_helpers import annotation_to_predicate

        # Sequence[int] -> list[int] etc., so the generated items have the requested types
        yield from generate_true(annotation_to_predicate(builtin[args]))
    elif (family_values := _family_generator(klass, annotation)) is not None:
        yield from family_values
    elif generator := type_registry.get(klass):
        yield from generator(**accepted_kwargs(generator, kwargs))
    elif klass is type:
        # For type[X] yield X and its subclasses, for plain type any class
        yield from generate_true(_type_arg_predicate(first(get_args(annotation), object)))
    elif klass == ConstrainedT:
        iterables = [random_ints()]
        yield from random_first_from_iterables(*iterables)
    elif isinstance(klass, type) and issubclass(klass, Predicate):
        yield from _random_predicates_of_type(klass, kwargs)
    else:
        yield from _constructed_instances(klass)


@generate_true.register
def generate_is_callable_p(predicate: IsCallablePredicate) -> Iterator:
    arg_names = [f"arg{i}" for i in range(len(predicate.params))]
    fn = generate_lambda(arg_names)
    fn.__annotations__ = dict(zip(arg_names, predicate.params, strict=False))
    fn.__annotations__["return"] = predicate.return_type
    while True:
        yield fn


@generate_true.register
def generate_is_async_p(predicate: IsAsyncPredicate) -> Iterator:
    async def _async_fn():
        pass

    while True:
        yield _async_fn


@generate_true.register
def generate_is_named_tuple_p(_predicate: IsNamedTuplePredicate) -> Iterator:
    yield from random_named_tuples()


@generate_true.register
def generate_is_lambda_p(predicate: IsLambdaPredicate) -> Iterator:
    nr_of_parameters = predicate.nr_of_parameters
    yield from random_lambdas(nr_of_parameters_p=eq_p(nr_of_parameters or 0))


@generate_true.register
def generate_dict_of_p(dict_of_predicate: DictOfPredicate, **kwargs: Any) -> Iterator:
    key_value_predicates = dict_of_predicate.key_value_predicates

    candidates = zip(
        *flatten(((generate_true(key_p), generate_true(value_p, **kwargs)) for key_p, value_p in key_value_predicates)),
        strict=False,
    )

    yield from (dict(chunked(candidate, 2)) for candidate in candidates)


@generate_true.register
def generate_frozendict_of_p(frozendict_of_predicate: FrozenDictOfPredicate, **kwargs: Any) -> Iterator:
    if sys.version_info >= (3, 15):
        dict_of_predicate = frozendict_of_predicate.dict_of_predicate
        yield from (frozendict(d) for d in generate_dict_of_p(dict_of_predicate, **kwargs))  # noqa: F821
    else:
        yield from []


@generate_true.register
def generate_list_of_p(list_of_predicate: ListOfPredicate, *, length_p: Predicate = default_length_p) -> Iterator:
    predicate = list_of_predicate.predicate

    yield from (take(length, generate_true(predicate)) for length in random_lengths(length_p))


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

    for length in random_lengths(length_p):
        values = take(length, generate_true(predicate))

        yield from set_from_list(values, order)


@generate_true.register
def generate_frozenset_of_p(
    frozenset_of_predicate: FrozenSetOfPredicate, *, length_p: Predicate = default_length_p
) -> Iterator:
    set_of_predicate: SetOfPredicate = SetOfPredicate(frozenset_of_predicate.predicate)
    yield from (frozenset(s) for s in generate_set_of_p(set_of_predicate, length_p=length_p))


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
    yield from random_anys()


@generate_true.register
def generate_match_p(match_predicate: MatchPredicate) -> Iterator:
    predicates = match_predicate.predicates

    predicate, *rest_predicates = predicates

    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            yield from generate_true(predicate, predicates=rest_predicates)
        case Predicate():
            if rest_predicates:
                iter_first = generate_true(predicate)
                iter_rest: Iterator = generate_true(MatchPredicate(predicates=rest_predicates))
                while True:
                    yield [next(iter_first)] + list(next(iter_rest))
            else:
                yield from zip(generate_true(predicate), strict=False)


@generate_true.register
def generate_exactly_n(exactly_predicate: ExactlyPredicate, *, predicates: list[Predicate]) -> Iterator:
    predicate = exactly_predicate.predicate

    list_of_predicate = is_list_of_p(predicate=predicate)

    n = exactly_predicate.n
    length_p = eq_p(n)

    if predicates:
        iter_first = generate_true(list_of_predicate, length_p=length_p)
        iter_rest: Iterator = generate_true(MatchPredicate(predicates=predicates))
        while True:
            yield list(next(iter_first)) + list(next(iter_rest))
    else:
        yield from generate_true(list_of_predicate, length_p=length_p)


@generate_true.register
def generate_repeat(repeat_predicate: RepeatPredicate, *, predicates: list[Predicate]) -> Iterator:
    predicate = repeat_predicate.predicate

    list_of_predicate = is_list_of_p(predicate=predicate)

    m = repeat_predicate.m
    n = repeat_predicate.n
    length_p = ge_le_p(lower=m, upper=n)

    if predicates:
        iter_first = generate_true(list_of_predicate, length_p=length_p)
        iter_rest: Iterator = generate_true(MatchPredicate(predicates=predicates))
        while True:
            yield list(next(iter_first)) + list(next(iter_rest))
    else:
        yield from generate_true(is_list_of_p(predicate=predicate), length_p=length_p)


@generate_true.register
def generate_star(star_predicate: StarPredicate, *, predicates: list[Predicate]) -> Iterator:
    predicate = star_predicate.predicate

    m = 0
    n = 10  # Some reasonable number

    yield from generate_true(RepeatPredicate(m=m, n=n, predicate=predicate), predicates=predicates)


@generate_true.register
def generate_plus(plus_predicate: PlusPredicate, *, predicates: list[Predicate]) -> Iterator:
    predicate = plus_predicate.predicate

    m = 1
    n = 10  # Some reasonable number

    yield from generate_true(RepeatPredicate(m=m, n=n, predicate=predicate), predicates=predicates)


@generate_true.register
def generate_optional(optional_predicate: OptionalPredicate, *, predicates: list[Predicate]) -> Iterator:
    predicate = optional_predicate.predicate

    m = 0
    n = 1

    yield from generate_true(RepeatPredicate(m=m, n=n, predicate=predicate), predicates=predicates)


@generate_true.register
def generate_count(count_predicate: CountPredicate) -> Iterator:
    predicate = count_predicate.predicate
    length_p = count_predicate.length_p

    valid_counts = generate_true(length_p)

    while True:
        count = next(valid_counts)
        true_values = list(take(count, generate_true(predicate)))

        yield list(random_permutation(true_values))

        nr_false = random.randint(1, 5)
        false_values = list(take(nr_false, generate_false(predicate)))
        if false_values:
            yield list(random_permutation(true_values + false_values))


def _yield_subclasses(klasses: list[type]) -> Iterator:
    while True:
        for klass in klasses:
            yield klass
            yield from klass.__subclasses__()


@generate_true.register
def generate_is_subclass(is_subclass_predicate: IsSubclassPredicate) -> Iterator:
    match is_subclass_predicate.class_or_tuple:
        case tuple(klasses):
            yield from _yield_subclasses(list(klasses))
        case UnionType() as union_type:
            yield from _yield_subclasses(list(get_args(union_type)))
        case _ as klass:
            yield from _yield_subclasses([klass])


@generate_true.register
def generate_is(is_predicate: IsPredicate) -> Iterator:
    yield from repeat(is_predicate.v)


@generate_true.register
def generate_juxt_p(predicate: JuxtPredicate) -> Iterator:
    generators = [generate_true(p) for p in predicate.predicates]
    for gen in cycle(generators):
        candidate = next(gen)
        if predicate(candidate):
            yield candidate


@generate_true.register
def generate_raises(predicate: RaisesPredicate) -> Iterator:
    exc_type = predicate.exception_type
    while True:
        yield lambda: (_ for _ in ()).throw(exc_type())


@generate_true.register
def generate_struct(predicate: StructPredicate) -> Iterator:
    required = predicate.required
    optional = predicate.optional

    dict_of_predicate = DictOfPredicate(key_value_predicates=list(required.items()))
    optional_generators = {key: generate_true(value_p) for key, value_p in optional.items()}
    # Without required keys there is nothing to zip, so start from an endless supply of empty dicts
    required_dicts = generate_dict_of_p(dict_of_predicate) if required else repeat({})

    yield from (d | sample_optional_fields(optional, optional_generators) for d in required_dicts)
