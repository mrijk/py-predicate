import random
import sys
from collections.abc import Callable, Container, Iterable, Iterator
from datetime import datetime, timedelta
from functools import singledispatch
from itertools import cycle, repeat
from types import UnionType
from typing import Any, Final, Hashable, get_args
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
from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.count_predicate import CountPredicate
from predicate.dict_of_predicate import DictOfPredicate, is_dict_of_p
from predicate.eq_predicate import EqPredicate, eq_p
from predicate.exactly_predicate import ExactlyPredicate
from predicate.exception_predicate import ExceptionPredicate
from predicate.fn_predicate import FnPredicate
from predicate.ge_predicate import GePredicate, ge_p
from predicate.generator.helpers import (
    default_length_p,
    generate_anys,
    generate_datetimes,
    generate_floats,
    generate_ints,
    generate_lambda,
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
    random_hashables,
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
    sample_optional_fields,
    set_from_list,
)
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.has_path_predicate import HasPathPredicate
from predicate.in_predicate import InPredicate
from predicate.is_async_predicate import IsAsyncPredicate
from predicate.is_callable_predicate import IsCallablePredicate
from predicate.is_close_predicate import IsClosePredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_lambda_predicate import IsLambdaPredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_predicate import IsPredicate
from predicate.is_predicate_of_p import IsPredicateOfPredicate
from predicate.is_subclass_predicate import IsSubclassPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.juxt_predicate import JuxtPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate, is_list_of_p
from predicate.lt_predicate import LtPredicate
from predicate.match_predicate import (
    MatchPredicate,
)
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.optional_predicate import OptionalPredicate
from predicate.plus_predicate import PlusPredicate
from predicate.predicate import (
    AndPredicate,
    ConstrainedT,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.property_predicate import PropertyPredicate
from predicate.raises_predicate import RaisesPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate, ge_le_p
from predicate.reduce_predicate import ReducePredicate
from predicate.regex_predicate import RegexPredicate
from predicate.repeat_predicate import RepeatPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import (
    IntersectsPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)
from predicate.standard_predicates import (
    is_int_p,
    is_list_p,
)
from predicate.star_predicate import StarPredicate
from predicate.struct_predicate import StructPredicate
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
def generate_exception(_predicate: ExceptionPredicate) -> Iterator:
    yield from []


@generate_true.register
def generate_and(predicate: AndPredicate) -> Iterator:
    if optimize(predicate) == always_false_p:
        yield from []
    else:
        attempts = 100
        _sentinel = object()

        first_left = next(
            (item for item in take(attempts, generate_true(predicate.left)) if predicate.right(item)), _sentinel
        )
        first_right = next(
            (item for item in take(attempts, generate_true(predicate.right)) if predicate.left(item)), _sentinel
        )

        iterables = []
        if first_left is not _sentinel:
            iterables.append(item for item in generate_true(predicate.left) if predicate.right(item))
        if first_right is not _sentinel:
            iterables.append(item for item in generate_true(predicate.right) if predicate.left(item))

        if not iterables:
            raise ValueError(f"Couldn't generate values that satisfy {predicate}")

        yield from random_first_from_iterables(*iterables)


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
def generate_is_close_p(predicate: IsClosePredicate) -> Iterator:
    yield from repeat(predicate.target)


@generate_true.register
def generate_has_key(predicate: HasKeyPredicate) -> Iterator:
    keys = generate_true(predicate.key_p)
    yield from (d | {key: v} for d, v, key in zip(random_dicts(), random_anys(), keys, strict=False))


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
        while True:
            yield from predicate.v
    raise ValueError(f"Can't generate true values for type {predicate.v.__class__.__name__}")


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
def generate_predicate_of(predicate: IsPredicateOfPredicate, **kwargs) -> Iterator:
    yield from random_predicates(**kwargs, klass=predicate.predicate_klass)


@generate_true.register
def generate_is_instance_p(predicate: IsInstancePredicate, **kwargs) -> Iterator:
    klass = predicate.instance_klass[0]  # type: ignore

    type_registry: dict[Any, Callable[[], Iterator]] = {
        Callable: random_callables,
        Container: random_containers,
        Hashable: random_hashables,
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
    elif klass == ConstrainedT:
        iterables = [random_ints()]
        yield from random_first_from_iterables(*iterables)
    elif klass == Predicate:  # TODO
        yield from random_predicates(**kwargs)
    else:
        raise ValueError(f"No generator found for {klass}")


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

    yield from (
        d | sample_optional_fields(optional, optional_generators) for d in generate_dict_of_p(dict_of_predicate)
    )
