from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.eq_predicate import EqPredicate
from predicate.fn_predicate import FnPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.implies import implies
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.optimizer.in_optimizer import optimize_in_predicate, optimize_not_in_predicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, Predicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_predicates import InPredicate, IsSubsetPredicate, NotInPredicate


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
            return always_false_p  # p & ~p == False

    match left := optimize(left), right := optimize(right):
        case _, AlwaysTruePredicate():  # p & True == p
            return left
        case AlwaysTruePredicate(), _:  # True & p == p
            return right

        case GePredicate(v1), LePredicate(v2) if v1 < v2:
            return GeLePredicate(lower=v1, upper=v2)
        case GePredicate(v1), LePredicate(v2) if v1 == v2:
            return EqPredicate(v=v1)

        case GePredicate(v1), LtPredicate(v2) if v1 < v2:
            return GeLtPredicate(lower=v1, upper=v2)

        case GtPredicate(v1), LePredicate(v2) if v1 < v2:
            return GtLePredicate(lower=v1, upper=v2)

        case GtPredicate(v1), LtPredicate(v2) if v1 < v2:
            return GtLtPredicate(lower=v1, upper=v2)

        case IsInstancePredicate(klass_left), IsInstancePredicate(klass_right) if klass_left != klass_right:
            return always_false_p

        case IsSubsetPredicate(v1), IsSubsetPredicate(v2):
            return IsSubsetPredicate(v) if (v := v1 & v2) else always_false_p

        case FnPredicate(predicate_fn), EqPredicate(v):
            return always_true_p if predicate_fn(v) else always_false_p

        case InPredicate(v1), InPredicate(v2):
            if v := v1 & v2:
                return optimize_in_predicate(InPredicate(v=v))
            return always_false_p

        case InPredicate(v1), NotInPredicate(v2):
            if v := v1 - v2:
                return optimize_in_predicate(InPredicate(v=v))
            return always_false_p

        case NotInPredicate(v1), NotInPredicate(v2) if v := v1 | v2:
            return optimize_not_in_predicate(NotInPredicate(v=v))

        case AllPredicate(left_all), AllPredicate(right_all):
            # All(p1) & All(p2) => All(p1 & p2)
            return optimize(AllPredicate(predicate=optimize(AndPredicate(left=left_all, right=right_all))))

        case _, _ if implies(left, right):
            return left  # p => q and (p & q) results in q

        case _, _ if implies(right, left):
            return right  # q => p and (p & q) results in p

        case _, _ if implies(left, negate(right)) or implies(right, negate(left)):
            return always_false_p

        case _, _ if and_contains_negate(predicate, right):
            return always_false_p  # p & q & ... & ~p == False

        case _, _ if and_contains_negate(predicate, left):
            return always_false_p  # q & p & ... & ~p == False

        case _, _ if left == right:  # p & p == p
            return left

        case _:
            return AndPredicate(left=left, right=right)


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
