from generator.generate_false.helpers import assert_generated_false
from predicate import comp_p, ge_p


def test_generate_comp():
    assert_generated_false(comp_p(fn=lambda x: 2 * x, predicate=ge_p(2)))
