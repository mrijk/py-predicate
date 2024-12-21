from collections.abc import Iterable
from itertools import filterfalse

from more_itertools import first

from predicate.comp_predicate import CompPredicate
from predicate.predicate import AndPredicate, OrPredicate, Predicate


def all_true[T](iterable: Iterable[T], predicate: Predicate[T]) -> bool:
    return all(predicate(item) for item in iterable)


def first_false[T](iterable: Iterable[T], predicate: Predicate[T]) -> T:
    return first(filterfalse(predicate, iterable))


def predicates_repr(predicates: list[Predicate]) -> str:
    return ", ".join(repr(predicate) for predicate in predicates)


def predicate_in_predicate_tree(tree: Predicate, predicate: Predicate) -> bool:
    from predicate.all_predicate import AllPredicate
    from predicate.list_of_predicate import ListOfPredicate
    from predicate.standard_predicates import PredicateFactory

    match tree:
        case AllPredicate(all_predicate):
            return predicate_in_predicate_tree(all_predicate, predicate)
        case ListOfPredicate(list_of_predicate):
            return predicate_in_predicate_tree(list_of_predicate, predicate)
        case AndPredicate(and_left, and_right):
            return predicate_in_predicate_tree(and_left, predicate) or predicate_in_predicate_tree(and_right, predicate)
        case CompPredicate(_, comp_predicate):
            return predicate_in_predicate_tree(comp_predicate, predicate)
        case OrPredicate(or_left, or_right):
            return predicate_in_predicate_tree(or_left, predicate) or predicate_in_predicate_tree(or_right, predicate)
        case PredicateFactory() as factory:
            return factory.predicate == predicate
        case _ if tree == predicate:
            return True
        case _:
            return False
