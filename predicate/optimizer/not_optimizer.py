from predicate.predicate import NotPredicate, Predicate


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize, optimize_predicate

    match predicate.predicate:
        case NotPredicate() as p:  # ~~p == p
            return optimize(p.predicate)
        case _:
            return optimize_predicate(
                predicate=NotPredicate(predicate=optimize(predicate.predicate))
            )
