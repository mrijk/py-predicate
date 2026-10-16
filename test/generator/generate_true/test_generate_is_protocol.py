from generator.generate_true.helpers import assert_generated_true
from predicate import is_protocol_p


def test_generate_is_protocol():
    assert_generated_true(is_protocol_p())
