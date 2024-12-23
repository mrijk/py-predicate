import random
import sys
from collections.abc import Iterator
from datetime import datetime, timedelta
from functools import singledispatch
from itertools import repeat
from uuid import UUID

from more_itertools import chunked, flatten, interleave, random_combination_with_replacement, random_permutation, take

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.generator.helpers import (
    generate_anys,
    generate_ints,
    generate_strings,
    generate_uuids,
    random_anys,
    random_datetimes,
    random_dicts,
    random_first_from_iterables,
    random_floats,
    random_ints,
    random_iterables,
)
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.is_empty_predicate import IsEmptyPredicate, IsNotEmptyPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
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
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import InPredicate, NotInPredicate
from predicate.standard_predicates import AnyPredicate, has_key_p
from predicate.tuple_of_predicate import TupleOfPredicate


@singledispatch
def generate_false[T](_predicate: Predicate[T]) -> Iterator[T]:
    """Generate values that don't satisfy this predicate."""
    raise ValueError("Please register generator for correct predicate type")


@generate_false.register
def generate_all_p(all_predicate: AllPredicate) -> Iterator:
    predicate = all_predicate.predicate

    while True:
        max_length = random.randint(1, 10)

        # TODO: combination of some true values, or just rewrite as any(false)
        values = take(max_length, generate_false(predicate))
        yield random_combination_with_replacement(values, max_length)


@generate_false.register
def generate_any_p(any_predicate: AnyPredicate, min_size: int = 0, max_size: int = 10) -> Iterator:
    predicate = any_predicate.predicate

    while True:
        length = random.randint(min_size, max_size)

        false_values = take(length, generate_false(predicate))

        yield random_permutation(false_values)


@generate_false.register
def generate_and(predicate: AndPredicate) -> Iterator:
    if optimize(predicate) != always_true_p:
        yield from random_first_from_iterables(generate_false(predicate.left), generate_false(predicate.right))


@generate_false.register
def generate_always_true(_predicate: AlwaysTruePredicate) -> Iterator:
    yield from []


@generate_false.register
def generate_eq(predicate: EqPredicate) -> Iterator:
    yield from generate_anys(~predicate)


@generate_false.register
def generate_always_false(_predicate: AlwaysFalsePredicate) -> Iterator:
    yield from random_anys()


@generate_false.register
def generate_has_key(predicate: HasKeyPredicate) -> Iterator:
    without_predicate_key = ~has_key_p(predicate.key)

    yield from (random_dict for random_dict in random_dicts() if without_predicate_key(random_dict))


@generate_false.register
def generate_has_length(predicate: HasLengthPredicate) -> Iterator:
    length = predicate.length
    yield from random_iterables(max_size=length - 1)


