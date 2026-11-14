import pytest
from hypothesis import given, settings
from hypothesis.errors import FailedHealthCheck, Unsatisfiable

from predicate import (
    all_p,
    eq_p,
    ge_p,
    has_key_p,
    has_length_p,
    in_p,
    is_empty_p,
    is_int_p,
    is_list_of_p,
    is_not_empty_p,
    is_str_p,
    lt_p,
)
from predicate.hypothesis import from_predicate
from predicate.str_predicates import starts_with_p

predicates = {
    "has_length_p eq": has_length_p(eq_p(3)),
    "has_length_p range": has_length_p(ge_p(2) & lt_p(5)),
    "has_length_p in": has_length_p(in_p({2, 4})),
    "has_length_p lt": has_length_p(lt_p(2)),
    "has_length_p large": has_length_p(eq_p(80)),
    "is_empty_p": is_empty_p,
    "is_not_empty_p": is_not_empty_p,
    "has_key_p eq": has_key_p(eq_p("name")),
    "has_key_p starts_with": has_key_p(starts_with_p("_")),
    "has_key_p is_str": has_key_p(is_str_p),
    "has_key_p int keys": has_key_p(ge_p(0)),
    "has_key_p in": has_key_p(in_p({"a", "b"})),
    "length & list_of": has_length_p(eq_p(3)) & is_list_of_p(is_int_p),
    "list_of & length": is_list_of_p(is_int_p) & has_length_p(ge_p(1)),
    "all_p(has_key_p)": all_p(has_key_p(eq_p("id"))),
    "is_list_of_p(has_length_p)": is_list_of_p(has_length_p(eq_p(2))),
    "has_key_p & has_length_p": has_key_p(eq_p("a")) & has_length_p(ge_p(1)),
}


@pytest.mark.parametrize("predicate", predicates.values(), ids=predicates.keys())
def test_from_predicate_satisfies_predicate(predicate):
    @settings(max_examples=50)
    @given(from_predicate(predicate))
    def check(x):
        assert predicate(x)

    check()


def collect(predicate, measure, n=200):
    seen = set()

    @settings(max_examples=n, database=None)
    @given(from_predicate(predicate))
    def run(x):
        seen.add(measure(x))

    run()
    return seen


def test_all_lengths_that_satisfy_are_generated_and_no_others():
    assert collect(has_length_p(ge_p(2) & lt_p(5)), len) == {2, 3, 4}
    assert collect(has_length_p(lt_p(2)), len) == {0, 1}


def test_length_beyond_the_maximum_cannot_be_generated():
    @given(from_predicate(has_length_p(eq_p(500))))
    def check(x): ...

    with pytest.raises((Unsatisfiable, FailedHealthCheck)):
        check()


def test_has_key_generates_the_key_and_other_keys():
    sizes = collect(has_key_p(eq_p("name")), len)
    assert 1 in sizes and any(size > 1 for size in sizes)


def test_has_key_always_contains_a_matching_key():
    @settings(max_examples=100)
    @given(from_predicate(has_key_p(starts_with_p("_"))))
    def check(x):
        assert any(key.startswith("_") for key in x if isinstance(key, str))

    check()
