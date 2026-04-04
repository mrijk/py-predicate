import pytest
from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from predicate import all_p, eq_p, ge_le_p, generate_false, has_length_p, is_int_p, is_str_p, le_p


@pytest.mark.parametrize(
    "length_p",
    [
        eq_p(2),
        le_p(2),
    ],
)
def test_generate_false_has_length_p(length_p):
    predicate = has_length_p(length_p=length_p)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "length_p, value_p",
    [
        (eq_p(2), is_int_p),
        (ge_le_p(lower=1, upper=3), is_str_p),
    ],
)
def test_generate_has_length_p_with_klass(length_p, value_p):
    predicate = has_length_p(length_p=length_p)
    values_p = all_p(value_p)

    values = take(5, generate_false(predicate, value_p=value_p))
    assert values

    for value in values:
        assert not predicate(value)
        assert values_p(value)
