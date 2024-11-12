from functools import singledispatch

from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    Predicate,
)


@singledispatch
def implies(predicate: Predicate, other: Predicate) -> bool:
    """Return True if predicate implies another predicate, otherwise False."""
    return False


@implies.register
def implies_false(_predicate: AlwaysFalsePredicate, _other: Predicate) -> bool:
    return True


@implies.register
def implies_true(_predicate: AlwaysTruePredicate, other: Predicate) -> bool:
    return other == AlwaysTruePredicate()


@implies.register
def _(predicate: GePredicate, other: Predicate) -> bool:
    match other:
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v > v
        case _:
            return False


@implies.register
def _(predicate: EqPredicate, other: Predicate) -> bool:
    match other:
        case EqPredicate(v):
            return predicate.v == v
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v > v
        case InPredicate(v):
            return predicate.v in v
        case _:
            return False
