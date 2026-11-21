import pytest

from predicate import explain
from predicate.set_predicates import is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p


def test_is_subset():
    predicate = is_subset_p({1, 2, 3})

    assert predicate({1})
    assert predicate({1, 2})
    assert predicate({1, 2, 3})
    assert not predicate({1, 2, 3, 4})


def test_is_real_subset():
    predicate = is_real_subset_p({1, 2, 3})

    assert predicate({1})
    assert predicate({1, 2})
    assert not predicate({1, 2, 3})


def test_is_superset():
    predicate = is_superset_p({1, 2, 3})

    assert not predicate({1, 2})
    assert predicate({1, 2, 3})
    assert predicate({1, 2, 3, 4})


def test_is_real_superset():
    predicate = is_real_superset_p({1, 2, 3})

    assert not predicate({1, 2})
    assert not predicate({1, 2, 3})
    assert predicate({1, 2, 3, 4})


@pytest.mark.parametrize(
    "predicate, value, reason",
    [
        (is_subset_p({1, 2}), {5}, "{5} is not a subset of {1, 2}"),
        (is_real_subset_p({1, 2}), {1, 2}, "{1, 2} is not a real subset of {1, 2}"),
        (is_superset_p({1, 2}), {1}, "{1} is not a superset of {1, 2}"),
        (is_real_superset_p({1, 2}), {1, 2}, "{1, 2} is not a real superset of {1, 2}"),
    ],
)
def test_set_predicates_explain(predicate, value, reason):
    assert explain(predicate, value) == {"reason": reason, "result": False}
