import pytest

from predicate import always_false_p


@pytest.mark.parametrize("predicate", [always_false_p])
def test_len_zero(predicate):
    assert predicate.count == 0


def test_len_and(p, q):
    predicate = p & q

    assert predicate.count == 1


def test_len_or(p, q):
    predicate = p | q

    assert predicate.count == 1


def test_len_xor(p, q):
    predicate = p ^ q

    assert predicate.count == 1


def test_len_not(p):
    predicate = ~p

    assert predicate.count == 1


def test_len_and_3(p, q, r, s):
    predicate = p & q & r & s

    assert predicate.count == 3
