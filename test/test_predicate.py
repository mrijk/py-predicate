from datetime import datetime
from uuid import uuid4

import pytest

from predicate import (
    always_false_p,
    eq_false_p,
    eq_true_p,
    is_bool_p,
    is_callable_p,
    is_complex_p,
    is_container_p,
    is_datetime_p,
    is_dict_p,
    is_hashable_p,
    is_int_p,
    is_iterable_p,
    is_list_p,
    is_predicate_p,
    is_range_p,
    is_set_p,
    is_str_p,
    is_tuple_p,
    is_uuid_p,
    zero_p,
)
from predicate.named_predicate import NamedPredicate
from predicate.predicate import Predicate
from predicate.standard_predicates import (
    is_iterable_of_p,
    is_single_or_iterable_of_p,
)


@pytest.mark.skip
def test_eq_true_p():
    assert eq_true_p(True)
    assert not eq_true_p(False)


@pytest.mark.skip
def test_eq_false_p():
    assert not eq_false_p(True)
    assert eq_false_p(False)


@pytest.mark.skip
def test_is_bool_p():
    assert not is_bool_p(0)
    assert not is_bool_p("1")

    assert is_bool_p(False)
    assert is_bool_p(True)


@pytest.mark.skip
def test_is_callable_p():
    assert not is_callable_p(None)

    def foo():
        pass

    assert is_callable_p(foo)

    assert is_callable_p(lambda x: x)

    predicate = always_false_p
    assert is_callable_p(predicate)


@pytest.mark.skip
def test_is_complex():
    assert not is_complex_p(1)

    assert is_complex_p(2 + 1j)


@pytest.mark.skip
def test_is_datetime_p():
    now = datetime.now()

    assert is_datetime_p(now)
    assert not is_datetime_p("foo")


@pytest.mark.skip
def test_is_int_p():
    assert not is_int_p(False)
    assert not is_int_p(None)
    assert not is_int_p("3")
    assert not is_int_p(3.0)

    assert is_int_p(3)


@pytest.mark.skip
def test_is_predicate_p():
    assert not is_predicate_p(None)
    assert is_predicate_p(always_false_p)


@pytest.mark.skip
def test_is_range_p():
    assert not is_range_p(None)
    assert is_range_p(range(10))


@pytest.mark.skip
def test_is_str_p():
    assert not is_str_p(None)
    assert not is_str_p(3)

    assert is_str_p("3")


@pytest.mark.skip
def test_is_dict_p():
    assert not is_dict_p(None)
    assert not is_dict_p({3})

    assert is_dict_p({})
    assert is_dict_p({"x": 3})


@pytest.mark.skip
def test_is_iterable_p():
    assert not is_iterable_p(1)

    assert is_iterable_p([])
    assert is_iterable_p(())
    assert is_iterable_p("foobar")
    assert is_iterable_p({1, 2, 3})
    assert is_iterable_p(range(5))


@pytest.mark.skip
def test_is_iterable_of_p():
    is_iterable_of_str = is_iterable_of_p(is_str_p)

    assert not is_iterable_of_str(None)
    assert not is_iterable_of_str([1])

    assert is_iterable_of_str([])
    assert is_iterable_of_str(["foo"])


@pytest.mark.skip
def test_is_single_or_iterable_of_p():
    is_single_or_iterable_of_str = is_single_or_iterable_of_p(is_str_p)

    assert not is_single_or_iterable_of_str(None)
    assert not is_single_or_iterable_of_str([1])

    assert is_single_or_iterable_of_str("foo")
    assert is_single_or_iterable_of_str([])
    assert is_single_or_iterable_of_str(["foo"])


@pytest.mark.skip
def test_is_list_p():
    assert not is_list_p(None)
    assert not is_list_p((3,))
    assert not is_list_p(3)

    assert is_list_p([])
    assert is_list_p([3])


@pytest.mark.skip
def test_is_set_p():
    assert not is_set_p(None)

    assert is_set_p(set())
    assert is_set_p({3})


@pytest.mark.skip
def test_is_tuple_p():
    assert not is_tuple_p(None)

    assert is_tuple_p((3,))


@pytest.mark.skip
def test_is_uuid_p():
    assert not is_uuid_p(None)

    assert is_uuid_p(uuid4())


@pytest.mark.skip
def test_base_predicate():
    p = Predicate()
    with pytest.raises(NotImplementedError):
        p(1)


@pytest.mark.skip
def test_named_predicate():
    p = NamedPredicate(name="p")
    q = NamedPredicate(name="q")

    assert not p(False)
    assert p != q


@pytest.mark.parametrize(
    "value",
    [
        set(),
        (),
        [],
        {"foo", "bar"},
    ],
)
@pytest.mark.skip
def test_is_container_p(value):
    assert is_container_p(value)


@pytest.mark.parametrize("value", [1, 3.14, True, "foo", datetime.now()])
@pytest.mark.skip
def test_is_hashable_p(value):
    assert is_hashable_p(value)


@pytest.mark.parametrize(
    "value",
    [
        {},
        {1, 2, 3},
    ],
)
@pytest.mark.skip
def test_is_not_hashable_p(value):
    assert not is_hashable_p(value)


@pytest.mark.skip
def test_zero_p():
    assert not zero_p(1)
    assert zero_p(0)


@pytest.mark.skip
def test_base_predicate_explain_failure():
    p = Predicate()
    with pytest.raises(NotImplementedError):
        p.explain_failure(1)


@pytest.mark.skip
def test_not_predicate_contains():
    assert is_int_p in ~(is_int_p & is_str_p)


@pytest.mark.skip
def test_xor_predicate_explain_failure():
    from predicate import explain, ge_p, le_p

    predicate = ge_p(2) ^ le_p(4)
    # x=3: both ge_p(2) and le_p(4) are True → XOR is False
    result = explain(predicate, 3)
    assert result["result"] is False
    assert "left" in result
    assert "right" in result


@pytest.mark.skip
def test_xor_predicate_contains():
    assert is_int_p in (is_int_p ^ is_str_p)


@pytest.mark.skip
def test_xor_p_factory():
    from predicate import ge_p
    from predicate.predicate import xor_p

    predicate = xor_p(ge_p(2), ge_p(4))
    assert predicate(2)
    assert predicate(3)
    assert not predicate(4)
    assert not predicate(1)
