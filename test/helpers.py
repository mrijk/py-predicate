from types import FunctionType

from predicate import exercise, is_instance_p
from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.eq_predicate import EqPredicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    XorPredicate,
)

is_all_p = is_instance_p(AllPredicate)
is_and_p = is_instance_p(AndPredicate)
is_not_p = is_instance_p(NotPredicate)
is_or_p = is_instance_p(OrPredicate)
is_xor_p = is_instance_p(XorPredicate)
is_false_p = is_instance_p(AlwaysFalsePredicate)
is_true_p = is_instance_p(AlwaysTruePredicate)
is_eq_p = is_instance_p(EqPredicate)


def exercise_class(predicate):
    data = list(exercise(predicate))
    assert data

    for param, result in data:
        assert predicate(*param) == result


def exercise_function(predicate_f):
    predicates = list(exercise(predicate_f))
    assert predicates

    for _, predicate in predicates:
        exercise_class(predicate)


def exercise_predicate(predicate_f):
    if isinstance(predicate_f, FunctionType):
        exercise_function(predicate_f)
    elif callable(predicate_f):
        exercise_class(predicate_f)
