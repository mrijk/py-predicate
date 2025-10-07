from dataclasses import dataclass

from predicate.predicate import AndPredicate, Predicate


@dataclass
class IsSamePredicate[T](Predicate[T]):
    """A predicate class that checks if two predicates are equivalent."""

    predicate: Predicate[T]

    def __call__(self, predicate: Predicate) -> bool:
        return is_same(self.predicate, predicate)

    def __repr__(self) -> str:
        return "is_same_p"


def is_same(p1: Predicate, p2: Predicate) -> bool:
    if p1 == p2:
        return True

    match p1, p2:
        case AndPredicate(), AndPredicate():
            return is_same_and(p1, p2)
        case _:
            return False


def is_same_and(p1: AndPredicate, p2: AndPredicate) -> bool:
    return False


def is_same_p[T](predicate: Predicate[T]) -> IsSamePredicate[T]:
    """Return True if the predicate is the same, otherwise False."""
    return IsSamePredicate(predicate=predicate)
