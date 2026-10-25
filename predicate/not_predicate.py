from dataclasses import dataclass
from typing import ClassVar, override

from predicate.predicate import Predicate, repr_operand


@dataclass
class NotPredicate[T](Predicate[T]):
    """A predicate class that models the 'not' predicate.

    Attributes
    ----------
    predicate: Predicate[T]
        predicate that will be negated

    """

    predicate: Predicate[T]

    precedence: ClassVar[int] = 4

    def __call__(self, x: T) -> bool:
        return not self.predicate(x)

    def __repr__(self) -> str:
        return f"~{repr_operand(self.predicate, 4)}"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.predicate

    @override
    @property
    def klass(self) -> type:
        return self.predicate.klass

    @override
    @property
    def count(self) -> int:
        return 1 + self.predicate.count

    @override
    def explain_failure(self, x: T) -> dict:
        return {"predicate": self.predicate.explain(x), "reason": f"not {self.predicate}"}
