import pytest

from predicate import le_p
from predicate.predicate import NamedPredicate
from predicate.truth_table import get_named_predicates, set_named_values, truth_table


@pytest.fixture
def p():
    return NamedPredicate(name="p")


@pytest.fixture
def q():
    return NamedPredicate(name="q")


def test_truth_table_names(p, q):
    predicate = p & q

    named_predicates = get_named_predicates(predicate)
    assert named_predicates == ["p", "q"]


def test_truth_table_names_invalid(p, q):
    predicate = p & q & le_p(2)

    with pytest.raises(ValueError):
        get_named_predicates(predicate)


def test_truth_table_values_invalid(p, q):
    predicate = p & q & le_p(2)

    with pytest.raises(ValueError):
        values = {"p": True, "q": True}
        set_named_values(predicate, values)


def test_truth_table_and(p, q):
    predicate = p & q

    result = [row[1] for row in truth_table(predicate)]

    assert result == [False, False, False, True]


def test_truth_table_not(p):
    predicate = ~p

    result = [row[1] for row in truth_table(predicate)]

    assert result == [True, False]


def test_truth_table_or(p, q):
    predicate = p | q

    result = [row[1] for row in truth_table(predicate)]

    assert result == [False, True, True, True]


def test_truth_table_xor(p, q):
    predicate = p ^ q

    result = [row[1] for row in truth_table(predicate)]

    assert result == [False, True, True, False]