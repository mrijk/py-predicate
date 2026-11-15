from hypothesis import given, settings
from hypothesis import strategies as st

from predicate import eq_p, ge_p, lt_p, optimize, to_json
from predicate.formatter.from_json import from_json
from predicate.integrations.hypothesis import predicates
from predicate.predicate import Predicate

domain = range(-8, 9)  # a little wider than the leaves of predicates()


@given(predicates())
def test_predicates_can_be_called_with_ints(predicate):
    assert isinstance(predicate, Predicate)
    assert all(isinstance(predicate(x), bool) for x in domain)


@settings(max_examples=300, deadline=None)
@given(predicates())
def test_optimize_keeps_the_meaning(predicate):
    optimized = optimize(predicate)
    assert all(predicate(x) == optimized(x) for x in domain)


@settings(max_examples=300, deadline=None)
@given(predicates(leaves=st.builds(eq_p, st.integers(-5, 5)) | st.builds(ge_p, st.integers(-5, 5)) | st.just(lt_p(0))))
def test_json_round_trip_keeps_the_meaning(predicate):
    restored = from_json(to_json(predicate))
    assert all(predicate(x) == restored(x) for x in domain)
