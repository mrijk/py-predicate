from datetime import datetime
from typing import Any

from more_itertools import take

from predicate.generator.helpers import random_predicates


def test_random_predicates_of_any_accept_any_value():
    values = [0, "a", None, 1.5, [1], datetime(2020, 1, 1)]
    for predicate in take(200, random_predicates(klass=Any)):
        for value in values:
            assert predicate(value) in (True, False)
