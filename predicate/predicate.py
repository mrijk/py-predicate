from abc import abstractmethod
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from fractions import Fraction
from functools import partial
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Callable, ClassVar, Iterable, Iterator, Protocol, cast, final, overload
from uuid import UUID

from more_itertools import spy


@dataclass
class Predicate[T]:
    """An abstract class to represent a predicate."""

    # Python operator precedence, used by repr to add parentheses: | < ^ < & < ~ < atoms
    precedence: ClassVar[int] = 5

    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> bool:
        raise NotImplementedError

    @overload
    def __and__(self, other: "Predicate[Any]") -> "Predicate[Any]": ...

    @overload
    def __and__(self, other: Callable[[T], bool]) -> "Predicate[Any]": ...

    def __and__(self, other: Any) -> "Predicate[Any]":
        """Return the 'and' predicate."""
        from predicate.and_predicate import AndPredicate

        left = resolve_predicate(self)
        right = _as_predicate(other)

        return AndPredicate(left=left, right=right)

    @overload
    def __rand__(self, other: "Predicate[Any]") -> "Predicate[Any]": ...

    @overload
    def __rand__(self, other: Callable[[T], bool]) -> "Predicate[Any]": ...

    def __rand__(self, other: Any) -> "Predicate[Any]":
        """Return the 'rand' predicate."""
        from predicate.and_predicate import AndPredicate

        left = _as_predicate(other)
        right = resolve_predicate(self)

        return AndPredicate(left=left, right=right)

    @overload
    def __or__(self, other: "Predicate[Any]") -> "Predicate[Any]": ...

    @overload
    def __or__(self, other: Callable[[T], bool]) -> "Predicate[Any]": ...

    def __or__(self, other: Any) -> "Predicate[Any]":
        """Return the 'or' predicate."""
        from predicate.or_predicate import OrPredicate

        left = resolve_predicate(self)
        right = _as_predicate(other)

        return OrPredicate(left=left, right=right)

    @overload
    def __ror__(self, other: "Predicate[Any]") -> "Predicate[Any]": ...

    @overload
    def __ror__(self, other: Callable[[T], bool]) -> "Predicate[Any]": ...

    def __ror__(self, other: Any) -> "Predicate[Any]":
        """Return the 'ror' predicate."""
        from predicate.or_predicate import OrPredicate

        left = _as_predicate(other)
        right = resolve_predicate(self)

        return OrPredicate(left=left, right=right)

    @overload
    def __xor__(self, other: "Predicate[Any]") -> "Predicate[Any]": ...

    @overload
    def __xor__(self, other: Callable[[T], bool]) -> "Predicate[Any]": ...

    def __xor__(self, other: Any) -> "Predicate[Any]":
        """Return the 'xor' predicate."""
        from predicate.xor_predicate import XorPredicate

        left = resolve_predicate(self)
        right = _as_predicate(other)

        return XorPredicate(left=left, right=right)

    @overload
    def __rxor__(self, other: "Predicate[Any]") -> "Predicate[Any]": ...

    @overload
    def __rxor__(self, other: Callable[[T], bool]) -> "Predicate[Any]": ...

    def __rxor__(self, other: Any) -> "Predicate[Any]":
        """Return the 'rxor' predicate."""
        from predicate.xor_predicate import XorPredicate

        left = _as_predicate(other)
        right = resolve_predicate(self)

        return XorPredicate(left=left, right=right)

    def __invert__(self) -> "Predicate[Any]":
        """Return the 'negated' predicate."""
        from predicate.not_predicate import NotPredicate

        return NotPredicate(predicate=self)

    def __contains__(self, predicate: "Predicate[Any]") -> bool:
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
    def explain(self, x: Any, *args: Any, **kwargs: Any) -> dict[str, Any]:
        if self(x, *args, **kwargs):
            return {"result": True}
        return {
            "result": False,
        } | self.explain_failure(x, *args, **kwargs)

    def explain_failure(self, x: Any, /, *args: Any, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError

    def consumes(self, iterable: Iterable[Any]) -> Iterator[int]:
        """Yield how many items from the start of the iterable this predicate can match, for match_p.

        By default a predicate matches a single item; predicates over several items (all_p, any_p, ...) override it.
        """
        [item], _ = spy(iterable)
        yield 1 if self(item) else 0


def _as_predicate(candidate: Any) -> Predicate[Any]:
    match candidate:
        case Predicate():
            return resolve_predicate(candidate)
        case _ if callable(candidate):
            from predicate.function_predicate import fn_p

            return fn_p(candidate)
        case _:
            return cast("Predicate[Any]", NotImplemented)


def repr_operand(predicate: Predicate[Any], precedence: int) -> str:
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


class SupportsComparison(Protocol):
    """A type that supports the ordering operators <, <=, > and >=."""

    def __lt__(self, other: Any, /) -> bool: ...

    def __le__(self, other: Any, /) -> bool: ...

    def __gt__(self, other: Any, /) -> bool: ...

    def __ge__(self, other: Any, /) -> bool: ...


def predicate_partial[T](
    func: Callable[[Predicate[T], Predicate[T]], Predicate[T]], /, *args: Any, **kwargs: Any
) -> Callable[[Predicate[T]], Predicate[T]]:
    return partial(func, *args, **kwargs)