@generate_false.register
def generate_ge_le(predicate: GeLePredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            smaller = random_datetimes(upper=lower - timedelta(seconds=1))
            larger = random_datetimes(lower=upper + timedelta(seconds=1))
            yield from interleave(smaller, larger)
        case int(), _:
            smaller = random_ints(lower=lower - 100, upper=lower - 1)
            larger = random_ints(lower=upper + 1, upper=upper + 100)
            yield from interleave(smaller, larger)
        case float(), _:
            smaller = random_floats(lower=lower - 100.0, upper=lower - 0.01)
            larger = random_floats(lower=upper + 0.01, upper=upper + 100.0)
            yield from interleave(smaller, larger)
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_ge_lt(predicate: GeLtPredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            smaller = random_datetimes(upper=lower - timedelta(seconds=1))
            larger = random_datetimes(lower=upper)
            yield from interleave(smaller, larger)
        case int(), _:
            smaller = random_ints(lower=lower - 100, upper=lower - 1)
            larger = random_ints(lower=upper, upper=upper + 100)
            yield from interleave(smaller, larger)
        case float(), _:
            smaller = random_floats(lower=lower - 100.0, upper=lower - 0.01)
            larger = random_floats(lower=upper, upper=upper + 100.0)
            yield from interleave(smaller, larger)
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_gt_le(predicate: GtLePredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            smaller = random_datetimes(upper=lower)
            larger = random_datetimes(lower=upper + timedelta(seconds=1))
            yield from interleave(smaller, larger)
        case int(), _:
            smaller = random_ints(lower=lower - 100, upper=lower)
            larger = random_ints(lower=upper + 1, upper=upper + 100)
            yield from interleave(smaller, larger)
        case float(), _:
            smaller = random_floats(lower=lower - 100.0, upper=lower)
            larger = random_floats(lower=upper + 0.01, upper=upper + 100.0)
            yield from interleave(smaller, larger)
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_gt_lt(predicate: GtLtPredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            smaller = random_datetimes(upper=lower)
            larger = random_datetimes(lower=upper)
            yield from interleave(smaller, larger)
        case int(), _:
            smaller = random_ints(lower=lower - 100, upper=lower)
            larger = random_ints(lower=upper, upper=upper + 100)
            yield from interleave(smaller, larger)
        case float(), _:
            smaller = random_floats(lower=lower - 100.0, upper=lower)
            larger = random_floats(lower=upper, upper=upper + 100.0)
            yield from interleave(smaller, larger)
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_ge(predicate: GePredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(upper=v - timedelta(seconds=1))
        case float():
            yield from random_floats(upper=v - sys.float_info.epsilon)
        case int():
            yield from random_ints(upper=v - 1)
        case str():
            yield from generate_strings(~predicate)
        case UUID():
            yield from generate_uuids(~predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_false.register
def generate_gt(predicate: GtPredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(upper=v)
        case float():
            yield from random_floats(upper=v)
        case int():
            yield from random_ints(upper=v)
        case str():
            yield from generate_strings(~predicate)
        case UUID():
            yield from generate_uuids(~predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_false.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from generate_anys(IsTruthyPredicate())


@generate_false.register
def generate_in(predicate: InPredicate) -> Iterator:
    # TODO: combine with generate_not_in true
    for item in predicate.v:
        match item:
            case int():
                yield from generate_ints(~predicate)
            case str():
                yield from generate_strings(~predicate)


@generate_false.register
def generate_is_empty(_predicate: IsEmptyPredicate) -> Iterator:
    yield from random_iterables(min_size=1)


@generate_false.register
def generate_is_not_empty(_predicate: IsNotEmptyPredicate) -> Iterator:
    yield from random_iterables(max_size=0)


@generate_false.register
def generate_le(predicate: LePredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(lower=predicate.v + timedelta(seconds=1))
        case float():
            yield from random_floats(lower=predicate.v + 0.01)
        case int():
            yield from random_ints(lower=predicate.v + 1)
        case str():
            yield from generate_strings(~predicate)
        case UUID():
            yield from generate_uuids(~predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_false.register
def generate_lt(predicate: LtPredicate) -> Iterator:
    match v := predicate.v:
        case datetime():
            yield from random_datetimes(lower=v)
        case float():
            yield from random_floats(lower=v)
        case int():
            yield from random_ints(lower=v)
        case str():
            yield from generate_strings(~predicate)
        case UUID():
            yield from generate_uuids(~predicate)
        case _:
            raise ValueError(f"Can't generate for type {type(v)}")


@generate_false.register
def generate_ne(predicate: NePredicate) -> Iterator:
    yield from repeat(predicate.v)


@generate_false.register
def generate_none(_predicate: IsNonePredicate) -> Iterator:
    yield from generate_anys(IsNotNonePredicate())


@generate_false.register
def generate_not(predicate: NotPredicate) -> Iterator:
    from predicate import generate_true

    yield from generate_true(predicate.predicate)


@generate_false.register
def generate_not_in(predicate: NotInPredicate) -> Iterator:
    from predicate import generate_true

    yield from generate_true(InPredicate(v=predicate.v))


@generate_false.register
def generate_not_none(_predicate: IsNotNonePredicate) -> Iterator:
    yield None


@generate_false.register
def generate_truthy(_predicate: IsTruthyPredicate) -> Iterator:
    yield from (False, 0, (), "", {})


@generate_false.register
def generate_is_instance_p(predicate: IsInstancePredicate) -> Iterator:
    not_predicate = NotPredicate(predicate=predicate)
    yield from generate_anys(not_predicate)


@generate_false.register
def generate_or(predicate: OrPredicate) -> Iterator:
    iterable_1 = (item for item in generate_false(predicate.left) if not predicate.right(item))
    iterable_2 = (item for item in generate_false(predicate.right) if not predicate.left(item))
    yield from random_first_from_iterables(iterable_1, iterable_2)


@generate_false.register
def generate_dict_of_p(dict_of_predicate: DictOfPredicate) -> Iterator:
    key_value_predicates = dict_of_predicate.key_value_predicates

    # TODO: generate mix of both false (at least 1) and true
    candidates = zip(
        *flatten(((generate_false(key_p), generate_false(value_p)) for key_p, value_p in key_value_predicates)),
        strict=False,
    )

    yield from (dict(chunked(candidate, 2)) for candidate in candidates)


@generate_false.register
def generate_list_of_p(list_of_predicate: ListOfPredicate, *, min_size: int = 1, max_size: int = 10) -> Iterator:
    predicate = list_of_predicate.predicate

    while True:
        length = random.randint(min_size, max_size)
        # TODO: generate mix of both false (at least 1) and true
        yield take(length, generate_false(predicate))


@generate_false.register
def generate_tuple_of_p(tuple_of_predicate: TupleOfPredicate) -> Iterator:
    predicates = tuple_of_predicate.predicates

    # TODO: generate mix of both false (at least 1) and true
    yield from zip(*(generate_false(predicate) for predicate in predicates), strict=False)


@generate_false.register
def generate_set_of_p(set_of_predicate: SetOfPredicate) -> Iterator:
    predicate = set_of_predicate.predicate

    values = take(10, generate_false(predicate))

    yield set(random_combination_with_replacement(values, 5))


@generate_false.register
def generate_xor(predicate: XorPredicate) -> Iterator:
    if optimize(predicate) == always_true_p:
        yield from []
    else:
        from predicate.generator.generate_true import generate_true

        not_right_and_not_left = (item for item in generate_false(predicate.right) if not predicate.left(item))
        if optimize(predicate.left & predicate.right) == always_false_p:
            yield from not_right_and_not_left

        left_and_right = (item for item in generate_true(predicate.left) if predicate.right(item))

        yield from random_first_from_iterables(left_and_right, not_right_and_not_left)
