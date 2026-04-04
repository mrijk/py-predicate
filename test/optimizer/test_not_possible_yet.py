import pytest

# This test file contains predicates that are not optimized yet
from predicate import can_optimize


@pytest.mark.skip
def test_not_possible_1(p, q, r):
    # (p & q) | (p & r) = p & (q | r)

    predicate = (p & q) | (p & r)

    assert not can_optimize(predicate)


@pytest.mark.skip
def test_not_possible_2(p, q, r):
    # (p | q) & (p | r) = p | (q & r)

    predicate = (p | q) & (p | r)

    assert not can_optimize(predicate)


@pytest.mark.skip
def test_not_possible_11(p, q, r):
    # (p & q) | (q & r) = q & (p | r)  [q is the common factor on the right/left]

    predicate = (p & q) | (q & r)

    assert not can_optimize(predicate)
