from dataclasses import dataclass
from typing import override

from more_itertools import first, ilen

from predicate.helpers import predicates_repr
from predicate.predicate import Predicate


@dataclass
class TupleOfPredicate[T](Predicate[T]):
    """A predicate class that models the tuple_of predicate."""

    predicates: list[Predicate]

    def __call__(self, x: tuple) -> bool:
        return ilen(x) == len(self.predicates) and all(p(v) for p, v in zip(self.predicates, x, strict=False))

    def __repr__(self) -> str:
        return f"is_tuple_of_p({predicates_repr(self.predicates)})"

    @override
    def explain_failure(self, x: tuple) -> dict:
        if (actual_length := ilen(x)) != (expected_length := len(self.predicates)):
            return {"reason": f"Incorrect tuple size, expected: {expected_length}, actual: {actual_length}"}

        index, fail_p, fail_v = first(
            (i, p, v) for i, (p, v) in enumerate(zip(self.predicates, x, strict=False)) if not p(v)
        )
        return {"index": index, "value": fail_v} | fail_p.explain_failure(fail_v)


def is_tuple_of_p(*predicates: Predicate) -> Predicate:
    """Return True if value is a tuple, and for all elements in the tuple the predicate is True, otherwise False."""
    return TupleOfPredicate(predicates=list(predicates))
