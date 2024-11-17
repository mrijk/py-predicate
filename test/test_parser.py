import pytest

from predicate import always_false_p, always_true_p
from predicate.parser import parse_expression
from predicate.predicate import NamedPredicate


@pytest.fixture
def p():
    return NamedPredicate(name="p")


@pytest.fixture
def q():
    return NamedPredicate(name="q")


def test_parser_false():
    expression = "false"

    predicate = parse_expression(expression)

    assert predicate == always_false_p


def test_parser_true():
    expression = "true"

    predicate = parse_expression(expression)

    assert predicate == always_true_p


def test_parse_not():
    expression = "~true"

    predicate = parse_expression(expression)

    assert predicate == ~always_true_p


def test_parse_and():
    expression = "true & false"

    predicate = parse_expression(expression)

    assert predicate == always_true_p & always_false_p


def test_parse_or():
    expression = "true | false"

    predicate = parse_expression(expression)

    assert predicate == always_true_p | always_false_p


def test_parse_xor():
    expression = "true ^ false"

    predicate = parse_expression(expression)

    assert predicate == always_true_p ^ always_false_p


def test_parse_and_or():
    expression = "true | false & true"

    predicate = parse_expression(expression)

    assert predicate == always_true_p | always_false_p & always_true_p


def test_parser_named(p):
    expression = "p"

    predicate = parse_expression(expression)

    assert predicate == p


def test_parser_not(p):
    expression = "~p"

    predicate = parse_expression(expression)

    assert predicate == ~p


def test_parser_xor(p, q):
    expression = "p ^ q"

    predicate = parse_expression(expression)

    assert predicate == p ^ q
