import random
import sys
from collections.abc import Iterable, Iterator
from datetime import datetime, timedelta
from functools import singledispatch
from itertools import cycle, repeat
from types import UnionType
from typing import Final, get_args
from uuid import UUID

from more_itertools import first, flatten, interleave, random_permutation, take

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.count_predicate import CountPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.exactly_predicate import ExactlyPredicate
from predicate.fn_predicate import FnPredicate
from predicate.ge_predicate import GePredicate
from predicate.generator.helpers import (
    default_size_p,
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
    random_lambdas,
    random_non_hashables,
    random_sets,
    random_strings,
    random_values_of_type,
    sample_optional_fields,
)
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate, has_key_p
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
from predicate.is_subclass_predicate import IsSubclassPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.juxt_predicate import JuxtPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate, is_list_of_p
from predicate.lt_predicate import LtPredicate
from predicate.match_predicate import (
    MatchPredicate,
)
from predicate.ne_predicate import NePredicate, ne_p
from predicate.not_in_predicate import NotInPredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.optional_predicate import OptionalPredicate
from predicate.plus_predicate import PlusPredicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate, XorPredicate
from predicate.raises_predicate import RaisesPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate, ge_le_p
from predicate.reduce_predicate import ReducePredicate
from predicate.regex_predicate import RegexPredicate
from predicate.repeat_predicate import RepeatPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import IsRealSubsetPredicate, IsSubsetPredicate
from predicate.standard_predicates import is_int_p
from predicate.star_predicate import StarPredicate
from predicate.struct_predicate import StructPredicate
from predicate.tee_predicate import TeePredicate
from predicate.tuple_of_predicate import TupleOfPredicate

default_at_least_one_length_p: Final = ge_le_p(lower=1, upper=10)


@singledispatch
def generate_false[T](predicate: Predicate[T], **kwargs) -> Iterator[T]:
    """Generate values that don't satisfy this predicate."""
    raise ValueError(f"Please register generator for correct predicate type: {predicate!r}")


@generate_false.register
def generate_all_p(all_predicate: AllPredicate, *, length_p: Predicate = default_at_least_one_length_p) -> Iterator:
    predicate = all_predicate.predicate

    while True:
        yield generate_at_least_one_false(predicate, length_p=length_p)


@generate_false.register
def generate_any_p(any_predicate: AnyPredicate, length_p: Predicate = default_size_p) -> Iterator:
    predicate = any_predicate.predicate
    from predicate import generate_true

    valid_lengths = generate_true(length_p)

    while True:
        length = next(valid_lengths)

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
    yield from (value for value in random_values_of_type(klass=predicate.klass) if not predicate(value))


@generate_false.register
def generate_always_false(_predicate: AlwaysFalsePredicate) -> Iterator:
    yield from random_anys()


@generate_false.register
def generate_is_close_p(predicate: IsClosePredicate) -> Iterator:
    yield from (v for v in random_floats() if not predicate(v))


@generate_false.register
def generate_has_key(predicate: HasKeyPredicate) -> Iterator:
    without_predicate_key = ~has_key_p(predicate.key)

    yield from (random_dict for random_dict in random_dicts() if without_predicate_key(random_dict))


@generate_false.register
def generate_has_length(predicate: HasLengthPredicate, *, value_p=is_int_p) -> Iterator:
    yield from random_iterables(length_p=~predicate.length_p, value_p=value_p)


@generate_false.register
def generate_has_path(predicate: HasPathPredicate) -> Iterator:
    from predicate import generate_true

    yield {}

    path = predicate.path
    root_p = path[0]
    rest_path = path[1:]

    if rest_path:
        valid_keys = generate_true(root_p)
        false_rest_values: Iterator = generate_false(HasPathPredicate(path=rest_path))
        while True:
            yield {next(valid_keys): next(false_rest_values)}
    else:
        false_keys = generate_false(root_p)
        while True:
            yield {next(false_keys): None}


