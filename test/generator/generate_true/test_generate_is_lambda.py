import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import is_lambda_with_signature_p


@pytest.mark.parametrize("nr_of_parameters", list(range(0, 5)))
def test_generate_is_lambda_with_signature(nr_of_parameters):
    predicate = is_lambda_with_signature_p(nr_of_parameters=nr_of_parameters)
    assert_generated_true(predicate)
