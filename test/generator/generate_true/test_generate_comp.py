from generator.generate_true.helpers import assert_generated_true
from predicate import comp_p, ge_p


def test_generate_comp():
    assert_generated_true(comp_p(fn=lambda x: 2 * x, predicate=ge_p(2)))
