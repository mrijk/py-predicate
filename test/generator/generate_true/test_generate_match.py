import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import is_int_p, is_str_p, match_p


@pytest.mark.parametrize(
    "predicates",
    [
        (is_int_p,),
        (is_int_p, is_str_p),
        # (exactly_n(3, is_int_p), ),
    ],
)
def test_generate_match(predicates):
    predicate = match_p(*predicates)

    assert_generated_true(predicate)
