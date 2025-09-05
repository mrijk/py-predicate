import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import is_subclass_p


@pytest.mark.parametrize(
    "parameter",
    [
        int,
        (int, str),
        int | str,
        object,
    ],
)
def test_generate_is_subclass(parameter):
    predicate = is_subclass_p(parameter)
    assert_generated_true(predicate)
