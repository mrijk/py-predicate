from predicate import eq_p
from predicate.named_predicate import NamedPredicate, to_named_predicate


def test_to_named_predicate(p):
    predicate = to_named_predicate(p)

    assert predicate == p


def test_to_named_predicate_with_rename():
    eq_2 = eq_p(2)

    predicate = to_named_predicate(eq_2)

    assert predicate == NamedPredicate(name="p1")


def test_to_named_predicate_or():
    eq_2 = eq_p(2)
    eq_3 = eq_p(3)

    predicate = to_named_predicate(eq_2 | eq_3)

    assert predicate == NamedPredicate(name="p1") | NamedPredicate(name="p2")


def test_to_named_predicate_same():
    p = eq_p(2)
    q = eq_p(2)

    predicate = to_named_predicate(p | q)

    assert predicate == NamedPredicate(name="p1") | NamedPredicate(name="p1")
