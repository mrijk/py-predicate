import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import ge_p, is_int_p, lt_p
from predicate.implies import implies_p_p


@pytest.mark.parametrize(
    "predicate", [implies_p_p(ge_p(5), ge_p(0)), implies_p_p(ge_p(0), lt_p(5)), implies_p_p(is_int_p, ge_p(0))]
)
def test_generate_implies(predicate):
    assert_generated_true(predicate)
