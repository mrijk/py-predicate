import pytest

from generator.generate_false.helpers import assert_generated_false
from predicate import exactly_n, is_int_p, is_str_p, match_p


@pytest.mark.parametrize(
    "predicates",
    [
        (is_int_p,),
        (is_int_p, is_str_p),
        (exactly_n(3, is_int_p),),
    ],
)
def test_generate_match(predicates):
    predicate = match_p(*predicates)

    assert_generated_false(predicate)


def test_generate_match_exactly_n_is_false_every_time():
    # A list with 3 leading ints matches exactly_n(3, is_int_p), so a false value must not be a long list whose only
    # false item comes late. Repeated, as one draw of values could be lucky.
    for _ in range(50):
        assert_generated_false(match_p(exactly_n(3, is_int_p)))
