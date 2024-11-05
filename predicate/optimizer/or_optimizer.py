from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    EqPredicate,
    GePredicate,
    InPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
)


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

    match left, right:
        case _, AlwaysFalsePredicate():
            # p | False == p
            return left
        case AlwaysFalsePredicate(), _:
            # False | p == p
            return right
        case _, AlwaysTruePredicate():
            # p | True == True
            return AlwaysTruePredicate()
        case AlwaysTruePredicate(), _:
            # True | p == True
            return AlwaysTruePredicate()

        case AndPredicate(and_left_left, and_left_right), AndPredicate(and_right_left, and_right_right):
            match and_left_left, and_left_right, and_right_left, and_right_right:
                case (
                    NotPredicate(left_not),
                    Predicate() as q,
                    Predicate() as p,
                    NotPredicate(right_not),
                ) if left_not == p and right_not == q:
                    # (~p & q) | (p & ~q) == p ^ q
                    return p ^ q
                case (
                    Predicate() as p,
                    NotPredicate(left_not),
                    NotPredicate(right_not),
                    Predicate() as q,
                ) if left_not == q and right_not == p:
                    # (p & ~q) | (~p & q) == p ^ q
                    return p ^ q

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

        case InPredicate(v1), NotInPredicate(v2):
            v = v2 - (v1 & v2)
            if not v:
                return AlwaysTruePredicate()
            if len(v) == 1:
                return NePredicate(v=v.pop())
            return NotInPredicate(v=v)

        case GePredicate(v1), GePredicate(v2):
            # x >= v1 | x >= v2 => x >= min(v1, v2)
            return GePredicate(v=min(v1, v2))

        case AnyPredicate(left_any), AnyPredicate(right_any):
            return AnyPredicate(optimize(OrPredicate(left=left_any, right=right_any)))

        case _, _ if or_contains_negate(predicate, right):
            return AlwaysTruePredicate()  # p | q | ... | ~p == True

        case _, _ if or_contains_negate(predicate, left):
            return AlwaysTruePredicate()  # q | p | ... | ~p == True

    return OrPredicate(left=left, right=right)


def optimize_or_not[T](left: Predicate[T], right: Predicate[T]) -> Predicate[T] | None:
    from predicate.negate import negate

    match left, right:
        case _, _ if left == negate(right):
            return AlwaysTruePredicate()  # p | ~p == true

    return None


def or_contains_negate(predicate: OrPredicate, sub_predicate: Predicate) -> bool:
    from predicate.negate import negate

    match left := predicate.left, right := predicate.right:
        case OrPredicate() as or_left, _:
            return or_contains_negate(or_left, sub_predicate)
        case _, OrPredicate() as or_right:
            return or_contains_negate(or_right, sub_predicate)
        case OrPredicate() as or_left, OrPredicate() as or_right:
            return or_contains_negate(or_left, sub_predicate) or or_contains_negate(or_right, sub_predicate)
        case _:
            return negate(sub_predicate) in (left, right)
