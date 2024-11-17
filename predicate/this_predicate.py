import inspect
from dataclasses import dataclass
from functools import cached_property

from predicate.predicate import AllPredicate, AndPredicate, OrPredicate, Predicate


@dataclass
class ThisPredicate[T](Predicate[T]):
    """A predicate class that lazily references another predicate."""

    @cached_property
    def this_predicate(self) -> Predicate | None:
        return find_this_predicate(self.frame, self)

    def __call__(self, x: T) -> bool:
        self.frame = inspect.currentframe()
        if self.this_predicate:
            return self.this_predicate(x)
        raise ValueError(f"Could not find 'this' predicate {self}")

    def __repr__(self) -> str:
        return "this_p"


def find_this_predicate(frame, predicate: Predicate) -> Predicate | None:
    for key, value in frame.f_locals.items():
        if isinstance(value, Predicate) and value != predicate and key != "self":
            if predicate_in_predicate_tree(value, predicate):
                return value
    if next_frame := frame.f_back:
        return find_this_predicate(next_frame, predicate)
    return None


def predicate_in_predicate_tree(tree: Predicate, predicate: Predicate) -> bool:
    from predicate.standard_predicates import PredicateFactory

    match tree:
        case AllPredicate(all_predicate):
            return predicate_in_predicate_tree(all_predicate, predicate)
        case AndPredicate(and_left, and_right):
            return predicate_in_predicate_tree(and_left, predicate) or predicate_in_predicate_tree(and_right, predicate)
        case OrPredicate(or_left, or_right):
            return predicate_in_predicate_tree(or_left, predicate) or predicate_in_predicate_tree(or_right, predicate)
        case PredicateFactory() as factory:
            return factory.predicate == predicate
        case _ if tree == predicate:
            return True
        case _:
            return False
