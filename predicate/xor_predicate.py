from dataclasses import dataclass
from typing import ClassVar, override

from predicate.predicate import Predicate, repr_operand


@dataclass
class XorPredicate[T](Predicate[T]):
    """A predicate class that models the 'xor' predicate.

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the XorPredicate
    right: Predicate[T]
        right predicate of the XorPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    precedence: ClassVar[int] = 2

    def __call__(self, x: T) -> bool:
        return self.left(x) ^ self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case XorPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False

    def __repr__(self) -> str:
        return f"{repr_operand(self.left, 2)} ^ {repr_operand(self.right, 3)}"

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


def xor_p[T](left: Predicate[T], right: Predicate[T]):
    return XorPredicate(left=left, right=right)
