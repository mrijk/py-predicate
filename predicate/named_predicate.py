from dataclasses import dataclass

from predicate.predicate import Predicate


@dataclass
class NamedPredicate(Predicate):
    """A predicate class to generate_true truth tables."""

    name: str
    v: bool = False

    def __call__(self, *args) -> bool:
        return self.v

    def __repr__(self) -> str:
        return self.name
