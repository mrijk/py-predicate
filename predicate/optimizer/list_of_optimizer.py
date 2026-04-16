from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.has_length_predicate import is_empty_p
from predicate.is_instance_predicate import is_list_p
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.optimizer.helpers import MaybeOptimized, NotOptimized, Optimized
from predicate.predicate import NotPredicate


def optimize_list_of_predicate[T](predicate: ListOfPredicate[T]) -> MaybeOptimized[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysTruePredicate():
            # is_list_of_p(always_true_p) == is_list_p
            return Optimized(is_list_p)
        case AlwaysFalsePredicate():
            # is_list_of_p(always_false_p) == is_list_p & is_empty_p  (vacuously true only for empty lists)
            return Optimized(is_list_p & is_empty_p)
        case NotPredicate(not_predicate):
            # is_list_of_p(~p) == is_list_p & ~any_p(p)  (De Morgan)
            return Optimized(is_list_p & NotPredicate(predicate=AnyPredicate(predicate=not_predicate)))
        case IsNotNonePredicate():
            return Optimized(is_list_p & NotPredicate(predicate=AnyPredicate(predicate=IsNonePredicate())))
        case _:
            pass

    return NotOptimized() if optimized == predicate.predicate else Optimized(ListOfPredicate(predicate=optimized))