@generate_false.register
def generate_ge_le(predicate: GeLePredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from interleave(
                random_datetimes(upper=lower - timedelta(seconds=1)),
                random_datetimes(lower=upper + timedelta(seconds=1)),
            )
        case int(), _:
            yield from interleave(
                random_ints(lower=lower - 100, upper=lower - 1),
                random_ints(lower=upper + 1, upper=upper + 100),
            )
        case float(), _:
            yield from interleave(
                random_floats(lower=lower - 100.0, upper=lower - 0.01),
                random_floats(lower=upper + 0.01, upper=upper + 100.0),
            )
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_ge_lt(predicate: GeLtPredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from interleave(
                random_datetimes(upper=lower - timedelta(seconds=1)),
                random_datetimes(lower=upper),
            )
        case int(), _:
            yield from interleave(
                random_ints(lower=lower - 100, upper=lower - 1),
                random_ints(lower=upper, upper=upper + 100),
            )
        case float(), _:
            yield from interleave(
                random_floats(lower=lower - 100.0, upper=lower - 0.01),
                random_floats(lower=upper, upper=upper + 100.0),
            )
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_gt_le(predicate: GtLePredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from interleave(
                random_datetimes(upper=lower),
                random_datetimes(lower=upper + timedelta(seconds=1)),
            )
        case int(), _:
            yield from interleave(
                random_ints(lower=lower - 100, upper=lower),
                random_ints(lower=upper + 1, upper=upper + 100),
            )
        case float(), _:
            yield from interleave(
                random_floats(lower=lower - 100.0, upper=lower),
                random_floats(lower=upper + 0.01, upper=upper + 100.0),
            )
        case _:
            raise ValueError(f"Can't generate for type {type(lower)}")


@generate_false.register
def generate_gt_lt(predicate: GtLtPredicate) -> Iterator:
    match lower := predicate.lower, upper := predicate.upper:
        case datetime(), _:
            yield from interleave(
                random_datetimes(upper=lower),
                random_datetimes(lower=upper),
            )
        case int(), _:
            yield from interleave(
                random_ints(lower=lower - 100, upper=lower),
                random_ints(lower=upper, upper=upper + 100),
            )
        case float(), _:
            yield from interleave(
                random_floats(lower=lower - 100.0, upper=lower),
                random_floats(lower=upper, upper=upper + 100.0),
            )
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
def generate_fn_p(predicate: FnPredicate) -> Iterator:
    yield from predicate.generate_false_fn()


@generate_false.register
def generate_in(predicate: InPredicate) -> Iterator:
    # TODO: combine with generate_not_in true
    if isinstance(predicate.v, Iterable):
        for item in predicate.v:
            match item:
                case int():
                    yield from generate_ints(~predicate)
                case str():
                    yield from generate_strings(~predicate)


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
    yield from cycle((False, 0, (), "", {}))


@generate_false.register
def generate_is_instance_p(predicate: IsInstancePredicate) -> Iterator:
    from typing import Hashable

    if predicate.instance_klass[0] is Hashable:
        yield from random_non_hashables()
        return
    not_predicate = NotPredicate(predicate=predicate)
    yield from generate_anys(not_predicate)


@generate_false.register
def generate_is_async_p(predicate: IsAsyncPredicate) -> Iterator:
    yield from random_lambdas()


@generate_false.register
def generate_is_lambda_p(predicate: IsLambdaPredicate) -> Iterator:
    if (nr_of_parameters := predicate.nr_of_parameters) is None:
        not_predicate = NotPredicate(predicate=predicate)
        yield from generate_anys(not_predicate)
    else:
        lower = 0
        upper = min(5, 2 * nr_of_parameters)
        nr_of_parameters_p = ge_le_p(lower=lower, upper=upper) & ne_p(nr_of_parameters)
        yield from random_lambdas(nr_of_parameters_p=nr_of_parameters_p)


@generate_false.register
def generate_or(predicate: OrPredicate) -> Iterator:
    attempts = 100
    _sentinel = object()

    first_left = next(
        (item for item in take(attempts, generate_false(predicate.left)) if not predicate.right(item)), _sentinel
    )
    first_right = next(
        (item for item in take(attempts, generate_false(predicate.right)) if not predicate.left(item)), _sentinel
    )

    iterables = []
    if first_left is not _sentinel:
        iterables.append(item for item in generate_false(predicate.left) if not predicate.right(item))
    if first_right is not _sentinel:
        iterables.append(item for item in generate_false(predicate.right) if not predicate.left(item))

    if not iterables:
        raise ValueError(f"Couldn't generate values that satisfy {predicate}")

    yield from random_first_from_iterables(*iterables)


@generate_false.register
def generate_dict_of_p(dict_of_predicate: DictOfPredicate) -> Iterator:
    from predicate import generate_true

    key_value_predicates = dict_of_predicate.key_value_predicates
    length = len(key_value_predicates)
    max_number = 2**length - 1
    generators = [
        ((generate_false(key_p), generate_false(value_p)), (generate_true(key_p), generate_true(value_p)))
        for key_p, value_p in key_value_predicates
    ]

    while True:
        n = random.randint(1, max_number)
        values = take(length, bool_array_from_int(n))
        yield {
            next(key_gen): next(val_gen)
            for (false_gens, true_gens), use_true in zip(generators, values, strict=False)
            for key_gen, val_gen in [true_gens if use_true else false_gens]
        }


@generate_false.register
def generate_list_of_p(
    list_of_predicate: ListOfPredicate, *, length_p: Predicate = default_at_least_one_length_p
) -> Iterator:
    predicate = list_of_predicate.predicate

    while True:
        yield list(generate_at_least_one_false(predicate, length_p=length_p))


def bool_array_from_int(n: int) -> Iterable[bool]:
    while n:
        yield n % 2 == 0
        n >>= 1
    while True:
        yield True


@generate_false.register
def generate_tuple_of_p(tuple_of_predicate: TupleOfPredicate) -> Iterator:
    from predicate import generate_true

    predicates = tuple_of_predicate.predicates

    length = len(predicates)
    max_number = 2**length - 1
    generators = [(generate_false(predicate), generate_true(predicate)) for predicate in predicates]

    while True:
        n = random.randint(1, max_number)
        values = take(length, (bool_array_from_int(n)))
        yield tuple(next(generator[value]) for generator, value in zip(generators, values, strict=False))


@generate_false.register
def generate_set_of_p(
    set_of_predicate: SetOfPredicate, *, length_p: Predicate = default_at_least_one_length_p
) -> Iterator:
    predicate = set_of_predicate.predicate

    while True:
        result = set(generate_at_least_one_false(predicate, length_p=length_p))
        # This check is needed because {False, 0} and {True, 1} result in {False} and {True}
        if not set_of_predicate(result):
            yield result


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


def generate_at_least_one_false(predicate: Predicate, *, length_p: Predicate = default_at_least_one_length_p) -> tuple:
    from predicate import generate_true

    length = max(first(generate_true(length_p)), 1)

    nr_false_values = random.randint(1, length) if length > 1 else 1
    nr_true_values = length - nr_false_values

    false_values = take(nr_false_values, generate_false(predicate))
    true_values = take(nr_true_values, generate_true(predicate))

    combined_values = false_values + true_values

    return random_permutation(combined_values)


@generate_false.register
def generate_juxt_p(predicate: JuxtPredicate) -> Iterator:
    yield from (item for item in random_anys() if not predicate(item))


@generate_false.register
def generate_tee(_predicate: TeePredicate) -> Iterator:
    yield from []


@generate_false.register
def generate_match_p(match_predicate: MatchPredicate) -> Iterator:
    predicates = match_predicate.predicates

    predicate, *rest_predicates = predicates

    match predicate:
        case OptionalPredicate() | PlusPredicate() | StarPredicate() | ExactlyPredicate() | RepeatPredicate():
            yield from generate_false(predicate, predicates=rest_predicates)
        case Predicate():
            if rest_predicates:
                iter_first = generate_false(predicate)
                iter_rest: Iterator = generate_false(MatchPredicate(predicates=rest_predicates))
                while True:
                    yield [next(iter_first)] + list(next(iter_rest))
            else:
                yield from zip(generate_false(predicate), strict=False)


@generate_false.register
def generate_exactly_n(exactly_predicate: ExactlyPredicate, *, predicates: list[Predicate]) -> Iterator:
    predicate = exactly_predicate.predicate

    list_of_predicate = is_list_of_p(predicate=predicate)

    n = exactly_predicate.n
    length_p = ne_p(n)

    if predicates:
        iter_first = generate_false(list_of_predicate, length_p=length_p)
        iter_rest: Iterator = generate_false(MatchPredicate(predicates=predicates))
        while True:
            yield list(next(iter_first)) + list(next(iter_rest))
    else:
        yield from generate_false(list_of_predicate, length_p=length_p)


@generate_false.register
def generate_count(count_predicate: CountPredicate) -> Iterator:
    predicate = count_predicate.predicate
    length_p = count_predicate.length_p

    # TODO: this is a minimal set. Also create iterables that contains some false items (which are not counted)
    yield from generate_all_p(AllPredicate(predicate=predicate), length_p=length_p)


def _subclasses(klass: type) -> set:
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return set(klass.__subclasses__())


@generate_false.register
def generate_is_subclass(is_subclass_predicate: IsSubclassPredicate) -> Iterator:
    all_sub_classes = _subclasses(object)

    match is_subclass_predicate.class_or_tuple:
        case tuple(klasses):
            subclasses = set(flatten(_subclasses(klass) for klass in klasses))
            if non_subclasses := all_sub_classes - subclasses:
                while True:
                    yield from non_subclasses
        case UnionType() as union_type:
            subclasses = set(flatten(_subclasses(klass) for klass in get_args(union_type)))
            if non_subclasses := all_sub_classes - subclasses:
                while True:
                    yield from non_subclasses
        case _ as klass:
            subclasses = _subclasses(klass)
            if non_subclasses := all_sub_classes - subclasses:
                while True:
                    yield from non_subclasses


@generate_false.register
def generate_is(is_predicate: IsPredicate) -> Iterator:
    singletons = (True, False, None, Ellipsis, (), NotImplemented)
    selection = [v for v in singletons if v is not is_predicate.v]

    yield from cycle(selection)


@generate_false.register
def generate_is_subset(predicate: IsSubsetPredicate) -> Iterator:
    yield from (s for s in random_sets() if not predicate(s))


@generate_false.register
def generate_is_real_subset(predicate: IsRealSubsetPredicate) -> Iterator:
    yield predicate.v  # v is not a real subset of itself
    yield from (s for s in random_sets() if not predicate(s))


@generate_false.register
def generate_reduce_p(predicate: ReducePredicate) -> Iterator:
    return
    yield


@generate_false.register
def generate_regex(predicate: RegexPredicate) -> Iterator:
    yield from (s for s in random_strings() if not predicate(s))


@generate_false.register
def generate_is_callable(predicate: IsCallablePredicate) -> Iterator:
    yield from (item for item in random_anys() if not predicate(item))


@generate_false.register
def generate_raises(predicate: RaisesPredicate) -> Iterator:
    yield from repeat(lambda: None)


@generate_false.register
def generate_struct(predicate: StructPredicate) -> Iterator:
    from predicate import generate_true

    required = predicate.required
    optional = predicate.optional

    known_keys = set(required) | set(optional)
    dict_of_predicate = DictOfPredicate(key_value_predicates=list(required.items()))

    def false_required_fields() -> Iterator:
        optional_generators = {key: generate_false(value_p) for key, value_p in optional.items()}
        for false_dict in generate_dict_of_p(dict_of_predicate):
            yield false_dict | sample_optional_fields(optional, optional_generators)

    def extra_key_dicts() -> Iterator:
        required_true_generators = {key: generate_true(value_p) for key, value_p in required.items()}
        optional_true_generators = {key: generate_true(value_p) for key, value_p in optional.items()}
        for extra_key in (key for key in random_strings(min_size=1) if key not in known_keys):
            required_fields = {key: next(required_true_generators[key]) for key in required}
            yield required_fields | sample_optional_fields(optional, optional_true_generators) | {extra_key: None}

    yield from random_first_from_iterables(false_required_fields(), extra_key_dicts())
