from itertools import repeat
from typing import Any, Iterator

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import always_false_p
from predicate.always_true_predicate import always_true_p
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.in_predicate import InPredicate
from predicate.is_async_predicate import is_async_p
from predicate.is_falsy_predicate import is_falsy_p
from predicate.is_instance_predicate import is_instance_p
from predicate.is_lambda_predicate import is_lambda_p
from predicate.is_named_tuple_predicate import is_named_tuple_p
from predicate.is_none_predicate import is_none_p
from predicate.is_not_none_predicate import is_not_none_p
from predicate.is_regex_predicate import is_regex_p
from predicate.is_truthy_predicate import is_truthy_p
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.not_predicate import NotPredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.xor_predicate import XorPredicate


def generate_predicate(predicate_type: type[Predicate], max_depth: int, klass: type) -> Iterator[Predicate]:
    if generator := predicate_type_registry().get(predicate_type):
        yield from generator(max_depth=max_depth, klass=klass)
    else:
        raise ValueError(f"No generator found for {predicate_type}")


def predicate_type_registry() -> dict[type, Any]:
    return typed_predicate_type_registry() | {
        type(predicate): _constant_predicates(predicate) for predicate in _constant_predicate_instances
    }


def typed_predicate_type_registry() -> dict[type, Any]:
    """Return the generators for predicates over values of a given klass; random_predicates combines these."""
    return {
        # TODO: AllPredicate works on iterables
        AllPredicate: generate_all_predicates,
        AndPredicate: generate_and_predicates,
        AnyPredicate: generate_any_predicates,
        EqPredicate: generate_eq_predicates,
        GeLePredicate: generate_ge_le_predicates,
        GeLtPredicate: generate_ge_lt_predicates,
        GePredicate: generate_ge_predicates,
        GtPredicate: generate_gt_predicates,
        GtLePredicate: generate_gt_le_predicates,
        GtLtPredicate: generate_gt_lt_predicates,
        InPredicate: generate_in_predicates,
        LePredicate: generate_le_predicates,
        LtPredicate: generate_lt_predicates,
        NePredicate: generate_ne_predicates,
        NotInPredicate: generate_not_in_predicates,
        NotPredicate: generate_not_predicates,
        OrPredicate: generate_or_predicates,
        XorPredicate: generate_xor_predicates,
    }


# Predicates without parameters: the module-level instance is the only value there is
_constant_predicate_instances: list[Predicate] = [
    always_false_p,
    always_true_p,
    is_async_p,
    is_falsy_p,
    is_lambda_p,
    is_named_tuple_p,
    is_none_p,
    is_not_none_p,
    is_regex_p,
    is_truthy_p,
]


def _constant_predicates(predicate: Predicate) -> Any:
    return lambda max_depth, klass: repeat(predicate)


def generate_random_predicate_pairs(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_predicates

    left_predicates = random_predicates(max_depth=max_depth - 1, klass=klass)
    right_predicates = random_predicates(max_depth=max_depth - 1, klass=klass)

    return zip(left_predicates, right_predicates, strict=False)


def generate_all_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1, klass=klass)

    yield from (AllPredicate(predicate) for predicate in predicates)


def generate_any_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1, klass=klass)

    yield from (AnyPredicate(predicate) for predicate in predicates)


def generate_set_of_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1, klass=klass)

    yield from (SetOfPredicate(predicate) for predicate in predicates)


def generate_and_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    yield from (left & right for left, right in generate_random_predicate_pairs(max_depth=max_depth, klass=klass))


def generate_eq_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_values_of_type

    yield from (EqPredicate(value) for value in random_values_of_type(klass))


def generate_ge_le_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_pairs_of_type

    yield from (GeLePredicate(lower=lower, upper=upper) for lower, upper in random_constrained_pairs_of_type(klass))


def generate_ge_lt_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_pairs_of_type

    yield from (GeLtPredicate(lower=lower, upper=upper) for lower, upper in random_constrained_pairs_of_type(klass))


def generate_gt_le_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_pairs_of_type

    yield from (GtLePredicate(lower=lower, upper=upper) for lower, upper in random_constrained_pairs_of_type(klass))


def generate_gt_lt_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_pairs_of_type

    yield from (GtLtPredicate(lower=lower, upper=upper) for lower, upper in random_constrained_pairs_of_type(klass))


def generate_ge_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_values_of_type

    yield from (GePredicate(value) for value in random_constrained_values_of_type(klass))


def generate_gt_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_values_of_type

    yield from (GtPredicate(value) for value in random_constrained_values_of_type(klass))


def generate_in_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_iterables

    yield from (InPredicate(set(iterable)) for iterable in random_iterables(value_p=is_instance_p(klass)))


def generate_not_in_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate import is_instance_p
    from predicate.generator.helpers import random_iterables

    yield from (NotInPredicate(set(iterable)) for iterable in random_iterables(value_p=is_instance_p(klass)))


def generate_le_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_values_of_type

    yield from (LePredicate(value) for value in random_constrained_values_of_type(klass))


def generate_lt_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_constrained_values_of_type

    yield from (LtPredicate(value) for value in random_constrained_values_of_type(klass))


def generate_ne_predicates(max_depth: int, klass: type) -> Iterator:
    from predicate.generator.helpers import random_values_of_type

    yield from (NePredicate(value) for value in random_values_of_type(klass))


def generate_not_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    from predicate.generator.helpers import random_predicates

    predicates = random_predicates(max_depth=max_depth - 1, klass=klass)
    yield from (~predicate for predicate in predicates)


def generate_or_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    yield from (left | right for left, right in generate_random_predicate_pairs(max_depth=max_depth, klass=klass))


def generate_xor_predicates(max_depth: int, klass: type) -> Iterator:
    if not max_depth:
        return

    yield from (left ^ right for left, right in generate_random_predicate_pairs(max_depth=max_depth, klass=klass))
