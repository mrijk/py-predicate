from dataclasses import dataclass
from functools import singledispatch
from typing import Any, Iterable, override

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.and_predicate import AndPredicate
from predicate.eq_predicate import EqPredicate
from predicate.frozenset_of_predicate import FrozenSetOfPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.in_predicate import InPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import (
    IntersectsPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)


@singledispatch
def implies(predicate: Predicate[Any], other: Predicate[Any]) -> bool:
    """Return True if predicate implies another predicate, otherwise False."""
    if predicate == other:
        return True
    if isinstance(other, AndPredicate):
        return implies(predicate, other.left) and implies(predicate, other.right)
    if isinstance(other, OrPredicate):
        return implies(predicate, other.left) or implies(predicate, other.right)
    return False


@implies.register
def _(_predicate: AlwaysFalsePredicate, _other: Predicate[Any]) -> bool:
    return True


@implies.register
def _(_predicate: AlwaysTruePredicate, other: Predicate[Any]) -> bool:
    return other == AlwaysTruePredicate()


@implies.register(AndPredicate)
def _(predicate: AndPredicate[Any], other: Predicate[Any]) -> bool:
    if predicate == other:
        return True
    if isinstance(other, AndPredicate):
        # p => (q & r) when p => q and p => r, e.g. a spec that narrows one part of an annotation (#306)
        return implies(predicate, other.left) and implies(predicate, other.right)
    return implies(predicate.left, other) or implies(predicate.right, other)


@implies.register(GePredicate)
def _(predicate: GePredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v > v
        case NePredicate(v):
            return predicate.v > v
        case _:
            return False


@implies.register(GtPredicate)
def _(predicate: GtPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IsInstancePredicate(instance_klass):
            return predicate.klass == instance_klass[0]  # type: ignore
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v >= v
        case NePredicate(v):
            return predicate.v >= v
        case _:
            return False


@implies.register(LePredicate)
def _(predicate: LePredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case LePredicate(v):
            return predicate.v <= v
        case LtPredicate(v):
            return predicate.v < v
        case NePredicate(v):
            return predicate.v < v
        case _:
            return False


@implies.register(LtPredicate)
def _(predicate: LtPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case LePredicate(v):
            return predicate.v <= v
        case LtPredicate(v):
            return predicate.v <= v
        case NePredicate(v):
            return predicate.v <= v
        case _:
            return False


@implies.register(EqPredicate)
def _(predicate: EqPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IsInstancePredicate(instance_klass):
            return predicate.klass == instance_klass[0]  # type: ignore
        case EqPredicate(v):
            return predicate.v == v
        case NePredicate(v):
            return predicate.v != v
        case GePredicate(v):
            return predicate.v >= v
        case GtPredicate(v):
            return predicate.v > v
        case LePredicate(v):
            return predicate.v <= v
        case LtPredicate(v):
            return predicate.v < v
        case InPredicate(v):
            return predicate.v in v
        case NotInPredicate(v):
            return predicate.v not in v
        case _:
            return False


@implies.register(IsRealSubsetPredicate)
def _(predicate: IsRealSubsetPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IsSubsetPredicate(v):
            return predicate.v <= v
        case _:
            return False


@implies.register(IsRealSupersetPredicate)
def _(predicate: IsRealSupersetPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IsSupersetPredicate(v):
            return v <= predicate.v
        case IntersectsPredicate(v) if predicate.v & v:
            return True
        case _:
            return False


@implies.register(IsSupersetPredicate)
def _(predicate: IsSupersetPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IntersectsPredicate(v) if predicate.v & v:
            return True
        case _:
            return False


@implies.register(IntersectsPredicate)
def _(predicate: IntersectsPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IntersectsPredicate(v):
            return predicate.v <= v
        case _:
            return False


@implies.register(InPredicate)
def _(predicate: InPredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case InPredicate(v) if isinstance(v, Iterable) and isinstance(predicate.v, Iterable):
            return set(predicate.v).issubset(v)
        case _:
            return False


@implies.register(IsInstancePredicate)
def _(predicate: IsInstancePredicate[Any], other: Predicate[Any]) -> bool:
    match other:
        case IsInstancePredicate(instance_klass):
            return set(predicate.instance_klass) <= set(instance_klass)
        case OrPredicate(left, right):
            return implies(predicate, left) or implies(predicate, right)
        case _:
            return False


@implies.register(OrPredicate)
def _(predicate: OrPredicate[Any], other: Predicate[Any]) -> bool:
    return predicate == other or (implies(predicate.left, other) and implies(predicate.right, other))


@implies.register(AllPredicate)
@implies.register(ListOfPredicate)
@implies.register(SetOfPredicate)
@implies.register(FrozenSetOfPredicate)
def _(predicate: Predicate[Any], other: Predicate[Any]) -> bool:
    # Element-wise predicates of the same kind: implied when the element predicate is implied
    return type(predicate) is type(other) and implies(predicate.predicate, other.predicate)  # type: ignore


@dataclass
class Implies[T](Predicate[T]):
    """A predicate class that models the 'implies' (=>) predicate."""

    left: Predicate[Any]
    right: Predicate[Any]

    def __call__(self, x: Any) -> bool:
        return not self.left(x) or self.right(x)

    def __repr__(self) -> str:
        return f"{self.left} => {self.right}"

    @override
    def explain_failure(self, x: Any) -> dict[str, Any]:
        return {"reason": f"{self.left} doesn't imply {self.right}"}


def implies_p_p(left: Predicate[Any], right: Predicate[Any]) -> Predicate[Any]:
    return Implies(left=left, right=right)
