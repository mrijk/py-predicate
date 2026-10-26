from abc import abstractmethod
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from fractions import Fraction
from functools import partial
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Callable, ClassVar, Iterable, Iterator, final
from uuid import UUID

from more_itertools import spy


@dataclass
class Predicate[T]:
    """An abstract class to represent a predicate."""

    # Python operator precedence, used by repr to add parentheses: | < ^ < & < ~ < atoms
    precedence: ClassVar[int] = 5

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    def __and__(self, predicate: "Predicate") -> "Predicate":
        """Return the 'and' predicate."""
        from predicate.and_predicate import AndPredicate

        return AndPredicate(left=resolve_predicate(self), right=resolve_predicate(predicate))

    def __or__(self, predicate: "Predicate") -> "Predicate":
        """Return the 'or' predicate."""
        from predicate.or_predicate import OrPredicate

        return OrPredicate(left=resolve_predicate(self), right=resolve_predicate(predicate))

    def __xor__(self, predicate: "Predicate") -> "Predicate":
        """Return the 'xor' predicate."""
        from predicate.xor_predicate import XorPredicate

        return XorPredicate(left=resolve_predicate(self), right=resolve_predicate(predicate))

    def __invert__(self) -> "Predicate":
        """Return the 'negated' predicate."""
        from predicate.not_predicate import NotPredicate

        return NotPredicate(predicate=self)

    def __contains__(self, predicate: "Predicate") -> bool:
        """Return True if the predicate argument is part of this predicate, otherwise False."""
        return predicate == self

    @property
    def count(self) -> int:
        """Returns number of operators in a predicate. Used for optimization."""
        return 0

    @property
    def klass(self) -> type:
        raise NotImplementedError

    @final
    def explain(self, x: Any, *args, **kwargs) -> dict:
        if self(x, *args, **kwargs):
            return {"result": True}
        return {
            "result": False,
        } | self.explain_failure(x, *args, **kwargs)

    def explain_failure(self, x: Any, /, *args, **kwargs) -> dict:
        raise NotImplementedError

    def consumes_single(self, iterable: Iterable[Any]) -> Iterator[int]:
        [item], _ = spy(iterable)
        yield 1 if self(item) else 0

    def consumes(self, iterable: Iterable[Any]) -> Iterator[int]:
        raise NotImplementedError


def repr_operand(predicate: Predicate, precedence: int) -> str:
    """Return repr of predicate, parenthesized if it binds looser than precedence."""
    return f"({predicate!r})" if predicate.precedence < precedence else repr(predicate)


def resolve_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    from predicate.predicate_factory import PredicateFactory

    match predicate:
        case PredicateFactory() as factory:
            return factory.predicate
        case _:
            return predicate


type ConstrainedT[T: (int, str, float, datetime, date, Decimal, Fraction, UUID, IPv4Address, IPv6Address)] = T


def predicate_partial[T](
    func: Callable[[Predicate[T], Predicate[T]], Predicate[T]], /, *args, **kwargs
) -> Callable[[Predicate[T]], Predicate[T]]:
    return partial(func, *args, **kwargs)
