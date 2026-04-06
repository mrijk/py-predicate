from generator.generate_false.helpers import assert_generated_false
from predicate import eq_p, has_path_p


def test_generate_has_path():
    predicate = has_path_p(eq_p("x"))

    assert_generated_false(predicate)


def test_generate_has_path_two_steps():
    predicate = has_path_p(eq_p("x"), eq_p("y"))

    assert_generated_false(predicate)


def test_generate_has_path_three_steps():
    predicate = has_path_p(eq_p("x"), eq_p("y"), eq_p("z"))

    assert_generated_false(predicate)
