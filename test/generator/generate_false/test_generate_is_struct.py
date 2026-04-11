import pytest

from generator.generate_false.helpers import assert_generated_false
from predicate import ge_p, is_str_p, is_struct_p


@pytest.mark.parametrize(
    "required, optional",
    [
        ({"name": is_str_p, "age": ge_p(0)}, {}),
        ({"name": is_str_p, "age": ge_p(0)}, {"email": is_str_p}),
    ],
)
def test_generate_is_struct(required, optional):
    predicate = is_struct_p(required=required, optional=optional)
    assert_generated_false(predicate)
