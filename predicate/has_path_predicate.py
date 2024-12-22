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
            case dict() as d:
                return match_dict(self.path, d)
            case _:
                return False

    def __repr__(self) -> str:
        return f"has_path_p({predicates_repr(self.path)})"

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case dict():
                # TODO: more details about first part of path that didn't match
                return {"reason": f"Dictionary {x} didn't match path"}
            case _:
                return {"reason": f"Value {x} is not a dict"}


def match_dict(path: list[Predicate], x: dict) -> bool:
    first_p, *rest = path
    found = [v for k, v in x.items() if first_p(k)]
    return any(match_rest(value, rest) for value in found)


def match_rest(value: Any, rest_path: list[Predicate]) -> bool:
    match value:
        case dict() as d if rest_path:
            return match_dict(rest_path, d)
        case list() as l if rest_path:
            first_p, *rest = rest_path
            return first_p(l) and any(match_rest(value, rest) for value in l)
        case _ if len(rest_path) == 1:
            return rest_path[0](value)
        case _:
            return len(rest_path) == 0
