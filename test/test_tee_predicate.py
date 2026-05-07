from unittest.mock import Mock

from more_itertools import first, one

from predicate import all_p, ge_p, tee_p
from predicate.consumes import consumes
from predicate.generator.generate_true import generate_true


def test_tee():
    log_fn = Mock()
    log = tee_p(fn=log_fn)

    ge_2 = ge_p(2)

    predicate = all_p(log & ge_2)

    assert predicate(range(2, 5))

    assert log_fn.call_count == 3


def test_tee_consumes():
    log_fn = Mock()
    predicate = tee_p(fn=log_fn)

    end = one(consumes(predicate, [1, 2, 3]))

    assert end == 0


def test_tee_generate_true():
    predicate = tee_p(fn=lambda x: None)
    value = first(generate_true(predicate))
    assert predicate(value)
