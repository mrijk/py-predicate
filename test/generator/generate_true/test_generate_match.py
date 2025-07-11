import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import exactly_n, is_bool_p, is_float_p, is_int_p, is_str_p, match_p


@pytest.mark.parametrize(
    "predicates",
    [
        (is_int_p,),
        (is_int_p, is_str_p),
        (exactly_n(3, is_int_p),),
        (exactly_n(3, is_int_p), is_bool_p, exactly_n(2, is_float_p), is_str_p),
    ],
)
def test_generate_match(predicates):
    predicate = match_p(*predicates)

    assert_generated_true(predicate)
