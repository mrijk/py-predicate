from predicate.optimizer.and_optimizer import optimize_and_predicate
from predicate.optimizer.not_optimizer import optimize_not_predicate
from predicate.optimizer.or_optimizer import optimize_or_predicate
from predicate.optimizer.rules import optimization_rules
from predicate.optimizer.xor_optimizer import optimize_xor_predicate
from predicate.predicate import (
    Predicate,
    NotPredicate,
    AlwaysTruePredicate,
    AlwaysFalsePredicate,
    AndPredicate,
    OrPredicate,
    XorPredicate,
)


def optimize[T](predicate: Predicate[T]) -> Predicate[T]:
    match predicate:
        case AndPredicate() as and_predicate:
            return optimize_and_predicate(and_predicate)
        case NotPredicate() as not_predicate:
            return optimize_not_predicate(not_predicate)
        case OrPredicate() as or_predicate:
            return optimize_or_predicate(or_predicate)
        case XorPredicate() as xor_predicate:
            return optimize_xor_predicate(xor_predicate)
        case _:
            return predicate


def predicate_matches_rule(predicate: Predicate | None, rule: Predicate | None) -> bool:
    match predicate, rule:
        case _, None:
            return True
        case NotPredicate() as predicate_child, NotPredicate() as rule_child:
            return predicate_matches_rule(
                predicate_child.predicate, rule_child.predicate
            )
        case OrPredicate() as predicate_child, OrPredicate() as rule_child:
            return predicate_matches_rule(
                predicate_child.left, rule_child.left
            ) and predicate_matches_rule(predicate_child.right, rule_child.right)
        case Predicate() as p1, Predicate() as p2 if type(p1) == type(p2):
            return True
        case _, _:
            return False
    return False


def match(predicate: Predicate) -> dict | None:
    for rule in optimization_rules:
        if predicate_matches_rule(predicate, rule["from"]):
            return rule

    return None


def can_optimize[T](predicate: Predicate[T]) -> bool:
    return optimize(predicate) != predicate


def optimize_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    if predicate.always_true:
        return AlwaysTruePredicate()
    if predicate.always_false:
        return AlwaysFalsePredicate()
    return predicate
