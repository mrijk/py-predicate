from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate, always_false_p
from predicate.always_true_predicate import AlwaysTruePredicate, always_true_p
from predicate.eq_predicate import EqPredicate
from predicate.fn_predicate import FnPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.implies import implies
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_predicates import InPredicate, IsSubsetPredicate, NotInPredicate


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> MaybeOptimized[T]:
    from predicate.negate import negate
    from predicate.optimizer.predicate_optimizer import optimizations, optimize

    match left := optimize(predicate.left), right := optimize(predicate.right):
        case _, AlwaysFalsePredicate():  # p & False == False
            return Optimized(predicate=always_false_p)
        case AlwaysFalsePredicate(), _:  # False & p == False
            return Optimized(predicate=always_false_p)
        case _, AlwaysTruePredicate():  # p & True == p
            return Optimized(predicate=left)
        case AlwaysTruePredicate(), _:  # True & p == p
            return Optimized(predicate=right)
        case _, _ if left == right:  # p & p == p
            return Optimized(predicate=left)
        case _, _ if left == negate(right):
            return Optimized(predicate=always_false_p)  # p & ~p == False

        # comparison optimizations
        case GePredicate(v1), LePredicate(v2) if v1 < v2:
            return Optimized(GeLePredicate(lower=v1, upper=v2))
        case GePredicate(v1), LePredicate(v2) if v1 == v2:
            return Optimized(EqPredicate(v=v1))
        case GePredicate(v1), LtPredicate(v2) if v1 < v2:
            return Optimized(GeLtPredicate(lower=v1, upper=v2))
        case GtPredicate(v1), LePredicate(v2) if v1 < v2:
            return Optimized(GtLePredicate(lower=v1, upper=v2))
        case GtPredicate(v1), LtPredicate(v2) if v1 < v2:
            return Optimized(GtLtPredicate(lower=v1, upper=v2))

        # misc optimizations
        case AllPredicate(left_all), AllPredicate(right_all):
            # All(p1) & All(p2) => All(p1 & p2)
            return Optimized(optimize(AllPredicate(predicate=optimize(AndPredicate(left=left_all, right=right_all)))))
        case IsInstancePredicate(klass_left), IsInstancePredicate(klass_right) if klass_left != klass_right:
            return Optimized(always_false_p)
        case IsSubsetPredicate(v1), IsSubsetPredicate(v2):
            return Optimized(IsSubsetPredicate(v) if (v := v1 & v2) else always_false_p)
        case FnPredicate(predicate_fn), EqPredicate(v):
            return Optimized(always_true_p if predicate_fn(v) else always_false_p)

        # set optimizations
        case InPredicate(v1), InPredicate(v2):
            if v := v1 & v2:
                return Optimized(optimize(InPredicate(v=v)))
            return Optimized(always_false_p)
        case InPredicate(v1), NotInPredicate(v2):
            if v := v1 - v2:
                return Optimized(optimize(InPredicate(v=v)))
            return Optimized(always_false_p)
        case NotInPredicate(v1), NotInPredicate(v2) if v := v1 | v2:
            return Optimized(optimize(NotInPredicate(v=v)))

        # recursive & optimizations
        case AndPredicate(and_left, and_right), _:
            match optimizations(and_left & right):
                case Optimized(optimized):
                    return Optimized(predicate=optimize(optimized & and_right))
                case _:
                    match optimizations(and_right & right):
                        case Optimized(optimized):
                            return Optimized(optimize(optimized & and_left))
                        case _:
                            return NotOptimized()
        case _, AndPredicate():
            return optimize_and_predicate(AndPredicate(right, left))

        case OrPredicate(or_left, or_right), _:
            match or_left, or_right:
                case NotPredicate(not_predicate), _ if not_predicate == right:  # (~p | q) & p == q & p
                    return Optimized(AndPredicate(left=or_right, right=right))
                case _, NotPredicate(not_predicate) if not_predicate == right:  # (q | ~p) & p == q & p
                    return Optimized(AndPredicate(left=or_left, right=right))

        case _, OrPredicate():
            return optimize_and_predicate(AndPredicate(left=right, right=left))

        # implies optimizations
        case _, _ if implies(left, right):
            return Optimized(left)  # p => q and (p & q) results in q
        case _, _ if implies(right, left):
            return Optimized(right)  # q => p and (p & q) results in p
        case _, _ if implies(left, negate(right)) or implies(right, negate(left)):
            return Optimized(always_false_p)

    return Optimized(left & right) if (left != predicate.left or right != predicate.right) else NotOptimized()
