from predicate.predicate import (
    AndPredicate,
    XorPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    NotPredicate,
    Predicate,
    get_as_not_predicate,
    get_as_and_predicate,
)


def optimize_xor_predicate[T](predicate: XorPredicate[T]) -> Predicate[T]:
    from predicate.optimizer.predicate_optimizer import optimize_predicate

    # p ^ False = p
    if isinstance(predicate.right, AlwaysFalsePredicate):
        return optimize_predicate(predicate.left)

    # False ^ p = p
    if isinstance(predicate.left, AlwaysFalsePredicate):
        return optimize_predicate(predicate.right)

    # p ^ True = ~p
    if isinstance(predicate.right, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=predicate.left))

    # True ^ p = ~p
    if isinstance(predicate.left, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=predicate.right))

    # p ^ p == False
    if predicate.left == predicate.right:
        return AlwaysFalsePredicate()

    # ~p ^ p == True
    if not_predicate := get_as_not_predicate(predicate.left):
        if predicate.right == not_predicate.predicate:
            return AlwaysTruePredicate()

    # p ^ ~p == True
    if not_predicate := get_as_not_predicate(predicate.right):
        if predicate.left == not_predicate.predicate:
            return AlwaysTruePredicate()

    if and_predicate := get_as_and_predicate(predicate.right):
        # p ^ (^p & q) == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if predicate.left == not_predicate.predicate:
                return NotPredicate(
                    AndPredicate(left=predicate.left, right=and_predicate.right)
                )
        # p ^ (q & ^p) == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.right):
            if predicate.left == not_predicate.predicate:
                return NotPredicate(
                    AndPredicate(left=predicate.left, right=and_predicate.left)
                )

    if and_predicate := get_as_and_predicate(predicate.left):
        # (^p & q) ^ p == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if predicate.right == not_predicate.predicate:
                return NotPredicate(
                    AndPredicate(left=predicate.right, right=and_predicate.right)
                )
        # (q & ^p) ^ p == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.right):
            if predicate.right == not_predicate.predicate:
                return NotPredicate(
                    AndPredicate(left=predicate.right, right=and_predicate.left)
                )

    return optimize_predicate(predicate)
