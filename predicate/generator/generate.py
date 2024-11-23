import math
import uuid
from collections.abc import Iterator
from datetime import datetime
from functools import singledispatch

from more_itertools import interleave, random_combination_with_replacement, repeatfunc, take

from predicate import AllPredicate, IsNonePredicate, is_int_p, is_str_p
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AnyPredicate,
    EqPredicate,
    InPredicate,
    IsFalsyPredicate,
    IsInstancePredicate,
    IsNotNonePredicate,
    IsTruthyPredicate,
    NePredicate,
    NotInPredicate,
    OrPredicate,
    Predicate,
)


@singledispatch
def generate[T](predicate: Predicate[T]) -> Iterator[T]:
    """Generate values that satisfy this predicate."""
    raise ValueError("Please register generator for correct predicate type.")


@generate.register
def generate_eq(predicate: EqPredicate) -> Iterator:
    yield predicate.v


@generate.register
def generate_false(_predicate: AlwaysFalsePredicate) -> Iterator:
    pass


@generate.register
def generate_in(predicate: InPredicate) -> Iterator:
    yield from predicate.v


@generate.register
def generate_ne(predicate: NePredicate) -> Iterator:
    yield not predicate.v


@generate.register
def generate_none(_predicate: IsNonePredicate) -> Iterator:
    yield None


@generate.register
def generate_not_in(predicate: NotInPredicate) -> Iterator:
    for item in predicate.v:
        match item:
            case int():
                yield from (item for item in generate(is_int_p) if predicate(item))
            case str():
                yield from (item for item in generate(is_str_p) if predicate(item))


@generate.register
def generate_not_none(_predicate: IsNotNonePredicate) -> Iterator:
    yield from ("foo", 3.14, 42)


@generate.register
def generate_or(predicate: OrPredicate) -> Iterator:
    yield from interleave(generate(predicate.left), generate(predicate.right))


@generate.register
def generate_true(_predicate: AlwaysTruePredicate) -> Iterator:
    yield True


@generate.register
def generate_falsy(_predicate: IsFalsyPredicate) -> Iterator:
    yield from (False, 0, (), "", {})


@generate.register
def generate_truthy(_predicate: IsTruthyPredicate) -> Iterator:
    yield from (True, 1, "true", {1}, 3.14)


@generate.register
def generate_is_instance_p(predicate: IsInstancePredicate) -> Iterator:
    klass = predicate.klass[0]
    if klass is str:
        yield from ("", "0", "foobar", "\n")
    elif klass is bool:
        yield from (False, True)
    elif klass is complex:
        yield from (complex(1, 1),)
    elif klass == datetime:
        yield from (datetime.now(),)
    elif klass is float:
        yield from (math.pi, math.e)
    elif klass == uuid.UUID:
        yield from repeatfunc(uuid.uuid4, times=10)
    elif klass is int:
        yield from (-1, 0, 1)


@generate.register
def generate_all_p(all_predicate: AllPredicate) -> Iterator:
    yield []

    predicate = all_predicate.predicate
    values = take(10, generate(predicate))

    yield random_combination_with_replacement(values, 5)

    yield set(random_combination_with_replacement(values, 5))


@generate.register
def generate_any_p(any_predicate: AnyPredicate) -> Iterator:
    predicate = any_predicate.predicate
    values = take(10, generate(predicate))

    # TODO: also add some values for which predicate isn't valid

    yield random_combination_with_replacement(values, 5)

    yield set(random_combination_with_replacement(values, 5))
