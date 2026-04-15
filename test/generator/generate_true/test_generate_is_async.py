from generator.generate_true.helpers import assert_generated_true
from predicate.is_async_predicate import is_async_p


def test_generate_is_async():
    assert_generated_true(is_async_p)
