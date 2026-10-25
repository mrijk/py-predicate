from dataclasses import dataclass
from typing import ClassVar, override

from predicate.predicate import Predicate, repr_operand


@dataclass
class AndPredicate[T](Predicate[T]):
    """A predicate class that models the 'and' predicate.

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the AndPredicate
    right: Predicate[T]
        right predicate of the AndPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    precedence: ClassVar[int] = 3

    def __call__(self, x: T) -> bool:
        return self.left(x) and self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case AndPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False

    def __repr__(self) -> str:
        return f"{repr_operand(self.left, 3)} & {repr_operand(self.right, 4)}"

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
        left_explanation = self.left.explain(x)

        if not (left_result := left_explanation["result"]):
            return {
                "left": {
                    "result": left_result,
                    "explanation": left_explanation,
                }
            }

        right_explanation = self.right.explain(x)
        right_result = right_explanation["result"]
        return {
            "left": {
                "result": left_result,
                "explanation": left_explanation,
            },
            "right": {
                "result": right_result,
                "explanation": right_explanation,
            },
        }


def and_p[T](left: Predicate[T], right: Predicate[T]):
    return AndPredicate(left=left, right=right)
