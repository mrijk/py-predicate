from generator.generate_true.helpers import assert_generated_true
from predicate import raises_exception_p, raises_p


def test_generate_raises_p():
    assert_generated_true(raises_p)


def test_generate_raises_exception_p():
    assert_generated_true(raises_exception_p(ValueError))
