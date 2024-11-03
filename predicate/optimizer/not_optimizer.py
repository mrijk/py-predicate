from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsNonePredicate,
    IsNotNonePredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    Predicate,
    XorPredicate,
)


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    # ~~p == p
    match predicate.predicate:
        case NotPredicate(not_predicate):
            return optimize(not_predicate)

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysFalsePredicate():  # ~False = True
            return AlwaysTruePredicate()
        case AlwaysTruePredicate():  # ~True = False
            return AlwaysFalsePredicate()
        case XorPredicate(left, right):
            match left, right:
                case NotPredicate(not_predicate), _:  # ~(~p ^ q) == p ^ q
                    return XorPredicate(left=not_predicate, right=right)
                case _, NotPredicate(not_predicate):  # ~(p ^ ~q) == p ^ q
                    return XorPredicate(left=left, right=not_predicate)
                case _:  # ~(p ^ q) == ~p ^ q
                    return XorPredicate(left=NotPredicate(predicate=left), right=right)
        case EqPredicate(v):
            return NePredicate(v=v)
        case GePredicate(v):  # ~(x >=v) => x < v
            return LtPredicate(v=v)
        case GtPredicate(v):
            return LePredicate(v=v)
        case LePredicate(v):
            return GtPredicate(v=v)
        case LtPredicate(v):
            return GePredicate(v=v)
        case NePredicate(v):
            return EqPredicate(v=v)
        case IsNonePredicate():
            return IsNotNonePredicate()
        case IsNotNonePredicate():
            return IsNonePredicate()

        case InPredicate(v):
            return NotInPredicate(v=v)
        case NotInPredicate(v):
            return InPredicate(v=v)

    return NotPredicate(predicate=optimized)
