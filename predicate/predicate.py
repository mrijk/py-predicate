from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Final, Iterable
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


def resolve_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    from predicate.standard_predicates import PredicateFactory

    match predicate:
        case PredicateFactory() as factory:
            return factory.predicate
        case _:
            return predicate


@dataclass
class FnPredicate[T](Predicate[T]):
    """A predicate class that can hold a function."""

    predicate_fn: Callable[[T], bool]

    def __call__(self, x: T) -> bool:
        return self.predicate_fn(x)


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


@dataclass
class InPredicate[T](Predicate[T]):
    """A predicate class that models the 'in' predicate."""

    v: set[T]

    def __init__(self, v: Iterable[T]):
        self.v = set(v)

    def __call__(self, x: T) -> bool:
        return x in self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, InPredicate) and self.v == other.v

    def __repr__(self) -> str:
        items = ", ".join(str(item) for item in self.v)
        return f"in_p({items})"


@dataclass
class NotInPredicate[T](Predicate[T]):
    """A predicate class that models the 'not in' predicate."""

    v: set[T]

    def __init__(self, v: Iterable[T]):
        self.v = set(v)

    def __call__(self, x: T) -> bool:
        return x not in self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, NotInPredicate) and self.v == other.v

    def __repr__(self) -> str:
        items = ", ".join(str(item) for item in self.v)
        return f"not_in_p({items})"


@dataclass
class EqPredicate[T](Predicate[T]):
    """A predicate class that models the 'eq' (=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x == self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, EqPredicate) and self.v == other.v

    def __repr__(self) -> str:
        return f"eq_p({self.v})"


@dataclass
class NePredicate[T](Predicate[T]):
    """A predicate class that models the 'ne' (!=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x != self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, NePredicate) and self.v == other.v

    def __repr__(self) -> str:
        return f"ne_p({self.v})"


@dataclass
class GePredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'ge' (>=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x >= self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GePredicate) and self.v == other.v

    def __repr__(self) -> str:
        return f"ge_p({self.v})"


@dataclass
class GtPredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'gt' (>) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x > self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GtPredicate) and self.v == other.v

    def __repr__(self) -> str:
        return f"gt_p({self.v})"


@dataclass
class LePredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'le' (<=) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x <= self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LePredicate) and self.v == other.v

    def __repr__(self) -> str:
        return f"le_p({self.v})"


@dataclass
class LtPredicate[T: (int, str, datetime, UUID)](Predicate[T]):
    """A predicate class that models the 'lt' (<) predicate."""

    v: T

    def __call__(self, x: T) -> bool:
        return x < self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LtPredicate) and self.v == other.v

    def __repr__(self) -> str:
        return f"lt_p({self.v})"


@dataclass
class AllPredicate[T](Predicate[T]):
    """A predicate class that models the 'all' predicate."""

    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iter)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AllPredicate) and self.predicate == other.predicate

    def __repr__(self) -> str:
        return f"all({repr(self.predicate)})"


@dataclass
class AnyPredicate[T](Predicate[T]):
    """A predicate class that models the 'any' predicate."""

    predicate: Predicate[T]

    def __call__(self, iter: Iterable[T]) -> bool:
        return any(self.predicate(x) for x in iter)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AnyPredicate) and self.predicate == other.predicate

    def __repr__(self) -> str:
        return f"any({repr(self.predicate)})"


@dataclass
class IsEmptyPredicate[T](Predicate[T]):
    """A predicate class that models the 'empty' predicate."""

    def __call__(self, iter: Iterable[T]) -> bool:
        return len(list(iter)) == 0

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsEmptyPredicate)

    def __repr__(self) -> str:
        return "is_empty_p"


@dataclass
class IsNotEmptyPredicate[T](Predicate[T]):
    """A predicate class that models the 'not empty' predicate."""

    def __call__(self, iter: Iterable[T]) -> bool:
        return len(list(iter)) > 0

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsNotEmptyPredicate)

    def __repr__(self) -> str:
        return "is_not_empty_p"


@dataclass
class IsInstancePredicate[T](Predicate[T]):
    """A predicate class that models the 'isinstance' predicate."""

    klass: type | tuple

    def __call__(self, x: object) -> bool:
        return isinstance(x, self.klass)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsInstancePredicate) and self.klass == other.klass

    def __repr__(self) -> str:
        name = self.klass[0].__name__  # type: ignore
        return f"is_{name}_p"


@dataclass
class AlwaysTruePredicate(Predicate):
    """A predicate class that models the 'True' predicate."""

    def __call__(self, *args, **kwargs):
        return True

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AlwaysTruePredicate)

    def __repr__(self) -> str:
        return "always_true_p"


@dataclass
class AlwaysFalsePredicate(Predicate):
    """A predicate class that models the 'False' predicate."""

    def __call__(self, *args, **kwargs):
        return False

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AlwaysFalsePredicate)

    def __repr__(self) -> str:
        return "always_false_p"


@dataclass
class IsNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is none' predicate."""

    def __call__(self, x: T) -> bool:
        return x is None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsNonePredicate)

    def __repr__(self) -> str:
        return "is_none_p"


@dataclass
class IsNotNonePredicate[T](Predicate[T]):
    """A predicate class that models the 'is not none' predicate."""

    def __call__(self, x: T) -> bool:
        return x is not None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IsNotNonePredicate)

    def __repr__(self) -> str:
        return "is_not_none_p"


@dataclass
class IsFalsyPredicate[T](Predicate[T]):
    """A predicate class that the falsy (0, False, [], "", etc.) predicate."""

    def __call__(self, x: T) -> bool:
        return not bool(x)

    def __repr__(self) -> str:
        return "is_falsy_p"


@dataclass
class IsTruthyPredicate[T](Predicate[T]):
    """A predicate class that the truthy (13, True, [1], "foo", etc.) predicate."""

    def __call__(self, x: T) -> bool:
        return bool(x)

    def __repr__(self) -> str:
        return "is_truthy_p"


always_true_p: Final[AlwaysTruePredicate] = AlwaysTruePredicate()
"""Predicate that always evaluates to True."""

always_false_p: Final[AlwaysFalsePredicate] = AlwaysFalsePredicate()
"""Predicate that always evaluates to False."""

is_empty_p: Final[IsEmptyPredicate] = IsEmptyPredicate()
"""Predicate that returns True if the iterable is empty, otherwise False."""

is_not_empty_p: Final[IsNotEmptyPredicate] = IsNotEmptyPredicate()
"""Predicate that returns True if the iterable is not empty, otherwise False."""


@dataclass
class NamedPredicate(Predicate):
    """A predicate class to generate truth tables."""

    name: str
    v: bool = False

    def __call__(self, *args) -> bool:
        return self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, NamedPredicate) and self.name == other.name

    def __repr__(self) -> str:
        return self.name
