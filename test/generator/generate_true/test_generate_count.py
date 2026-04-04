from generator.generate_true.helpers import assert_generated_true
from predicate import count_p, eq_p, ge_p


def test_generate_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert_generated_true(predicate)
