from dataclasses import dataclass
from typing import Any, Callable

from predicate.predicate import Predicate


@dataclass
class PredicateFactory[T](Predicate[T]):
    """Test."""

    factory: Callable[[], Predicate[Any]]

    @property
    def predicate(self) -> Predicate[Any]:
        return self.factory()

    def __call__(self, *args: Any, **kwargs: Any) -> bool:
        raise ValueError("Don't call PredicateFactory directly")

    def __repr__(self) -> str:
        return repr(self.predicate)
