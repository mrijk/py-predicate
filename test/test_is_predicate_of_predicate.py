import pytest

from predicate import lt_p
from predicate.standard_predicates import ge_p, is_predicate_of_p, le_p


@pytest.mark.parametrize(
    ("klass", "valid", "invalid"),
    [
        (float, 3.14, 3),
        (int, 2, "foo"),
        (str, "foo", 2),
        (bool, True, "foo"),
    ],
)
def test_is_predicate_of_type(klass, valid, invalid):
    predicate = is_predicate_of_p(klass)

    assert not predicate(lt_p(invalid))
    assert predicate(lt_p(valid))


@pytest.mark.parametrize(("predicate", "klass"), [(~le_p(2), int), (ge_p("bar") & le_p("foo"), str)])
def test_is_predicate_of_type_composed(predicate, klass):
    predicate_of = is_predicate_of_p(klass)

    assert predicate_of(predicate)
