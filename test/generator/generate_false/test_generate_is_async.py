from generator.generate_false.helpers import assert_generated_false
from predicate.is_async_predicate import is_async_p


def test_generate_is_async_false():
    assert_generated_false(is_async_p)
