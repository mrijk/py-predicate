from dataclasses import dataclass

from predicate.predicate import Predicate


@dataclass
class NamedPredicate(Predicate):
    """A predicate class to generate_true truth tables."""

    name: str
    v: bool = False

    def __call__(self, *args) -> bool:
        return self.v

    def __eq__(self, other: object) -> bool:
        return isinstance(other, NamedPredicate) and self.name == other.name

    def __repr__(self) -> str:
        return self.name
