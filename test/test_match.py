import pytest

from predicate import always_false_p, always_true_p, ge_p
from predicate.optimizer.predicate_optimizer import match


@pytest.mark.skip()
def test_match_not_not():
    ge_2 = ge_p(2)

    predicate = ~~ge_2

    rule = match(predicate)

    assert rule is not None


def test_no_match():
    ge_2 = ge_p(2)

    predicate = ~ge_2

    rule = match(predicate)

    assert rule is None


def test_match_not_false():
    predicate = ~always_false_p

    rule = match(predicate)

    assert rule is not None


def test_match_not_true():
    predicate = ~always_true_p

    rule = match(predicate)

    assert rule is not None


def test_match_true_false():
    predicate = always_true_p | always_false_p

    rule = match(predicate)

    assert rule is not None
