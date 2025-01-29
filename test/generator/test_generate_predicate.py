import pytest
from more_itertools import take

from predicate import is_predicate_of_p
from predicate.all_predicate import AllPredicate
from predicate.any_predicate import AnyPredicate
from predicate.eq_predicate import EqPredicate
from predicate.ge_predicate import GePredicate
from predicate.generator.generate_predicate import (
    generate_all_predicates,
    generate_any_predicates,
    generate_predicate,
    generate_set_of_predicates,
)
from predicate.gt_predicate import GtPredicate
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.ne_predicate import NePredicate
from predicate.predicate import AndPredicate, NotPredicate, OrPredicate, XorPredicate
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import InPredicate, NotInPredicate

AMOUNT_TO_GENERATE = 100


@pytest.mark.parametrize("predicate_type", (AndPredicate, OrPredicate, XorPredicate))
@pytest.mark.parametrize("klass", (int, str, float))
def test_generate_and_predicate(predicate_type, klass):
    generator = generate_predicate(predicate_type, max_depth=2, klass=klass)
    predicates = take(AMOUNT_TO_GENERATE, generator)

    assert predicates

    is_klass_predicate = is_predicate_of_p(klass)

    for predicate in predicates:
        assert isinstance(predicate, predicate_type)
        assert is_klass_predicate(predicate)


@pytest.mark.parametrize("klass", (int, str, float))
def test_generate_not_predicate(klass):
    generator = generate_predicate(NotPredicate, max_depth=2, klass=klass)
    predicates = take(AMOUNT_TO_GENERATE, generator)

    assert predicates

    is_klass_predicate = is_predicate_of_p(klass)

    for predicate in predicates:
        assert isinstance(predicate, NotPredicate)
        assert is_klass_predicate(predicate)


@pytest.mark.parametrize(
    "predicate_type",
    (
        EqPredicate,
        GeLePredicate,
        GeLtPredicate,
        GePredicate,
        GtPredicate,
        GtLePredicate,
        GtLtPredicate,
        InPredicate,
        LePredicate,
        LtPredicate,
        NePredicate,
        NotInPredicate,
    ),
)
@pytest.mark.parametrize("klass", (int, str, float))
def test_generate_basic_predicate(predicate_type, klass):
    generator = generate_predicate(predicate_type, max_depth=1, klass=klass)
    predicates = take(AMOUNT_TO_GENERATE, generator)

    assert predicates

    is_klass_predicate = is_predicate_of_p(klass)

    for predicate in predicates:
        assert isinstance(predicate, predicate_type)
        assert is_klass_predicate(predicate)


@pytest.mark.parametrize(
    ("predicate_type", "generate_func"),
    [
        (AllPredicate, generate_all_predicates),
        (AnyPredicate, generate_any_predicates),
    ],
)
@pytest.mark.parametrize("klass", (int, str, float))
def test_generate_all_predicate(predicate_type, generate_func, klass):
    generator = generate_func(max_depth=2, klass=klass)

    predicates = take(AMOUNT_TO_GENERATE, generator)

    assert predicates

    is_klass_predicate = is_predicate_of_p(klass)

    for predicate in predicates:
        assert isinstance(predicate, predicate_type)
        assert is_klass_predicate(predicate)


@pytest.mark.parametrize("klass", (int,))
def test_generate_set_of_predicate(klass):
    predicate_type = SetOfPredicate
    generator = generate_set_of_predicates(max_depth=1, klass=klass)

    predicates = take(AMOUNT_TO_GENERATE, generator)

    assert predicates

    is_klass_predicate = is_predicate_of_p(klass)

    for predicate in predicates:
        assert isinstance(predicate, predicate_type)
        assert is_klass_predicate(predicate)
