from abc import abstractmethod
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from fractions import Fraction
from functools import partial
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Callable, ClassVar, Iterable, Iterator, final, overload
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

    @overload
    def __and__(self, other: "Predicate") -> "Predicate": ...

    @overload
    def __and__(self, other: Callable[[T], bool]) -> "Predicate": ...

    def __and__(self, other: Any) -> "Predicate":
        """Return the 'and' predicate."""
        from predicate.and_predicate import AndPredicate

        left = resolve_predicate(self)
        right = _as_predicate(other)

        return AndPredicate(left=left, right=right)

    def __rand__(self, other) -> "Predicate":
        """Return the 'rand' predicate."""
        return self & other

    @overload
    def __or__(self, other: "Predicate") -> "Predicate": ...

    @overload
    def __or__(self, other: Callable[[T], bool]) -> "Predicate": ...

    def __or__(self, other: Any) -> "Predicate":
        """Return the 'or' predicate."""
        from predicate.or_predicate import OrPredicate

        left = resolve_predicate(self)
        right = _as_predicate(other)

        return OrPredicate(left=left, right=right)

    def __ror__(self, other: Any) -> "Predicate":
        """Return the 'ror' predicate."""
        from predicate.or_predicate import OrPredicate

        left = _as_predicate(other)
        right = resolve_predicate(self)

        return OrPredicate(left=left, right=right)

    @overload
    def __xor__(self, other: "Predicate") -> "Predicate": ...

    @overload
    def __xor__(self, other: Callable[[T], bool]) -> "Predicate": ...

    def __xor__(self, other: Any) -> "Predicate":
        """Return the 'xor' predicate."""
        from predicate.xor_predicate import XorPredicate

        left = resolve_predicate(self)
        right = _as_predicate(other)

        return XorPredicate(left=left, right=right)

    def __rxor__(self, other) -> "Predicate":
        """Return the 'rxor' predicate."""
        return self ^ other

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
    def explain(self, x: Any, *args, **kwargs) -> dict[str, Any]:
        if self(x, *args, **kwargs):
            return {"result": True}
        return {
            "result": False,
        } | self.explain_failure(x, *args, **kwargs)

    def explain_failure(self, x: Any, /, *args, **kwargs) -> dict[str, Any]:
        raise NotImplementedError

    def consumes(self, iterable: Iterable[Any]) -> Iterator[int]:
        """Yield how many items from the start of the iterable this predicate can match, for match_p.

        By default a predicate matches a single item; predicates over several items (all_p, any_p, ...) override it.
        """
        [item], _ = spy(iterable)
        yield 1 if self(item) else 0


def _as_predicate(candidate: Any) -> Predicate:
    match candidate:
        case Predicate():
            return resolve_predicate(candidate)
        case _ if callable(candidate):
            from predicate.function_predicate import fn_p

            return fn_p(candidate)
        case _:
            return NotImplemented


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
