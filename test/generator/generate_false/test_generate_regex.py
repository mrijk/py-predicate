import pytest

from generator.generate_false.helpers import assert_generated_false
from predicate import regex_p


@pytest.mark.parametrize(
    "pattern",
    [
        r"\d+",
        r"[a-z]+",
        r"foo|bar",
    ],
)
def test_generate_regex(pattern):
    predicate = regex_p(pattern)

    assert_generated_false(predicate)
