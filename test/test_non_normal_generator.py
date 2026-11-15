import math
import sys
from itertools import islice

from predicate import generate_false, is_normal_p


def test_non_normal_generation_reaches_all_special_value_categories():
    values = list(islice(generate_false(is_normal_p), 20))
    assert len(values) == 20
    assert all(not is_normal_p(value) for value in values)
    assert any(value == 0.0 for value in values)
    assert math.inf in values
    assert -math.inf in values
    assert any(math.isnan(value) for value in values)
    assert any(0 < abs(value) < sys.float_info.min for value in values)
