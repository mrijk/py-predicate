from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from predicate import always_true_p, eq_p, generate_false, in_p
from predicate.accepts_predicate import accepts_p


def test_generate_accepts_eq():
    assert_generated_false(accepts_p(eq_p(2)))


def test_generate_accepts_eq_bool_is_not_int():
    assert bool in take(20, generate_false(accepts_p(eq_p(2))))


def test_generate_accepts_or():
    assert_generated_false(accepts_p(eq_p(2) | eq_p(3)))


def test_generate_accepts_or_mixed_accepts_everything():
    assert not take(5, generate_false(accepts_p(eq_p(2) | eq_p("a"))))


def test_generate_accepts_in():
    assert_generated_false(accepts_p(in_p([1, 2])))


def test_generate_accepts_always_true():
    assert not take(5, generate_false(accepts_p(always_true_p)))
