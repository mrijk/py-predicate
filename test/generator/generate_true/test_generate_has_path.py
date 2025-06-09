from generator.generate_true.helpers import assert_generated_true
from predicate import eq_p, has_path_p


def test_generate_has_path():
    has_x = eq_p("x")
    predicate = has_path_p(has_x)

    assert_generated_true(predicate)
