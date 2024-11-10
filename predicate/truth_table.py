from collections.abc import Iterable, Iterator
from itertools import repeat

from more_itertools import gray_product

from predicate import AndPredicate, NotPredicate, Predicate
from predicate.predicate import NamedPredicate, OrPredicate, XorPredicate


def truth_table(predicate: Predicate) -> Iterable[tuple]:
    """Generate a truth table."""
    named_predicates = get_named_predicates(predicate)

    tuples = repeat((False, True), len(named_predicates))

    combinations = sorted(gray_product(*tuples))

    for combination in combinations:
        values = dict(zip(named_predicates, combination, strict=False))
        yield combination, execute_predicate(predicate, values=values)


def get_named_predicates(predicate: Predicate) -> list[str]:
    """Return the names used in the predicate."""

    def get_names() -> Iterator[str]:
        match predicate:
            case AndPredicate(left, right) | OrPredicate(left, right) | XorPredicate(left, right):
                yield from get_named_predicates(left)
                yield from get_named_predicates(right)
            case NotPredicate(not_predicate):
                yield from get_named_predicates(not_predicate)
            case NamedPredicate() as named:
                yield named.name
            case _:
                raise ValueError(f"Type not allowed: {predicate}")

    return sorted(set(get_names()))


def execute_predicate(predicate: Predicate, values: dict) -> bool:
    set_named_values(predicate, values)

    dummy = False
    return predicate(dummy)


def set_named_values(predicate: Predicate, values: dict) -> None:
    """Set the named predicate values."""
    match predicate:
        case AndPredicate(left, right) | OrPredicate(left, right) | XorPredicate(left, right):
            set_named_values(left, values)
            set_named_values(right, values)
        case NotPredicate(not_predicate):
            set_named_values(not_predicate, values)
        case NamedPredicate() as named:
            named.v = values[named.name]
        case _:
            raise ValueError(f"Type not allowed: {predicate}")