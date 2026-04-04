import pytest

from generator.generate_false.helpers import assert_generated_false
from predicate import count_p, eq_p, is_int_p, is_str_p, juxt_p


@pytest.mark.skip("TODO")
@pytest.mark.skip
def test_generate_juxt():
    p1 = is_int_p
    p2 = is_str_p
    p3 = eq_p(2)
    p4 = eq_p("foo")
    two_true = count_p(predicate=eq_p(True), length_p=eq_p(2))

    predicate = juxt_p(p1, p2, p3, p4, evaluate=two_true)
    assert_generated_false(predicate)
