import pytest

from predicate import all_p, eq_p, ge_p, gt_p, is_instance_p, le_p, lt_p, ne_p
from predicate.constructor.mutate import mutations
from predicate.eq_predicate import EqPredicate


@pytest.mark.skip
def test_mutate_eq_p():
    eq_2 = eq_p(2)

    result = mutations(eq_2, false_set=[1], true_set=[2])

    all_different = all_p(is_instance_p(EqPredicate))

    assert all_different(result)


@pytest.mark.parametrize(
    "predicate",
    [
        eq_p("foo"),
        ne_p("foo"),
        ge_p("foo"),
        gt_p("foo"),
        le_p("foo"),
        lt_p("foo"),
    ],
)
@pytest.mark.skip
def test_mutate_non_int(predicate):
    assert list(mutations(predicate, false_set=["bar"], true_set=["foo"])) == []
