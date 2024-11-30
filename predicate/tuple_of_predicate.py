from dataclasses import dataclass

from more_itertools import ilen

from predicate.predicate import Predicate


@dataclass
class TupleOfPredicate[T](Predicate[T]):
    """A predicate class that models the tuple_of predicate."""

    predicates: list[Predicate]

    def __call__(self, x: tuple) -> bool:
        return ilen(x) == len(self.predicates) and all(p(v) for p, v in zip(self.predicates, x, strict=False))

    def __repr__(self) -> str:
        # TODO: add predicates repr
        return "tuple_of_p"
