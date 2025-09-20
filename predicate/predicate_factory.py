from dataclasses import dataclass
from typing import Callable

from predicate.predicate import Predicate


@dataclass
class PredicateFactory[T](Predicate[T]):
    """Test."""

    factory: Callable[[], Predicate]

    @property
    def predicate(self) -> Predicate:
        return self.factory()

    def __call__(self, *args, **kwargs) -> bool:
        raise ValueError("Don't call PredicateFactory directly")

    def __repr__(self) -> str:
        return repr(self.predicate)
