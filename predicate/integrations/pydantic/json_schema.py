from collections.abc import Callable
from typing import Any

from pydantic_core import to_jsonable_python

from predicate.all_predicate import AllPredicate
from predicate.and_predicate import AndPredicate
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.in_predicate import InPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.not_predicate import NotPredicate
from predicate.or_predicate import OrPredicate
from predicate.predicate import Predicate
from predicate.regex_predicate import RegexPredicate

_BOUNDS: dict[type, str] = {
    GePredicate: "minimum",
    GtPredicate: "exclusiveMinimum",
    LePredicate: "maximum",
    LtPredicate: "exclusiveMaximum",
}


def _jsonable(value: Any) -> bool:
    try:
        to_jsonable_python(value)
    except Exception:  # noqa: BLE001
        return False
    return True


def _merge(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    if left.keys() & right.keys():
        return {"allOf": [left, right]}  # ponytail: no bound tightening, allOf is valid and simple
    return left | right


def _and(p: AndPredicate[Any]) -> dict[str, Any] | None:
    left, right = _schema(p.left), _schema(p.right)
    if left is None or right is None:
        return left or right  # an unmapped side only makes the schema looser, which is safe
    return _merge(left, right)


def _or(p: OrPredicate[Any]) -> dict[str, Any] | None:
    left, right = _schema(p.left), _schema(p.right)
    # a dropped side would make anyOf too strict, so drop the whole thing
    return None if left is None or right is None else {"anyOf": [left, right]}


def _not(p: NotPredicate[Any]) -> dict[str, Any] | None:
    inner = _schema(p.predicate)
    return None if inner is None else {"not": inner}


def _wrap(key: str) -> Callable[[Any], dict[str, Any] | None]:
    def wrap(p: Any) -> dict[str, Any] | None:
        inner = _schema(p.predicate)
        return None if inner is None else {key: inner}

    return wrap


def _bound(p: Any) -> dict[str, Any] | None:
    return {_BOUNDS[type(p)]: p.v} if _jsonable(p.v) else None


def _eq(p: EqPredicate[Any]) -> dict[str, Any] | None:
    return {"const": p.v} if _jsonable(p.v) else None


def _in(p: InPredicate[Any]) -> dict[str, Any] | None:
    if not isinstance(p.v, list | tuple | set | frozenset) or not _jsonable(list(p.v)):
        return None
    return {"enum": list(p.v)}


def _regex(p: RegexPredicate[Any]) -> dict[str, Any] | None:
    # regex_p uses re.match (anchored at the start), JSON Schema pattern is a search
    return {"pattern": f"^(?:{p.regex.pattern})"}


_MAPPERS: dict[type, Callable[[Any], dict[str, Any] | None]] = {
    **dict.fromkeys(_BOUNDS, _bound),
    EqPredicate: _eq,
    InPredicate: _in,
    RegexPredicate: _regex,
    AndPredicate: _and,
    OrPredicate: _or,
    NotPredicate: _not,
    AllPredicate: _wrap("items"),
    AnyPredicate: _wrap("contains"),
}


def _schema(predicate: Predicate[Any]) -> dict[str, Any] | None:
    mapper = _MAPPERS.get(type(predicate))
    return mapper(predicate) if mapper else None


def predicate_to_json_schema(predicate: Predicate[Any]) -> dict[str, Any]:
    """Map a predicate to JSON Schema keywords; predicates without a mapping are left out ({})."""
    return _schema(predicate) or {}
