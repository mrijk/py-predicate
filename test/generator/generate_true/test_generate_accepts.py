from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import always_true_p, eq_p, fn_p, generate_true, in_p
from predicate.accepts_predicate import accepts_p


class Foo:
    pass


def test_generate_accepts_eq():
    assert_generated_true(accepts_p(eq_p(2)))
    assert set(take(20, generate_true(accepts_p(eq_p(2))))) == {int}


def test_generate_accepts_or():
    assert_generated_true(accepts_p(eq_p(2) | eq_p("a")))


def test_generate_accepts_in_mixed():
    assert_generated_true(accepts_p(in_p([1, "a"])))


def test_generate_accepts_always_true():
    assert_generated_true(accepts_p(always_true_p))


def test_generate_accepts_no_klass():
    assert_generated_true(accepts_p(fn_p(lambda x: True)))


def test_generate_accepts_own_class():
    predicate = accepts_p(eq_p(Foo()))

    assert_generated_true(predicate)
    assert Foo in take(20, generate_true(predicate))
