from generator.generate_true.helpers import assert_generated_true
from predicate import eq_p, ge_p, is_same_p, lt_p


def test_generate_is_same():
    assert_generated_true(is_same_p(eq_p(1)))
    assert_generated_true(is_same_p(ge_p(1) & lt_p(5)))
