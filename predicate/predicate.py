from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Final, override
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

    def explain(self, x: Any) -> dict:
        return {"result": True} if self(x) else self.explain_failure(x)

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
        return f"~{repr(self.predicate)}"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"result": False, "predicate": self.predicate.explain(x), "reason": f"not {repr(self.predicate)}"}


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

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "result": False,
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

    @override
    def explain_failure(self, x: T) -> dict:
        return {
            "result": False,
            "left": self.left.explain(x),
            "right": self.right.explain(x),
        }


type ConstrainedT[T: (int, str, float, datetime, UUID)] = T


@dataclass
class AlwaysTruePredicate(Predicate):
    """A predicate class that models the 'True' predicate."""

    def __call__(self, *args, **kwargs):
        return True

    def __repr__(self) -> str:
        return "always_true_p"


@dataclass
class AlwaysFalsePredicate(Predicate):
    """A predicate class that models the 'False' predicate."""

    def __call__(self, *args, **kwargs):
        return False

    def __repr__(self) -> str:
        return "always_false_p"

    @override
    def explain_failure(self, *args, **kwargs) -> dict:
        return {"result": False, "reason": "Always returns False"}


@dataclass
class IsFalsyPredicate[T](Predicate[T]):
    """A predicate class that the falsy (0, False, [], "", etc.) predicate."""

    def __call__(self, x: T) -> bool:
        return not bool(x)

    def __repr__(self) -> str:
        return "is_falsy_p"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"result": False, "reason": f"{x} is not a falsy value"}


@dataclass
class IsTruthyPredicate[T](Predicate[T]):
    """A predicate class that the truthy (13, True, [1], "foo", etc.) predicate."""

    def __call__(self, x: T) -> bool:
        return bool(x)

    def __repr__(self) -> str:
        return "is_truthy_p"

    @override
    def explain_failure(self, x: T) -> dict:
        return {"result": False, "reason": f"{x} is not a truthy value"}


always_true_p: Final[AlwaysTruePredicate] = AlwaysTruePredicate()
"""Predicate that always evaluates to True."""

always_false_p: Final[AlwaysFalsePredicate] = AlwaysFalsePredicate()
"""Predicate that always evaluates to False."""

# Next two predicates mimim the Rust equivalents

always_p = always_true_p
"""Synonym for always_true_p."""

never_p = always_false_p
"""Synonym for always_false_p."""
