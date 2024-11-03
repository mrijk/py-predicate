from predicate.optimizer.all_optimizer import optimize_all_predicate
from predicate.optimizer.and_optimizer import optimize_and_predicate
from predicate.optimizer.any_optimizer import optimize_any_predicate
from predicate.optimizer.not_optimizer import optimize_not_predicate
from predicate.optimizer.or_optimizer import optimize_or_predicate
from predicate.optimizer.rules import WildcardPredicate, optimization_rules
from predicate.optimizer.xor_optimizer import optimize_xor_predicate
from predicate.predicate import (
    AllPredicate,
    AndPredicate,
    AnyPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)


def optimize[T](predicate: Predicate[T]) -> Predicate[T]:
    match predicate:
        case AllPredicate() as all_predicate:
            return optimize_all_predicate(all_predicate)
        case AndPredicate() as and_predicate:
            return optimize_and_predicate(and_predicate)
        case AnyPredicate() as any_predicate:
            return optimize_any_predicate(any_predicate)
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
        case AndPredicate(and_left, and_right), AndPredicate(rule_left, rule_right):
            return predicate_matches_rule(and_left, rule_left) and predicate_matches_rule(and_right, rule_right)
        case NotPredicate(not_predicate), NotPredicate(rule_predicate):
            return predicate_matches_rule(not_predicate, rule_predicate)
        case OrPredicate() as predicate_child, OrPredicate() as rule_child:
            return predicate_matches_rule(predicate_child.left, rule_child.left) and predicate_matches_rule(
                predicate_child.right, rule_child.right
            )
        case _, WildcardPredicate():
            return True
        case Predicate() as p1, Predicate() as p2 if p1 == p2:
            return True
    return False


def match(predicate: Predicate) -> dict | None:
    for rule in optimization_rules:
        if predicate_matches_rule(predicate, rule["from"]):  # type: ignore
            return rule

    return None


def can_optimize[T](predicate: Predicate[T]) -> bool:
    return optimize(predicate) != predicate
