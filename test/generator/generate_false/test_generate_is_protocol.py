from generator.generate_false.helpers import assert_generated_false
from predicate import is_protocol_p


def test_generate_is_protocol_false():
    assert_generated_false(is_protocol_p())
