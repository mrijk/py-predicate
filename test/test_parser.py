from predicate import always_false_p, always_true_p
from predicate.optimizer.parser import parse_string


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
