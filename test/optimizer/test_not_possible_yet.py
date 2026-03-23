# This test file contains predicates that are not optimized yet
from predicate import can_optimize, eq_p, ge_p, gt_p, le_p, lt_p, ne_p, not_in_p


def test_not_possible_1(p, q, r):
    # (p & q) | (p & r) = p & (q | r)

    predicate = (p & q) | (p & r)

    assert not can_optimize(predicate)


def test_not_possible_2(p, q, r):
    # (p | q) & (p | r) = p | (q & r)

    predicate = (p | q) & (p | r)

    assert not can_optimize(predicate)


def test_not_possible_3(p, q):
    # p & (p | q) = p  [absorption law]

    predicate = p & (p | q)

    assert not can_optimize(predicate)


def test_not_possible_4():
    # not_in({1, 2}) | not_in({2, 3}) = not_in({2})  [intersection of exclusion sets]

    predicate = not_in_p({1, 2}) | not_in_p({2, 3})

    assert not can_optimize(predicate)


def test_not_possible_5():
    # ge(2) | le(5) = always_true when lower <= upper

    predicate = ge_p(2) | le_p(5)

    assert not can_optimize(predicate)


def test_not_possible_6():
    # eq(5) | gt(5) = ge(5)

    predicate = eq_p(5) | gt_p(5)

    assert not can_optimize(predicate)


def test_not_possible_7():
    # eq(5) | lt(5) = le(5)

    predicate = eq_p(5) | lt_p(5)

    assert not can_optimize(predicate)


def test_not_possible_8():
    # ne(5) & gt(5) = gt(5)  [gt already implies ne]

    predicate = ne_p(5) & gt_p(5)

    assert not can_optimize(predicate)


def test_not_possible_9():
    # ne(5) & lt(5) = lt(5)  [lt already implies ne]

    predicate = ne_p(5) & lt_p(5)

    assert not can_optimize(predicate)


def test_not_possible_10(p, q):
    # (p ^ q) & p = p & ~q  [xor operand absorbs with AND]

    predicate = (p ^ q) & p

    assert not can_optimize(predicate)


def test_not_possible_11(p, q, r):
    # (p & q) | (q & r) = q & (p | r)  [q is the common factor on the right/left]

    predicate = (p & q) | (q & r)

    assert not can_optimize(predicate)
