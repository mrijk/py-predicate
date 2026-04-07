from predicate.predicate import Predicate


def is_tautology(predicate: Predicate) -> bool:
    """Return True if the predicate is True for all possible inputs."""
    from predicate.always_true_predicate import AlwaysTruePredicate
    from predicate.optimizer.predicate_optimizer import optimize

    return isinstance(optimize(predicate), AlwaysTruePredicate)


def is_satisfiable(predicate: Predicate) -> bool:
    """Return True if the predicate can be True for at least one input."""
    from predicate.always_false_predicate import AlwaysFalsePredicate
    from predicate.optimizer.predicate_optimizer import optimize

    return not isinstance(optimize(predicate), AlwaysFalsePredicate)


def are_equivalent(p: Predicate, q: Predicate) -> bool:
    """Return True if both predicates accept exactly the same values."""
    return is_tautology(~(p ^ q))
