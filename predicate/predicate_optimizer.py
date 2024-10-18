from predicate.predicate import Predicate, NotPredicate, AlwaysTruePredicate, AlwaysFalsePredicate, AndPredicate, \
    get_as_not_predicate, OrPredicate, XorPredicate


def optimize[T](predicate: Predicate[T]) -> Predicate[T]:
    match predicate:
        case AndPredicate() as and_predicate:
            return optimize_and_predicate(and_predicate)
        case NotPredicate() as not_predicate:
            return optimize_not_predicate(not_predicate)
        case OrPredicate() as or_predicate:
            return optimize_or_predicate(or_predicate)
        case XorPredicate() as xor_predicate:
            return optimize_xor_predicate(xor_predicate)
        case _:
            return predicate


def can_optimize[T](predicate: Predicate[T]) -> bool:
    return optimize(predicate) != predicate


def optimize_predicate[T](predicate: Predicate[T]) -> Predicate[T]:
    if predicate.always_true:
        return AlwaysTruePredicate[T]()
    if predicate.always_false:
        return AlwaysFalsePredicate[T]()
    return predicate


def optimize_and_predicate[T](predicate: AndPredicate[T]) -> Predicate[T]:
    # p & p == p
    if predicate.predicate_1 == predicate.predicate_2:
        return optimize(predicate.predicate_1)

    # ~p & p == False
    if predicate_1 := get_as_not_predicate(predicate.predicate_1):
        if predicate.predicate_2 == predicate_1.predicate_1:
            return AlwaysFalsePredicate()

    # p & ~p == False
    if predicate_2 := get_as_not_predicate(predicate.predicate_2):
        if predicate.predicate_1 == predicate_2.predicate_1:
            return AlwaysFalsePredicate()

    return optimize_predicate(predicate)


def optimize_not_predicate[T](predicate: NotPredicate[T]) -> Predicate[T]:
    match predicate.predicate_1:
        case NotPredicate() as p:  # ~~p == p
            return optimize(p.predicate_1)
        case _:
            return optimize_predicate(predicate=NotPredicate(predicate=optimize(predicate.predicate_1)))


def optimize_or_predicate[T](predicate: OrPredicate[T]) -> Predicate[T]:
    # p | p == p
    if predicate.predicate_1 == predicate.predicate_2:
        return optimize(predicate.predicate_1)

    # ~p | p == True
    if predicate_1 := get_as_not_predicate(predicate.predicate_1):
        if predicate.predicate_2 == predicate_1.predicate_1:
            return AlwaysTruePredicate()

    # p | ~p == True
    if predicate_2 := get_as_not_predicate(predicate.predicate_2):
        if predicate.predicate_1 == predicate_2.predicate_1:
            return AlwaysTruePredicate()

    return optimize_predicate(predicate)


def optimize_xor_predicate[T](predicate: XorPredicate[T]) -> Predicate[T]:
    # p ^ False = p
    if isinstance(predicate.predicate_2, AlwaysFalsePredicate):
        return optimize_predicate(predicate.predicate_1)

    # False ^ p = p
    if isinstance(predicate.predicate_1, AlwaysFalsePredicate):
        return optimize_predicate(predicate.predicate_2)

    # p ^ True = ~p
    if isinstance(predicate.predicate_2, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=predicate.predicate_1))

    # True ^ p = ~p
    if isinstance(predicate.predicate_1, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=predicate.predicate_2))

    # p ^ p == False
    if predicate.predicate_1 == predicate.predicate_2:
        return AlwaysFalsePredicate()

    # ~p ^ p == True
    if predicate_1 := get_as_not_predicate(predicate.predicate_1):
        if predicate.predicate_2 == predicate_1.predicate_1:
            return AlwaysTruePredicate()

    # p ^ ~p == True
    if predicate_2 := get_as_not_predicate(predicate.predicate_2):
        if predicate.predicate_1 == predicate_2.predicate_1:
            return AlwaysTruePredicate()

    return optimize_predicate(predicate)