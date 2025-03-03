# This test file contains predicates that are not optimized yet
from predicate import can_optimize


def test_not_possible_1(p, q, r):
    # (p & q) | (p & r) = p & (q | r)

    predicate = (p & q) | (p & r)

    assert not can_optimize(predicate)
