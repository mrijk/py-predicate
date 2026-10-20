import re
from dataclasses import dataclass
from typing import Any, Final, override

from predicate.predicate import Predicate


@dataclass
class IsRegexPredicate[T](Predicate[T]):
    """A predicate class that models the is_regex predicate."""

    def __call__(self, x: Any) -> bool:
        if not isinstance(x, str):
            return False
        try:
            re.compile(x)
        except re.error:
            return False
        return True

    def __repr__(self) -> str:
        return "is_regex_p"

    @override
    def explain_failure(self, x: Any) -> dict:
        if not isinstance(x, str):
            return {"reason": f"{x} is not a string"}
        try:
            re.compile(x)
        except re.error as e:
            return {"reason": f"String {x} is not a valid regex: {e}"}


is_regex_p: Final[IsRegexPredicate] = IsRegexPredicate()
