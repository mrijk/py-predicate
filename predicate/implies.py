from functools import singledispatch

from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    NePredicate,
    Predicate,
)
from predicate.set_predicates import (
    InPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
    NotInPredicate,
)


@singledispatch
def implies(predicate: Predicate, other: Predicate) -> bool:
    """Return True if predicate implies another predicate, otherwise False."""
    return False


@implies.register
def _(_predicate: AlwaysFalsePredicate, _other: Predicate) -> bool:
    return True


@implies.register
def _(_predicate: AlwaysTruePredicate, other: Predicate) -> bool:
    return other == AlwaysTruePredicate()


@implies.register
def _(predicate: AndPredicate, other: Predicate) -> bool:
    return other == predicate.left or other == predicate.right


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
def _(predicate: GtPredicate, other: Predicate) -> bool:
    match other:
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v >= v
        case _:
            return False


@implies.register
def _(predicate: EqPredicate, other: Predicate) -> bool:
    match other:
        case EqPredicate(v):
            return predicate.v == v
        case NePredicate(v):
            return predicate.v != v
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v > v
        case InPredicate(v):
            return predicate.v in v
        case NotInPredicate(v):
            return predicate.v not in v
        case _:
            return False


@implies.register
def _(predicate: IsRealSubsetPredicate, other: Predicate) -> bool:
    match other:
        case IsSubsetPredicate(v):
            return predicate.v == v
        case _:
            return False


@implies.register
def _(predicate: IsRealSupersetPredicate, other: Predicate) -> bool:
    match other:
        case IsSupersetPredicate(v):
            return predicate.v == v
        case _:
            return False


@implies.register
def _(predicate: InPredicate, other: Predicate) -> bool:
    match other:
        case InPredicate(v):
            return predicate.v.issubset(v)
        case _:
            return False
