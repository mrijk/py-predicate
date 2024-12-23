from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from ipaddress import IPv4Address, IPv6Address
from typing import Any, override
from uuid import UUID


@dataclass
class Predicate[T]:
    """An abstract class to represent a predicate."""

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    def __and__(self, predicate: "Predicate") -> "Predicate":
        """Return the 'and' predicate."""
        return AndPredicate(left=self, right=predicate)

    def __or__(self, predicate: "Predicate") -> "Predicate":
        """Return the 'or' predicate."""
        return OrPredicate(left=resolve_predicate(self), right=resolve_predicate(predicate))

    def __xor__(self, predicate: "Predicate") -> "Predicate":
        """Return the 'xor' predicate."""
        return XorPredicate(left=self, right=predicate)

    def __invert__(self) -> "Predicate":
        """Return the 'negated' predicate."""
        return NotPredicate(predicate=self)

    def __contains__(self, predicate: "Predicate") -> bool:
        """Return True if the predicate argument is part of this predicate, otherwise False."""
        return predicate == self

    def explain(self, x: Any) -> dict:
        if self(x):
            return {"result": True}
        return {
            "result": False,
        } | self.explain_failure(x)

    def explain_failure(self, x: Any) -> dict:
        raise NotImplementedError


def resolve_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    from predicate.standard_predicates import PredicateFactory

    match predicate:
        case PredicateFactory() as factory:
            return factory.predicate
        case _:
            return predicate


@dataclass
class AndPredicate[T](Predicate[T]):
    """A predicate class that models the 'and' predicate.

    ```

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the AndPredicate
    right: Predicate[T]
        right predicate of the AndPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) and self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case AndPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False

    def __repr__(self) -> str:
        return f"{repr(self.left)} & {repr(self.right)}"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.left or predicate in self.right

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


@dataclass
class NotPredicate[T](Predicate[T]):
    """A predicate class that models the 'not' predicate.

    ```

    Attributes
    ----------
    predicate: Predicate[T]
        predicate that will be negated


    """

    predicate: Predicate[T]

    def __call__(self, x: T) -> bool:
        return not self.predicate(x)

    def __repr__(self) -> str:
        return f"~{self.predicate}"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.predicate

    @override
    def explain_failure(self, x: T) -> dict:
        return {"predicate": self.predicate.explain(x), "reason": f"not {self.predicate}"}


@dataclass
class OrPredicate[T](Predicate[T]):
    """A predicate class that models the 'or' predicate.

    ```

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
        return f"{repr(self.left)} | {repr(self.right)}"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.left or predicate in self.right

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "left": self.left.explain(x),
            "right": self.right.explain(x),
        }


@dataclass
class XorPredicate[T](Predicate[T]):
    """A predicate class that models the 'xor' predicate.

    ```

    Attributes
    ----------
    left: Predicate[T]
        left predicate of the XorPredicate
    right: Predicate[T]
        right predicate of the XorPredicate

    """

    left: Predicate[T]
    right: Predicate[T]

    def __call__(self, x: T) -> bool:
        return self.left(x) ^ self.right(x)

    def __eq__(self, other: object) -> bool:
        match other:
            case XorPredicate(left, right):
                return (left == self.left and right == self.right) or (right == self.left and left == self.right)
            case _:
                return False

    def __repr__(self) -> str:
        return f"{repr(self.left)} ^ {repr(self.right)}"

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate == self or predicate in self.left or predicate in self.right

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "left": self.left.explain(x),
            "right": self.right.explain(x),
        }


type ConstrainedT[T: (int, str, float, datetime, UUID, IPv4Address, IPv6Address)] = T
