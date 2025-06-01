from unittest.mock import Mock

from predicate import all_p, ge_p, tee_p


def test_tee():
    log_fn = Mock()
    log = tee_p(fn=log_fn)

    ge_2 = ge_p(2)

    predicate = all_p(log & ge_2)

    assert predicate(range(2, 5))

    assert log_fn.call_count == 3
