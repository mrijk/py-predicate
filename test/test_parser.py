import pytest

from predicate import always_false_p, always_true_p
from predicate.optimizer.parser import parse_string
from predicate.predicate import NamedPredicate


@pytest.fixture
def p():
    return NamedPredicate(name="p")


@pytest.fixture
def q():
    return NamedPredicate(name="q")


def test_parser_false():
    predicate_string = "false"

    predicate = parse_string(predicate_string)

    assert predicate == always_false_p


def test_parser_true():
    predicate_string = "true"

    predicate = parse_string(predicate_string)

    assert predicate == always_true_p


def test_parse_not():
    predicate_string = "~true"

    predicate = parse_string(predicate_string)

    assert predicate == ~always_true_p


def test_parse_and():
    predicate_string = "true & false"

    predicate = parse_string(predicate_string)

    assert predicate == always_true_p & always_false_p


def test_parse_or():
    predicate_string = "true | false"

    predicate = parse_string(predicate_string)

    assert predicate == always_true_p | always_false_p


def test_parse_xor():
    predicate_string = "true ^ false"

    predicate = parse_string(predicate_string)

    assert predicate == always_true_p ^ always_false_p


def test_parse_and_or():
    predicate_string = "true | false & true"

    predicate = parse_string(predicate_string)

    assert predicate == always_true_p | always_false_p & always_true_p


def test_parser_named(p, q):
    expression = "p ^ q"

    predicate = parse_string(expression)

    assert predicate == p ^ q
