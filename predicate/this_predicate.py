import inspect
from dataclasses import dataclass
from functools import cached_property
from typing import Any

from more_itertools import first_true

from predicate.predicate import Predicate


@dataclass
class ThisPredicate[T](Predicate[T]):
    """A predicate class that lazily references another predicate."""

    @cached_property
    def this_predicate(self) -> Predicate:
        return find_this_predicate(self.frame, self)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        return self.this_predicate(x)

    def __repr__(self) -> str:
        return "this_p"


def find_in_locals(locals: dict, predicate: Predicate) -> Predicate | None:
    def is_other_predicate(key: str, value: Any) -> bool:
        return isinstance(value, Predicate) and value != predicate and key != "self"

    other_predicates = (value for key, value in locals if is_other_predicate(key, value))

    return first_true(other_predicates, pred=lambda other: predicate in other)


def find_this_predicate(frame, predicate: Predicate) -> Predicate:
    locals = frame.f_locals.items()
    if found := find_in_locals(locals, predicate):
        return found

    return find_this_predicate(frame.f_back, predicate)
