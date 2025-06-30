import pytest

from generator.generate_false.helpers import assert_generated_false
from predicate import is_int_p, match_p


@pytest.mark.parametrize(
    "predicates",
    [(is_int_p,)],
)
def test_generate_match(predicates):
    predicate = match_p(*predicates)

    assert_generated_false(predicate)
