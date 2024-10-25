from predicate.predicate import (
    NotPredicate,
    Predicate,
    XorPredicate,
    get_as_not_predicate,
    get_as_xor_predicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    GePredicate,
    LtPredicate,
    GtPredicate,
    LePredicate,
    NePredicate,
    EqPredicate,
)


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize, optimize_predicate

    # ~~p == p
    if not_predicate := get_as_not_predicate(predicate.predicate):
        return optimize(not_predicate.predicate)

    optimized = optimize(predicate.predicate)

    # ~False = True
    if isinstance(optimized, AlwaysFalsePredicate):
        return AlwaysTruePredicate()

    # ~True = False
    if isinstance(optimized, AlwaysTruePredicate):
        return AlwaysFalsePredicate()

    if xor_predicate := get_as_xor_predicate(optimized):
        match xor_predicate.left, xor_predicate.right:
            case NotPredicate() as not_predicate, _:  # ~(~p ^ q) == p ^ q
                return XorPredicate(
                    left=not_predicate.predicate, right=xor_predicate.right
                )
            case _, NotPredicate() as not_predicate:  # ~(p ^ ~q) == p ^ q
                return XorPredicate(
                    left=xor_predicate.left, right=not_predicate.predicate
                )
            case _, _:  # ~(p ^ q) == ~p ^ q
                return XorPredicate(
                    left=NotPredicate(predicate=xor_predicate.left),
                    right=xor_predicate.right,
                )

    # ~(x >=v) => x < v

    match optimized:
        case EqPredicate(v):
            return NePredicate(v=v)
        case GePredicate(v):
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
            return optimize_predicate(predicate=NotPredicate(predicate=optimized))
