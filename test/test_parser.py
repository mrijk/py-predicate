import pytest

from predicate import always_false_p, always_true_p, ge_p
from predicate.implies import Implies
from predicate.named_predicate import NamedPredicate
from predicate.parser import parse_expression


@pytest.fixture
def p():
    return NamedPredicate(name="p")


@pytest.fixture
def q():
    return NamedPredicate(name="q")


@pytest.fixture
def r():
    return NamedPredicate(name="r")


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


def test_parser_grouped(p, q, r):
    expression = "p & (q | r)"

    predicate = parse_expression(expression)

    assert predicate == p & (q | r)


def test_parser_implies(p, q):
    expression = "p => q"

    predicate = parse_expression(expression)

    assert predicate == Implies(p, q)


def test_parser_failure(p, q):
    expression = "p ^"

    predicate = parse_expression(expression)

    assert predicate is None


def test_parser_ge_p():
    expression = "ge_p(2)"

    predicate = parse_expression(expression)

    assert predicate == ge_p(2)


def test_parser_gt_p():
    expression = "gt_p(2)"

    with pytest.raises(Exception):  # noqa: B017
        parse_expression(expression)
