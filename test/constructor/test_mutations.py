from predicate import all_p, eq_p, ge_p, gt_p, is_instance_p, le_p, lt_p, ne_p
from predicate.constructor.mutate import mutations
from predicate.eq_predicate import EqPredicate


def test_mutate_eq_p():
    eq_2 = eq_p(2)

    result = mutations(eq_2, false_set=[1], true_set=[2])

    all_different = all_p(is_instance_p(EqPredicate))

    assert all_different(result)


def test_mutate_eq_p_non_int():
    assert list(mutations(eq_p("foo"), false_set=["bar"], true_set=["foo"])) == []


def test_mutate_ne_p_non_int():
    assert list(mutations(ne_p("foo"), false_set=["foo"], true_set=["bar"])) == []


def test_mutate_ge_p_non_int():
    assert list(mutations(ge_p("foo"), false_set=[], true_set=["bar"])) == []


def test_mutate_gt_p_non_int():
    assert list(mutations(gt_p("foo"), false_set=[], true_set=["bar"])) == []


def test_mutate_le_p_non_int():
    assert list(mutations(le_p("foo"), false_set=[], true_set=["bar"])) == []


def test_mutate_lt_p_non_int():
    assert list(mutations(lt_p("foo"), false_set=[], true_set=["bar"])) == []
