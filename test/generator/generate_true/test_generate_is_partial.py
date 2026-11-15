from generator.generate_true.helpers import assert_generated_true
from predicate.is_partial_predicate import is_partial_p, is_partial_with_signature_p


def test_generate_is_partial():
    assert_generated_true(is_partial_p)


def test_generate_is_partial_with_signature():
    assert_generated_true(is_partial_with_signature_p(nr_of_parameters=2))
