from dataclasses import dataclass
from typing import Iterable, override

from predicate.helpers import first_false
from predicate.predicate import Predicate


@dataclass
class AllPredicate[T](Predicate[T]):
    """A predicate class that models the 'all' predicate."""

    predicate: Predicate[T]

    def __call__(self, iterable: Iterable[T]) -> bool:
        return all(self.predicate(x) for x in iterable)

    def __contains__(self, predicate: Predicate[T]) -> bool:
        return predicate in self.predicate

    def __repr__(self) -> str:
        return f"all_p({self.predicate!r})"

    @override
    def get_klass(self) -> type:
        return self.predicate.klass

    @override
    @property
    def count(self) -> int:
        return 1 + self.predicate.count

    @override
    def explain_failure(self, iterable: Iterable[T]) -> dict:
        fail = first_false(iterable, self.predicate)

        return {"reason": f"Item '{fail}' didn't match predicate {self.predicate!r}"}
