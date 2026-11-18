import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import compile_predicate, ge_p, is_int_p, lt_p


@pytest.mark.parametrize("predicate", [ge_p(0), is_int_p, ge_p(0) & lt_p(10)])
def test_generate_compiled(predicate):
    assert_generated_true(compile_predicate(predicate))
