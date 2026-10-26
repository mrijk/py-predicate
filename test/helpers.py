from types import FunctionType

from predicate import exercise, is_instance_p
from predicate.and_predicate import AndPredicate
from predicate.eq_predicate import EqPredicate
from predicate.not_predicate import NotPredicate

is_and_p = is_instance_p(AndPredicate)
is_not_p = is_instance_p(NotPredicate)
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
