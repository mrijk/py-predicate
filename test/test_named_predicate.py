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


def test_to_named_predicate_not():
    eq_2 = eq_p(2)

    predicate = to_named_predicate(~eq_2)

    assert predicate == ~NamedPredicate(name="p1")


def test_to_named_predicate_not_preserves_inner_predicate():
    # ~eq_p(2) & ~eq_p(3) must name the inner predicates independently.
    # If the inner predicate is replaced with None both nots share the same
    # name, giving ~p1 & ~p1 instead of the correct ~p1 & ~p2.
    predicate = to_named_predicate(~eq_p(2) & ~eq_p(3))
    assert predicate == ~NamedPredicate(name="p1") & ~NamedPredicate(name="p2")
