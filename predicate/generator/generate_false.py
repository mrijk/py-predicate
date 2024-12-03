import random
import sys
import uuid
from collections.abc import Iterator
from datetime import datetime, timedelta
from functools import singledispatch

from more_itertools import random_combination_with_replacement, take

from predicate.all_predicate import AllPredicate
from predicate.generator.helpers import (
    generate_anys,
    generate_ints,
    generate_strings,
    generate_uuids,
    random_anys,
    random_floats,
    random_ints,
)
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    IsEmptyPredicate,
    IsFalsyPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    IsTruthyPredicate,
    NePredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    always_true_p,
)
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import InPredicate


@singledispatch
def generate_false[T](predicate: Predicate[T]) -> Iterator[T]:
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
def generate_and(predicate: AndPredicate) -> Iterator:
    if optimize(predicate) == always_true_p:
        yield from []
    else:
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
    # TODO: add generic helper function
    yield from ([1], {1, 2, 3}, (1,), "aap")


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
def generate_set_of_p(set_of_predicate: SetOfPredicate) -> Iterator:
    predicate = set_of_predicate.predicate

    values = take(10, generate_false(predicate))

    yield set(random_combination_with_replacement(values, 5))
