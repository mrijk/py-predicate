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
    from predicate.optimizer.predicate_optimizer import optimize_predicate, optimize

    left = optimize(predicate.left)
    right = optimize(predicate.right)

    # False ^ False = False

    if isinstance(left, AlwaysFalsePredicate) and isinstance(
        right, AlwaysFalsePredicate
    ):
        return AlwaysFalsePredicate()

    # True ^ True = False

    if isinstance(left, AlwaysTruePredicate) and isinstance(right, AlwaysTruePredicate):
        return AlwaysFalsePredicate()

    # p ^ False = p
    if isinstance(right, AlwaysFalsePredicate):
        return optimize_predicate(left)

    # False ^ p = p
    if isinstance(left, AlwaysFalsePredicate):
        return optimize_predicate(right)

    # p ^ True = ~p
    if isinstance(right, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=left))

    # True ^ p = ~p
    if isinstance(left, AlwaysTruePredicate):
        return optimize_predicate(NotPredicate(predicate=right))

    # p ^ p == False
    if left == right:
        return AlwaysFalsePredicate()

    # ~p ^ p == True
    if not_predicate := get_as_not_predicate(left):
        if right == not_predicate.predicate:
            return AlwaysTruePredicate()

    # p ^ ~p == True
    if not_predicate := get_as_not_predicate(right):
        if left == not_predicate.predicate:
            return AlwaysTruePredicate()

    if and_predicate := get_as_and_predicate(right):
        # p ^ (^p & q) == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if left == not_predicate.predicate:
                return NotPredicate(AndPredicate(left=left, right=and_predicate.right))
        # p ^ (q & ^p) == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.right):
            if left == not_predicate.predicate:
                return NotPredicate(
                    AndPredicate(left=predicate.left, right=and_predicate.left)
                )

    if and_predicate := get_as_and_predicate(left):
        # (^p & q) ^ p == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.left):
            if right == not_predicate.predicate:
                return NotPredicate(AndPredicate(left=right, right=and_predicate.right))
        # (q & ^p) ^ p == ~(p | q)
        if not_predicate := get_as_not_predicate(and_predicate.right):
            if right == not_predicate.predicate:
                return NotPredicate(AndPredicate(left=right, right=and_predicate.left))

    return optimize_predicate(predicate)
