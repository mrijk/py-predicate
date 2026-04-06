from generator.generate_false.helpers import assert_generated_false
from predicate import raises_exception_p, raises_p


def test_generate_raises_p():
    assert_generated_false(raises_p)


def test_generate_raises_exception_p():
    assert_generated_false(raises_exception_p(ValueError))
