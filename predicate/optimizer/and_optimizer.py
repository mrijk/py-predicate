from predicate.predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    InPredicate,
    NePredicate,
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
        case _, AlwaysFalsePredicate():  # p & False = False
            return AlwaysFalsePredicate()
        case AlwaysFalsePredicate(), _:  # False & p = False
            return AlwaysFalsePredicate()
        case _, AlwaysTruePredicate():  # p & True == p
            return optimize(left)
        case AlwaysTruePredicate(), _:  # True & p == p
            return optimize(right)

        case EqPredicate(v1), EqPredicate(v2) if v1 == v2:
            # x = v1 & x = v2 & v1 == v2 => x = v1
            return left
        case EqPredicate(v1), EqPredicate(v2) if v1 != v2:
            # x = v1 & x = v2 & v1 != v2 => False
            return AlwaysFalsePredicate()
        case EqPredicate(v1), GePredicate(v2) if v1 == v2:
            # x = v1 & x >= v2 & v1 = v2 => x = v1
            return left
        case EqPredicate(v1), GePredicate(v2) if v1 < v2:
            # x = v1 & x >= v2 & v1 < v2 => False
            return AlwaysFalsePredicate()
        case GePredicate(v1), GePredicate(v2):
            # x >= v1 & x >= v2 => x >= max(v1, v2)
            return GePredicate(v=max(v1, v2))

        case FnPredicate(predicate_fn), EqPredicate(v):
            return AlwaysTruePredicate() if predicate_fn(v) else AlwaysFalsePredicate()

        case InPredicate(v1), InPredicate(v2):
            v = v1 & v2
            if not v:
                return AlwaysFalsePredicate()
            if len(v) == 1:
                return EqPredicate(v=v.pop())
            return InPredicate(v=v)

        case InPredicate(v1), NotInPredicate(v2):
            v = v1 - v2
            if not v:
                return AlwaysFalsePredicate()
            if len(v) == 1:
                return EqPredicate(v=v.pop())
            return InPredicate(v=v)

        case NotInPredicate(v1), NotInPredicate(v2):
            v = v1 | v2
            if not v:
                return AlwaysTruePredicate()
            if len(v) == 1:
                return NePredicate(v=v.pop())
            return NotInPredicate(v=v)

        case AllPredicate(left_all), AllPredicate(right_all):
            # All(p1) & All(p2) => All(p1 & p2)
            return optimize(AllPredicate(predicate=optimize(AndPredicate(left=left_all, right=right_all))))

        case _, _ if and_contains_negate(predicate, right):
            return AlwaysFalsePredicate()  # p & q & ... & ~p == False

        case _, _ if and_contains_negate(predicate, left):
            return AlwaysFalsePredicate()  # q & p & ... & ~p == False

        case _, _ if left == negate(right):
            return AlwaysFalsePredicate()  # p & ~p == False

        case _, _ if left == right:  # p & p == p
            return left

        case _:
            # return AndPredicate(left=left, right=right)
            return predicate


def and_contains_negate(predicate: AndPredicate, sub_predicate: Predicate) -> bool:
    from predicate.negate import negate

    match left := predicate.left, right := predicate.right:
        case AndPredicate() as and_left, _:
            return and_contains_negate(and_left, sub_predicate)
        case _, AndPredicate() as and_right:
            return and_contains_negate(and_right, sub_predicate)
        case AndPredicate() as and_left, AndPredicate() as and_right:
            return and_contains_negate(and_left, sub_predicate) or and_contains_negate(and_right, sub_predicate)
        case _:
            return negate(sub_predicate) in (left, right)
