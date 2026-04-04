from generator.generate_false.helpers import assert_generated_false
from predicate import count_p, eq_p, ge_p


def test_generate_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert_generated_false(predicate)
