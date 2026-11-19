import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import always_false_p, ge_p, is_str_p, is_struct_p


@pytest.mark.parametrize(
    "required, optional",
    [
        ({"name": is_str_p, "age": ge_p(0)}, {}),
        ({"name": is_str_p, "age": ge_p(0)}, {"email": is_str_p}),
    ],
)
def test_generate_is_struct(required, optional):
    predicate = is_struct_p(required=required, optional=optional)
    assert_generated_true(predicate)


def test_optional_field_without_values_is_left_out():
    predicate = is_struct_p(optional={"x": always_false_p})

    assert_generated_true(predicate)
