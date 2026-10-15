from dataclasses import dataclass
from typing import override

from predicate.predicate import Predicate


@dataclass
class OrPredicate[T](Predicate[T]):
    """A predicate class that models the 'or' predicate.

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the OrPredicate
    right: Predicate[T]
        right predicate of the OrPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) or self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case OrPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False

    def __repr__(self) -> str:
        return f"{self.left!r} | {self.right!r}"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.left or predicate in self.right

    @override
    @property
    def klass(self) -> type:
        return self.left.klass

    @override
    @property
    def count(self) -> int:
        return 1 + self.left.count + self.right.count

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "left": self.left.explain(x),
            "right": self.right.explain(x),
        }


def or_p[T](left: Predicate[T], right: Predicate[T]):
    return OrPredicate(left=left, right=right)
