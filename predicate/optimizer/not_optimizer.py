from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    EqPredicate,
    GePredicate,
    GtPredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotPredicate,
    Predicate,
    XorPredicate,
    get_as_not_predicate,
)


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize

    # ~~p == p
    if not_predicate := get_as_not_predicate(predicate.predicate):
        return optimize(not_predicate.predicate)

    optimized = optimize(predicate.predicate)

    match optimized:
        case AlwaysFalsePredicate():  # ~False = True
            return AlwaysTruePredicate()
        case AlwaysTruePredicate():  # ~True = False
            return AlwaysFalsePredicate()
        case XorPredicate(left, right):
            match left, right:
                case NotPredicate() as not_predicate, _:  # ~(~p ^ q) == p ^ q
                    return XorPredicate(left=not_predicate.predicate, right=right)
                case _, NotPredicate() as not_predicate:  # ~(p ^ ~q) == p ^ q
                    return XorPredicate(left=left, right=not_predicate.predicate)
                case _, _:  # ~(p ^ q) == ~p ^ q
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
        case _:
            return optimize(predicate=NotPredicate(predicate=optimized))
