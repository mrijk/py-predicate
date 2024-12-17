import re
from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class RegexPredicate[T](Predicate[T]):
    """A predicate class that holds a regular expression."""

    def __init__(self, pattern: str, flags: int = 0):
        self.pattern = pattern
        self.regex = re.compile(pattern, flags)

    def __call__(self, x: str) -> bool:
        return self.regex.match(x) is not None

    def __repr__(self) -> str:
        return f'regex_p("{self.regex.pattern}")'

    @override
    def explain_failure(self, x: str) -> dict:
        return {"reason": f"String {x} didn't match patter {self.regex.pattern}"}
