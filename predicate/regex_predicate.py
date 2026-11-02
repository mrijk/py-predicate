import re
from dataclasses import dataclass
from typing import Any, override

from predicate.predicate import Predicate


@dataclass
class RegexPredicate[T](Predicate[T]):
    """A predicate class that holds a regular expression."""

    def __init__(self, pattern: str, flags: int = 0):
        self.pattern = pattern
        self.regex = re.compile(pattern, flags)

    def __call__(self, x: Any) -> bool:
        match x:
            case str():
                return self.regex.match(x) is not None
            case _:
                return False

    def __repr__(self) -> str:
        return f'regex_p("{self.regex.pattern}")'

    @override
    def explain_failure(self, x: Any) -> dict:
        match x:
            case str():
                return {"reason": f"String {x} didn't match pattern {self.regex.pattern}"}
            case _:
                return {"reason": f"{x} is not a string"}


def regex_p(pattern: str) -> Predicate[str]:
    """Return True if value matches regex, otherwise False."""
    return RegexPredicate(pattern=pattern)
