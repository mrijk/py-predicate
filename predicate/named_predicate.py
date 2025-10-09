from dataclasses import dataclass

from predicate.implies import Implies
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate, XorPredicate


@dataclass
class NamedPredicate(Predicate):
    """A predicate class to generate_true truth tables."""

    name: str
    v: bool = False

    def __call__(self, *args) -> bool:
        return self.v

    def __repr__(self) -> str:
        return self.name


def _to_named_predicate(predicate: Predicate, names_map: dict[str, NamedPredicate]) -> Predicate:
    """Convert any predicate to a named predicate."""

    def next_name() -> str:
        return f"p{len(names_map) + 1}"

    match predicate:
        case OrPredicate(left, right) | AndPredicate(left, right) | XorPredicate(left, right) | Implies(left, right):
            klass = predicate.__class__
            return klass(left=_to_named_predicate(left, names_map), right=_to_named_predicate(right, names_map))
        case NamedPredicate() as named:
            return named
        case NotPredicate(not_predicate):
            return NotPredicate(predicate=_to_named_predicate(not_predicate, names_map))
        case _:
            key = str(predicate)
            if named_predicate := names_map.get(key, None):
                return named_predicate
            named_predicate = NamedPredicate(name=next_name())
            names_map[key] = named_predicate
            return named_predicate


def to_named_predicate(predicate: Predicate) -> Predicate:
    return _to_named_predicate(predicate, {})
