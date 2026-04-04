import pytest

from generator.generate_true.helpers import assert_generated_true
from predicate import eq_p, ge_p, has_path_p, is_int_p, is_list_p


@pytest.mark.parametrize(
    "path",
    [[eq_p("x")], [eq_p("x"), is_int_p], [eq_p("x"), eq_p("y"), eq_p(13)], [eq_p("x"), is_list_p, eq_p("y"), ge_p(2)]],
)
def test_generate_has_path(path):
    predicate = has_path_p(*path)

    assert_generated_true(predicate)
