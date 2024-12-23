from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.optimizer.in_optimizer import optimize_in_predicate, optimize_not_in_predicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate
from predicate.set_predicates import InPredicate, NotInPredicate


def optimize_or_predicate[T](predicate: OrPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    # before optimization

    if optimized := optimize_or_not(left=predicate.left, right=predicate.right):
        return optimized

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    # p | p == p
    if left == right:
        return left

    if optimized := optimize_or_not(left=left, right=right):
        return optimized

    from predicate.implies import implies

    match left, right:
        case _, AlwaysTruePredicate():
            return always_true_p  # p | True == True
        case AlwaysTruePredicate(), _:
            return always_true_p  # True | p == True

        case AndPredicate(and_left_left, and_left_right), AndPredicate(and_right_left, and_right_right):
            match and_left_left, and_left_right, and_right_left, and_right_right:
                case (
                    NotPredicate(left_not),
                    Predicate() as q,
                    Predicate() as p,
                    NotPredicate(right_not),
                ) if left_not == p and right_not == q:
                    return p ^ q  # (~p & q) | (p & ~q) == p ^ q
                case (
                    Predicate() as p,
                    NotPredicate(left_not),
                    NotPredicate(right_not),
                    Predicate() as q,
                ) if left_not == q and right_not == p:
                    return p ^ q  # (p & ~q) | (~p & q) == p ^ q
                case _:
                    return OrPredicate(left=left, right=right)

        case _, AndPredicate(and_left, and_right):
            match and_left:
                case NotPredicate(not_predicate) if not_predicate == left:  # p | (~p & q) == p | q
                    return OrPredicate(left=left, right=and_right)

        case InPredicate(v1), EqPredicate(v2) if v2 not in v1:
            return InPredicate((*v1, v2))
        case EqPredicate(v1), InPredicate(v2) if v1 not in v2:
            return InPredicate((*v2, v1))
        case EqPredicate(v1), EqPredicate(v2) if v1 != v2:
            return InPredicate((v1, v2))

        case EqPredicate(v1), NotInPredicate(v2) if v1 in v2:
            return optimize_not_in_predicate(NotInPredicate(v2 - {v1}))

        case InPredicate(v1), InPredicate(v2) if v := v1 | v2:
            return optimize_in_predicate(InPredicate(v=v))

        case InPredicate(v1), NotInPredicate(v2):
            if v := v2 - (v1 & v2):
                return optimize_not_in_predicate(NotInPredicate(v=v))
            return always_true_p

        case AnyPredicate(left_any), AnyPredicate(right_any):
            return AnyPredicate(optimize(OrPredicate(left=left_any, right=right_any)))

        case _, _ if implies(left, right):
            return right

        case _, _ if implies(right, left):
            return left

        # case _, _ if implies(left, negate(right)):
        #     return negate(left)
        #
        # case _, _ if implies(right, negate(left)):
        #     return negate(right)

        case _, _ if or_contains_negate(predicate, right):
            return always_true_p  # p | q | ... | ~p == True

        case _, _ if or_contains_negate(predicate, left):
            return always_true_p  # q | p | ... | ~p == True

    return OrPredicate(left=left, right=right)


def optimize_or_not[T](left: Predicate[T], right: Predicate[T]) -> Predicate[T] | None:
    from predicate.negate import negate

    match left, right:
        case _, _ if left == negate(right):
            return always_true_p  # p | ~p == true

    return None


def or_contains_negate(predicate: OrPredicate, sub_predicate: Predicate) -> bool:
    from predicate.negate import negate

    match left := predicate.left, right := predicate.right:
        case OrPredicate() as or_left, _:
            return or_contains_negate(or_left, sub_predicate)
        # case _, OrPredicate() as or_right:
        #     return or_contains_negate(or_right, sub_predicate)
        # case OrPredicate() as or_left, OrPredicate() as or_right:
        #     return or_contains_negate(or_left, sub_predicate) or or_contains_negate(or_right, sub_predicate)
        case _:
            return negate(sub_predicate) in (left, right)
