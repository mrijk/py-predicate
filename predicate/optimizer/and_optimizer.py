from predicate.implies import implies
from predicate.optimizer.in_optimizer import optimize_in_predicate, optimize_not_in_predicate
from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    InPredicate,
    NotInPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
)


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> Predicate[T]:
    from predicate.negate import negate
    from predicate.optimizer.predicate_optimizer import optimize

    match left := predicate.left, right := predicate.right:
        case OrPredicate(or_left, or_right), _:
            match or_left, or_right:
                case NotPredicate(not_predicate), _ if not_predicate == right:  # (~p | q) & p == q & p
                    return AndPredicate(left=or_right, right=right)
                case _, NotPredicate(not_predicate) if not_predicate == right:  # (q | ~p) & p == q & p
                    return AndPredicate(left=or_left, right=right)

        case _, OrPredicate():
            return optimize_and_predicate(AndPredicate(left=right, right=left))

        case _, _ if left == negate(right):
            return AlwaysFalsePredicate()  # p & ~p == False

    match left := optimize(left), right := optimize(right):
        case _, AlwaysTruePredicate():  # p & True == p
            return left
        case AlwaysTruePredicate(), _:  # True & p == p
            return right

        case EqPredicate(v1), EqPredicate(v2) if v1 != v2:
            # x = v1 & x = v2 & v1 != v2 => False
            return AlwaysFalsePredicate()
        case EqPredicate(v1), GePredicate(v2) if v1 > v2:
            # x = v1 & x >= v2 & v1 < v2 => False
            return AlwaysFalsePredicate()

        case FnPredicate(predicate_fn), EqPredicate(v):
            return AlwaysTruePredicate() if predicate_fn(v) else AlwaysFalsePredicate()

        case InPredicate(v1), InPredicate(v2):
            if v := v1 & v2:
                return optimize_in_predicate(InPredicate(v=v))
            return AlwaysFalsePredicate()

        case InPredicate(v1), NotInPredicate(v2):
            if v := v1 - v2:
                return optimize_in_predicate(InPredicate(v=v))
            return AlwaysFalsePredicate()

        case NotInPredicate(v1), NotInPredicate(v2):
            if v := v1 | v2:
                return optimize_not_in_predicate(NotInPredicate(v=v))
            return AlwaysTruePredicate()

        case AllPredicate(left_all), AllPredicate(right_all):
            # All(p1) & All(p2) => All(p1 & p2)
            return optimize(AllPredicate(predicate=optimize(AndPredicate(left=left_all, right=right_all))))

        case _, _ if implies(left, right):
            return left  # p => q and (p & q) results in q

        case _, _ if implies(right, left):
            return right  # q => p and (p & q) results in p

        case _, _ if and_contains_negate(predicate, right):
            return AlwaysFalsePredicate()  # p & q & ... & ~p == False

        case _, _ if and_contains_negate(predicate, left):
            return AlwaysFalsePredicate()  # q & p & ... & ~p == False

        case _, _ if left == right:  # p & p == p
            return left

        case _:
            # return AndPredicate(left=left, right=right)
            return predicate


def and_contains_negate(predicate: AndPredicate, sub_predicate: Predicate) -> bool:
    from predicate.negate import negate

    match left := predicate.left, right := predicate.right:
        # case AndPredicate() as and_left, AndPredicate() as and_right:
        #     return and_contains_negate(and_left, sub_predicate) or and_contains_negate(and_right, sub_predicate)
        case _ if negate(sub_predicate) in (left, right):
            return True
        case AndPredicate() as and_left, _:
            return and_contains_negate(and_left, sub_predicate)
        case _, AndPredicate() as and_right:
            return and_contains_negate(and_right, sub_predicate)
        case _:
            return negate(sub_predicate) in (left, right)
