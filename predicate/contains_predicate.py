from dataclasses import dataclass
from typing import override

from predicate.predicate import Explanation, Predicate


@dataclass
class ContainsPredicate(Predicate[str]):
    """Match strings containing a fixed substring."""

    substring: str

    def __call__(self, text: str) -> bool:
        return self.substring in text

    def __repr__(self) -> str:
        return f"contains_p({self.substring!r})"

    @override
    @property
    def klass(self) -> type[str]:
        return str

    @override
    def explain_failure(self, text: str) -> Explanation:
        return {"reason": f"{text!r} does not contain {self.substring!r}"}


def contains_p(substring: str) -> ContainsPredicate:
    """Return a case-sensitive predicate for strings containing substring."""
    return ContainsPredicate(substring)
