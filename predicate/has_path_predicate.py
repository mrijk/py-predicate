from dataclasses import dataclass
from typing import Any, override

from predicate.helpers import predicates_repr
from predicate.predicate import Predicate


@dataclass
class HasPathPredicate[T](Predicate[T]):
    """A predicate class that models the 'length' predicate."""

    path: list[Predicate]

    def __call__(self, x: Any) -> bool:
        match x:
            case dict(d):
                return match_dict(d, path=self.path)
            case _:
                return False

    def __repr__(self) -> str:
        return f"has_path_p({predicates_repr(self.path)})"

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case dict():
                current = x
                for i, p in enumerate(self.path):
                    if not isinstance(current, dict):
                        return {"reason": f"Expected a dict at path position {i}, got {type(current).__name__}"}
                    keys = [k for k in current if p(k)]
                    if not keys:
                        return {"reason": f"No key matching {p!r} found at path position {i}"}
                    current = current[keys[0]]
                return {"reason": f"Dictionary {x} didn't match path"}  # pragma: no cover
            case _:
                return {"reason": f"Value {x} is not a dict"}


def match_dict(x: dict, *, path: list[Predicate]) -> bool:
    first_p, *rest = path
    found = [v for k, v in x.items() if first_p(k)]
    return any(match_rest(value, rest) for value in found)


def match_rest(value: Any, rest_path: list[Predicate]) -> bool:
    match (value, rest_path):
        case (dict(d), [_, *_]):
            return match_dict(d, path=rest_path)
        case (list(l), [first_p, *rest]):
            return first_p(l) and any(match_rest(v, rest) for v in l)
        case (_, [p]):
            return p(value)
        case (_, []):
            return True
        case _:
            return False


def has_path_p(*predicates: Predicate) -> Predicate:
    """Return True if value is a dict, and contains the path specified by the predicates, otherwise False."""
    return HasPathPredicate(list(predicates))
