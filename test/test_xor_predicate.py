from functools import partial
from operator import ge
from typing import cast

from predicate import ge_p, is_predicate_p
from predicate.xor_predicate import XorPredicate


def test_xor():
    # p ^ q
    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    predicate = ge_2 ^ ge_4

    assert not predicate(1)
    assert not predicate(4)
    assert predicate(2)


def test_xor_callable_right():
    # p ^ q
    ge_2 = partial(ge, 2)
    ge_4 = ge_p(4)

    predicate = ge_2 ^ ge_4

    assert is_predicate_p(cast(XorPredicate, predicate).right)


def test_xor_callable_left():
    # p ^ q
    ge_2 = ge_p(2)

    def ge_4(x):
        return x >= 4

    predicate = ge_2 ^ ge_4

    assert is_predicate_p(cast(XorPredicate, predicate).right)


def test_xor_commutative():
    # p ^ q == q ^ p
    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    predicate = ge_2 ^ ge_4

    assert not predicate(1)
    assert not predicate(4)
    assert predicate(2)

    ge_4_xor_ge_4 = ge_4 ^ ge_2

    assert not ge_4_xor_ge_4(1)
    assert not ge_4_xor_ge_4(4)
    assert ge_4_xor_ge_4(2)


def test_xor_eq(p, q):
    assert p ^ q == q ^ p
