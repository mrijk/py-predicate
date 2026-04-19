from generator.generate_true.helpers import assert_generated_true
from predicate.is_callable_predicate import is_callable_p


def test_generate_is_callable_no_params():
    predicate = is_callable_p([], bool)

    assert_generated_true(predicate)


def test_generate_is_callable_with_params():
    predicate = is_callable_p([int, str], bool)

    assert_generated_true(predicate)
