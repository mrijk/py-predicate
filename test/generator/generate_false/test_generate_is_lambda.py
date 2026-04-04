import pytest

from generator.generate_false.helpers import assert_generated_false
from predicate import is_lambda_p, is_lambda_with_signature_p


def test_generate_is_lambda():
    predicate = is_lambda_p
    assert_generated_false(predicate)


@pytest.mark.parametrize("nr_of_parameters", list(range(1, 5)))
def test_generate_is_lambda_with_signature(nr_of_parameters):
    predicate = is_lambda_with_signature_p(nr_of_parameters=nr_of_parameters)
    assert_generated_false(predicate)
