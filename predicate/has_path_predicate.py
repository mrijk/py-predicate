from dataclasses import dataclass
from typing import Any, override

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
        return "has_path_p"

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case dict():
                return {"reason": "tbd"}
            case _:
                return {"reason": f"Value {x} is not a dict"}


def match_dict(path: list[Predicate], x: dict) -> bool:
    def match_rest(rest_path: list[Predicate], value: Any) -> bool:
        match value:
            case dict() as d if rest_path:
                return match_dict(rest_path, d)
            case _ if len(rest_path) == 1:
                return rest_path[0](value)
            case _:
                return len(rest_path) == 0

    first_p, *rest = path
    found = [v for k, v in x.items() if first_p(k)]
    return any(match_rest(rest, value) for value in found)
