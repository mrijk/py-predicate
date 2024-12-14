import random
import sys
import uuid
from collections.abc import Iterator
from datetime import datetime, timedelta
from functools import singledispatch

from more_itertools import chunked, flatten, interleave, random_combination_with_replacement, random_permutation, take

from predicate.all_predicate import AllPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.generator.helpers import (
    generate_anys,
    generate_ints,
    generate_strings,
    generate_uuids,
    random_anys,
    random_dicts,
    random_floats,
    random_ints,
    random_iterables,
)
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.is_empty_predicate import IsEmptyPredicate, IsNotEmptyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.ne_predicate import NePredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    IsFalsyPredicate,
    IsTruthyPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    always_true_p,
)
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import InPredicate
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
        yield from (item for item in generate_false(predicate.left))
        yield from (item for item in generate_false(predicate.right))


@generate_false.register
def generate_always_true(_predicate: AlwaysTruePredicate) -> Iterator:
    yield from []


@generate_false.register
def generate_eq(predicate: EqPredicate) -> Iterator:
    yield from generate_anys(NotPredicate(predicate=predicate))


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
    match predicate.lower:
        case int():
            smaller = random_ints(lower=predicate.lower - 100, upper=predicate.lower - 1)
            greater = random_ints(lower=predicate.upper + 1, upper=predicate.upper + 100)
            yield from interleave(smaller, greater)
        case float():
            smaller = random_floats(lower=predicate.lower - 100.0, upper=predicate.lower - 0.01)
            greater = random_floats(lower=predicate.upper + 0.01, upper=predicate.upper + 100.0)
            yield from interleave(smaller, greater)


@generate_false.register
def generate_ge_lt(predicate: GeLtPredicate) -> Iterator:
    match predicate.lower:
        case int():
            smaller = random_ints(lower=predicate.lower - 100, upper=predicate.lower - 1)
            greater = random_ints(lower=predicate.upper, upper=predicate.upper + 100)
            yield from interleave(smaller, greater)
        case float():
            smaller = random_floats(lower=predicate.lower - 100.0, upper=predicate.lower - 0.01)
            greater = random_floats(lower=predicate.upper, upper=predicate.upper + 100.0)
            yield from interleave(smaller, greater)


@generate_false.register
def generate_gt_le(predicate: GtLePredicate) -> Iterator:
    match predicate.lower:
        case int():
            smaller = random_ints(lower=predicate.lower - 100, upper=predicate.lower)
            greater = random_ints(lower=predicate.upper + 1, upper=predicate.upper + 100)
            yield from interleave(smaller, greater)
        case float():
            smaller = random_floats(lower=predicate.lower - 100.0, upper=predicate.lower)
            greater = random_floats(lower=predicate.upper + 0.01, upper=predicate.upper + 100.0)
            yield from interleave(smaller, greater)


@generate_false.register
def generate_gt_lt(predicate: GtLtPredicate) -> Iterator:
    match predicate.lower:
        case int():
            smaller = random_ints(lower=predicate.lower - 100, upper=predicate.lower)
            greater = random_ints(lower=predicate.upper, upper=predicate.upper + 100)
            yield from interleave(smaller, greater)
        case float():
            smaller = random_floats(lower=predicate.lower - 100.0, upper=predicate.lower)
            greater = random_floats(lower=predicate.upper, upper=predicate.upper + 100.0)
            yield from interleave(smaller, greater)


@generate_false.register
def generate_ge(predicate: GePredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt - timedelta(days=days) for days in range(1, 6))
        case float():
            yield from random_floats(upper=predicate.v - sys.float_info.epsilon)
        case int():
            yield from random_ints(upper=predicate.v - 1)
        case str():
            yield from generate_strings(NotPredicate(predicate=predicate))
        case uuid.UUID():
            yield from generate_uuids(NotPredicate(predicate=predicate))


@generate_false.register
def generate_gt(predicate: GtPredicate) -> Iterator:
    match predicate.v:
        case datetime() as dt:
            yield from (dt - timedelta(days=days) for days in range(0, 5))
        case float():
            yield from random_floats(upper=predicate.v)
        case int():
            yield from random_ints(upper=predicate.v)
        case str():
            yield from generate_strings(NotPredicate(predicate=predicate))
        case uuid.UUID():
            yield from generate_uuids(NotPredicate(predicate=predicate))


@generate_false.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from generate_anys(IsTruthyPredicate())


@generate_false.register
def generate_in(predicate: InPredicate) -> Iterator:
    # TODO: combine with generate_not_in true
    for item in predicate.v:
        match item:
            case int():
                yield from generate_ints(NotPredicate(predicate=predicate))
            case str():
                yield from generate_strings(NotPredicate(predicate=predicate))


@generate_false.register
def generate_is_empty(_predicate: IsEmptyPredicate) -> Iterator:
    yield from random_iterables(min_size=1)


@generate_false.register
def generate_is_not_empty(_predicate: IsNotEmptyPredicate) -> Iterator:
    yield from random_iterables(max_size=0)


@generate_false.register
def generate_ne(predicate: NePredicate) -> Iterator:
    yield from predicate.v


@generate_false.register
def generate_none(_predicate: IsNonePredicate) -> Iterator:
    yield from generate_anys(IsNotNonePredicate())


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
    yield from (item for item in generate_false(predicate.left) if not predicate.right(item))
    yield from (item for item in generate_false(predicate.right) if not predicate.left(item))


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
