from predicate import all_p, eq_p, is_instance_p
from predicate.constructor.mutate import mutations
from predicate.eq_predicate import EqPredicate


def test_mutate_eq_p():
    eq_2 = eq_p(2)

    result = mutations(eq_2, false_set=[1], true_set=[2])

    all_different = all_p(is_instance_p(EqPredicate))

    assert all_different(result)
