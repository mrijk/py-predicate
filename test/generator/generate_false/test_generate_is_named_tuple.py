from generator.generate_false.helpers import assert_generated_false
from predicate import is_named_tuple_p


def test_generate_is_named_tuple():
    assert_generated_false(is_named_tuple_p)
