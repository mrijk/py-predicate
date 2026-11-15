import pytest
from hypothesis import find, given, settings

from predicate import (
    in_p,
    intersects_p,
    is_int_p,
    is_real_subset_p,
    is_real_superset_p,
    is_set_of_p,
    is_subset_p,
    is_superset_p,
)
from predicate.hypothesis import from_predicate
from predicate.integrations.hypothesis.helpers import sampled_from

predicates = {
    "is_subset_p": is_subset_p({1, 2, 3}),
    "is_real_subset_p": is_real_subset_p({1, 2, 3}),
    "is_superset_p": is_superset_p({1, 2, 3}),
    "is_real_superset_p": is_real_superset_p({1, 2, 3}),
    "intersects_p": intersects_p({1, 2, 3}),
    "strings": is_subset_p({"a", "b", "c"}),
    "strings superset": is_superset_p({"a", "b"}),
    "mixed types": is_superset_p({1, "a"}),
    "mixed types intersects": intersects_p({1, "a"}),
    "frozenset": is_subset_p(frozenset({1, 2})),
    "empty subset": is_subset_p(set()),
    "empty superset": is_superset_p(set()),
    "empty real superset": is_real_superset_p(set()),
    "single real subset": is_real_subset_p({1}),
    "set_of & subset": is_subset_p({1, 2, 3}) & is_set_of_p(is_int_p),
}


@pytest.mark.parametrize("predicate", predicates.values(), ids=predicates.keys())
def test_from_predicate_satisfies_set_predicate(predicate):
    @settings(max_examples=50)
    @given(from_predicate(predicate))
    def check(x):
        assert predicate(x)

    check()


@pytest.mark.parametrize("predicate", [is_real_subset_p(set()), intersects_p(set())], ids=repr)
def test_unsatisfiable_set_predicates_generate_nothing(predicate):
    assert from_predicate(predicate).is_empty


def collect(predicate, n=200):
    seen = set()

    @settings(max_examples=n, database=None)
    @given(from_predicate(predicate))
    def run(x):
        seen.add(frozenset(x))

    run()
    return seen


def test_subsets_vary_and_stay_inside_v():
    seen = collect(is_subset_p({1, 2, 3}))
    assert len(seen) > 4
    assert all(s <= {1, 2, 3} for s in seen)


def test_supersets_contain_v_and_add_extra_elements():
    seen = collect(is_superset_p({1, 2, 3}))
    assert all({1, 2, 3} <= s for s in seen)
    assert any(s > {1, 2, 3} for s in seen)


def test_real_supersets_are_strictly_bigger():
    assert all(s > {1, 2} for s in collect(is_real_superset_p({1, 2})))


def test_intersecting_sets_vary_beyond_v():
    seen = collect(intersects_p({1, 2, 3}))
    assert all(s & {1, 2, 3} for s in seen)
    assert any(s - {1, 2, 3} for s in seen)


def test_sampled_from_is_ordered_for_replay_and_handles_empty():
    assert find(sampled_from({"b", "c", "a"}), lambda x: True) == "a"
    assert sampled_from(set()).is_empty


def test_in_p_shrinks_to_the_first_value_in_stable_order():
    assert find(from_predicate(in_p({"b", "c", "a"})), lambda x: True) == "a"
