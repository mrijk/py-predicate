import pytest

from predicate import all_p, any_p, explain, ge_p, is_bool_p, is_int_p, is_list_of_p, is_predicate_of_p, le_p, lt_p
from predicate.predicate import Predicate
from predicate.standard_predicates import is_str_p


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


def test_is_predicate_repr():
    predicate = is_predicate_of_p(int)

    assert repr(predicate) == "is_predicate_of_p('int')"


@pytest.mark.skip("Fix me!")
@pytest.mark.parametrize("predicate", [all_p, any_p, is_list_of_p])
@pytest.mark.parametrize(
    ("klass", "valid", "invalid"),
    [
        (Predicate[int], is_int_p, is_str_p),
        (Predicate[str], is_str_p, is_bool_p),
    ],
)
def test_is_predicate_of_predicate_type(predicate, klass, valid, invalid):
    predicate_of = is_predicate_of_p(klass)

    assert not predicate_of(predicate(invalid))
    assert predicate_of(predicate(valid))


@pytest.mark.parametrize(("predicate", "klass"), [(~le_p(2), int), (ge_p("bar") & le_p("foo"), str)])
def test_is_predicate_of_type_composed(predicate, klass):
    predicate_of = is_predicate_of_p(klass)

    assert predicate_of(predicate)


def test_is_predicate_of_type_explain():
    predicate = is_predicate_of_p(int)

    expected = {"reason": "lt_p('foo') is not a predicate of type 'int'", "result": False}
    assert explain(predicate, lt_p("foo")) == expected


def test_is_predicate_of_type_explain_not_predicate():
    predicate = is_predicate_of_p(int)

    expected = {"reason": "Value `foo` is not a predicate", "result": False}
    assert explain(predicate, "foo") == expected
