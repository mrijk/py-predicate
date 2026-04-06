Standard predicates
===================

This section describes the predicates that are included in py-predicate.

.. include:: set_predicates.rst
.. include:: str_predicates.rst

all_p
-----

This predicate tests if for all elements in an Iterable, the enclosed predicate is True:

.. code-block:: python

    from predicate import all_p, is_int_p

    # Predicate to test if all items in an iterable are of type int
    all_int = all_p(is_int_p)

    assert all_int([1, 2, 3])
    assert not all_int([None, 2, 3])

The equivalent code without using predicates could be something like:

.. code-block:: python

    def all_int(iter: Iterable) -> bool:
        return all(isinstance(ele, int) for ele in iter)


always_false_p
--------------

This predicate ignores any arguments and always returns False:

.. code-block:: python

    from predicate import always_false_p

    assert not always_false_p(13)


This might be the result of an optimization.

always_p
--------

Synonym for always_true_p.


always_true_p
-------------

This predicate ignores any arguments and always returns True:

.. code-block:: python

    from predicate import always_true_p

    assert always_true_p(13)


This might be the result of an optimization.

any_p
-----

This predicate tests if for any element in an Iterable, the enclosed predicate is True:

.. code-block:: python

    from predicate import any_p, is_int_p

    # Predicate to test if any of the items in an iterable is of type int
    any_int = any_p(is_int_p)

    assert not any_int(())
    assert any_int((1, 2, 3))
    assert any_int([1, 2, 3])
    assert any_int([None, 2, 3])


count_p
-------

The count_p accepts two paramters. The ``predicate`` is evaluated and adds 1 to the count if True,
otherwise 0. The ``length_p`` evaluates the final count and is returned as the value of the
count_p itself.

In the next example we define a predicate that returns True if the number of elements in the
iterable that are greater or equal 1, is exactly 1.

.. code-block:: python

    from predicate import count_p, ge_p, eq_p

    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert predicate([1])
    assert not predicate([1, 3])


eq_false_p
----------

This predicates tests if the argument is False.

.. code-block:: python

    from predicate import eq_false_p

    assert eq_false_p(False)
    assert not eq_false_p(True)

Note that this tests for the exact boolean value False. If you want to test for falsy values, see:
:ref:`is_falsy_p`.

eq_p
----

This predicates tests for equality.

.. code-block:: python

    from predicate import eq_p

    eq_2 = eq_p(2)

    assert eq_2(2)
    assert not eq_2(3)

eq_true_p
----------

This predicates tests if the argument is True.

.. code-block:: python

    from predicate import eq_true_p

    assert not eq_true_p(False)
    assert eq_true_p(True)

Note that this tests for the exact boolean value True. If you want to test for falsy values, see:
:ref:`is_truthy_p`.

fn_p
----

This predicate can be used to wrap any (lambda) function:

.. code-block:: python

    from predicate import fn_p

    square_ge_2 = fn_p(lambda x: x * x >= 2)

    assert not square_ge_2(1)
    assert square_ge_2(2)

ge_p
----

This predicates tests for greater or equal a value.

.. code-block:: python

    from predicate import ge_p

    ge_2 = ge_p(2)

    assert ge_2(2)
    assert not ge_2(1)

gt_p
----

This predicates tests for greater than a value.

.. code-block:: python

    from predicate import gt_p

    gt_2 = gt_p(2)

    assert not gt_2(2)
    assert gt_2(3)

has_length_p
------------

This predicate tests the length of an iterable against another predicate.

.. code-block:: python

    from predicate import has_length_p, lt_p

    has_length_lt_2 = has_length_p(lt_p(2))

    assert not has_length_lt_2([1, 2, 3])
    assert has_length_lt_2({1})


implies_p
---------

This predicate tests if one predicate implies another one.

.. code-block:: python

    from predicate import implies_p, ge_p

    p = ge_p(2)
    q = ge_p(3)

    assert not implies(p, q)
    assert implies(q, p)


is_bool_p
---------

This predicate tests if the value is of type ``bool``. Only True if the value is either ``False`` or ``True``.

.. code-block:: python

    from predicate import is_bool_p

    assert is_bool_p(False)
    assert is_bool_p(True)


is_bytes_p
----------

This predicate tests if the value is of type ``bytes``.

.. code-block:: python

    from predicate import is_bytes_p

    assert not is_bytes_p("hello")
    assert not is_bytes_p(bytearray(b"hello"))
    assert is_bytes_p(b"hello")
    assert is_bytes_p(b"")

is_callable_p
-------------

This predicate tests if the value is of type ``Callable``.

.. code-block:: python

    from predicate import is_callable_p

    assert is_callable(is_callable)
    assert is_callable(lambda x: x)
    assert is_callable(str.upper)



is_close_p
----------

This predicate tests if a float value is approximately equal to a target, accounting for
floating-point rounding errors. It wraps :func:`math.isclose` with configurable ``rel_tol``
and ``abs_tol`` parameters.

.. code-block:: python

    from predicate import is_close_p

    predicate = is_close_p(1.0)

    assert predicate(1.0)
    assert predicate(1.0 + 1e-10)   # within default relative tolerance
    assert not predicate(1.1)

Use ``abs_tol`` when comparing values near zero:

.. code-block:: python

    from predicate import is_close_p

    near_zero = is_close_p(0.0, abs_tol=1e-6)

    assert near_zero(1e-7)
    assert not near_zero(1e-5)

is_complex_p
------------

This predicate tests if the value is of type ``complex``.

.. code-block:: python

    from predicate import is_complex_p

    assert not is_complex(1)
    assert is_complex(complex(1, 1))
    assert is_complex(1 + 1j)

is_container_p
--------------

This predicate tests if the value is of type ``Container``.

.. code-block:: python

    from predicate import is_container_p

    assert is_container_p((1, 2, 3))
    assert is_container_p([1, 2, 3])
    assert is_container_p({1, 2, 3})
    assert is_container_p({"one": 1, "two": 2, "three": 3})
    assert is_container_p("one")  # a string is also a container!


is_date_p
---------

This predicate tests if the value is of type ``date``.

Note that ``datetime`` is a subclass of ``date``, so ``datetime`` values also match.
If you need to distinguish, combine with ``~is_datetime_p``.

.. code-block:: python

    from datetime import date, datetime
    from predicate import is_date_p

    assert is_date_p(date.today())
    assert is_date_p(datetime.now())  # datetime is a subclass of date
    assert not is_date_p("2024-01-01")

is_datetime_p
-------------

This predicate tests if the value is of type ``datetime``.

.. code-block:: python

    from datetime import datetime
    from predicate import is_datetime_p

    assert is_datetime_p(datetime.now())

is_dict_p
---------

This predicate tests if the value is of type ``dict``.

.. code-block:: python

    from predicate import is_dict_p

    assert is_dict_p({"one": 1, "two": 2, "three": 3})



is_dict_of_p
------------

This predicate tests if the value is of type ``dict`` and the key and values match the predicates.

.. code-block:: python

    from predicate import is_dict_of_p, is_int_p, eq_p

    # test for dictionaries that have keys x and y. The values should be integers
    predicate = is_dict_of_p((eq_p("x"), is_int_p), (eq_p("y"), is_int_p))

    assert predicate({"x": 1, "y": 7})


is_empty_p
----------

This predicate tests if an iterable is empty.

.. code-block:: python

    from predicate import is_empty_p

    assert is_empty_p(())
    assert is_empty_p({})
    assert is_empty_p([])
    assert is_empty_p("")

.. _is_falsy_p:

is_falsy_p
----------

This predicate tests for falsy values, for example False, "", {}, [], 0, etc.

.. code-block:: python

    from predicate import is_falsy_p

    assert is_falsy_p(0)
    assert is_falsy_p({})

is_finite_p
-----------

This predicate tests if the value is a finite number (i.e. not infinite and not NaN).

.. code-block:: python

    import math
    from predicate import is_finite_p

    assert not is_finite_p(math.inf)
    assert not is_finite_p(math.nan)
    assert is_finite_p(42)

is_float_p
----------

This predicate tests if the value is of type ``float``.

.. code-block:: python

    from predicate import is_float_p

    assert not is_float_p(3)
    assert is_float_p(3.14)


is_frozenset_p
--------------

This predicate tests if the value is of type ``frozenset``.

.. code-block:: python

    from predicate import is_frozenset_p

    assert not is_frozenset_p({1, 2, 3})  # a set, not a frozenset
    assert is_frozenset_p(frozenset({1, 2, 3}))
    assert is_frozenset_p(frozenset())

is_hashable_p
-------------

This predicate tests if the value is hashable.

.. code-block:: python

    from predicate import is_hashable_p

    assert not is_hashable_p({})
    assert is_hashable_p("foo")

is_inf_p
--------

This predicate tests if the value is infinite.

.. code-block:: python

    import math
    from predicate import is_inf_p

    assert not is_inf_p(3)
    assert is_inf_p(math.inf)

is_instance_p
-------------

This predicate tests if the value is an instance of one or more given classes.

.. code-block:: python

    from predicate import is_instance_p

    is_int_or_str = is_instance_p(int, str)

    assert is_int_or_str(42)
    assert is_int_or_str("hello")
    assert not is_int_or_str(3.14)

is_int_p
--------

This predicate tests if the value is of type ``int``.

.. code-block:: python

    from predicate import is_int_p

    assert not is_int_p(3.14)
    assert is_int_p(3)


is_iterable_of_p
----------------

This predicate tests if the value is an ``Iterable`` and all its elements satisfy the given predicate.

.. code-block:: python

    from predicate import is_iterable_of_p, is_int_p

    all_ints = is_iterable_of_p(is_int_p)

    assert all_ints([1, 2, 3])
    assert all_ints((1,))
    assert not all_ints([1, "two", 3])

is_iterable_p
-------------

This predicate tests if the value is of type ``Iterable``.

.. code-block:: python

    from predicate import is_iterable_p

    assert is_iterable_p([1, 2, 3])
    assert is_iterable_p("hello")
    assert not is_iterable_p(42)

is_list_of_p
------------

This predicate predicate tests if the value if a list, where all items in the list conform to
a given predicate.

.. code-block:: python

    from predicate import is_list_of_p, is_str_p

    is_list_of_str = is_list_of_p(is_str_p)

    assert not is_list_of_str(["one", "two", 3])
    assert is_list_of_str(["foo"])


is_list_p
---------

This predicate tests if the value is of type ``list``.

.. code-block:: python

    from predicate import is_list_p

    assert not is_list_p({1, 2, 3})
    assert is_list_p([1, 2, 3])

is_mapping_p
------------

This predicate tests if the value is a ``Mapping`` (i.e. any dict-like type).

.. code-block:: python

    from collections import OrderedDict
    from predicate import is_mapping_p

    assert is_mapping_p({"key": "value"})
    assert is_mapping_p(OrderedDict())
    assert not is_mapping_p([("key", "value")])

is_nan_p
--------

This predicate tests if the value is ``NaN`` (not a number).

.. code-block:: python

    import math
    from predicate import is_nan_p

    assert not is_nan_p(1)
    assert is_nan_p(math.nan)



is_none_p
---------

This predicate tests if the value is ``None``.

.. code-block:: python

    from predicate import is_none_p

    assert not is_none_p(13)
    assert is_none_p(None)


is_not_none_p
-------------

This predicate tests if the value is not ``None``.

.. code-block:: python

    from predicate import is_not_none_p

    assert not is_not_none_p(None)
    assert is_not_none_p(13)

is_number_p
-----------

This predicate tests if the value is a number (``int``, ``float``, or ``complex``).
``bool`` values are excluded, consistent with how ``is_int_p`` works.

.. code-block:: python

    from predicate import is_number_p

    assert is_number_p(42)
    assert is_number_p(3.14)
    assert is_number_p(1 + 2j)
    assert not is_number_p(True)  # bool is excluded
    assert not is_number_p("42")

is_path_p
---------

This predicate tests if the value is a ``pathlib`` path.
Matches ``Path``, ``PurePosixPath``, ``PureWindowsPath``, and any other ``PurePath`` subclass.

.. code-block:: python

    from pathlib import Path, PurePosixPath
    from predicate import is_path_p

    assert is_path_p(Path("/tmp/file.txt"))
    assert is_path_p(PurePosixPath("/etc/hosts"))
    assert not is_path_p("/tmp/file.txt")  # a plain string is not a path

is_predicate_p
--------------

This predicate tests if the value is of type ``Predicate``.

.. code-block:: python

    from predicate import is_predicate_p, eq_p

    assert is_predicate_p(eq_p(1))
    assert not is_predicate_p(42)

is_range_p
----------

This predicate tests if value is a range.

.. code-block:: python

    from predicate import is_range_p

    assert not is_range_p(0)
    assert is_range_p(range(5))

is_sequence_p
-------------

This predicate tests if the value is a ``Sequence`` (list, tuple, str, bytes, range, etc.).
Note that ``dict`` and ``set`` are *not* sequences.

.. code-block:: python

    from predicate import is_sequence_p

    assert is_sequence_p([1, 2, 3])
    assert is_sequence_p((1, 2))
    assert is_sequence_p("hello")  # str is a sequence
    assert is_sequence_p(range(5))
    assert not is_sequence_p({1, 2, 3})
    assert not is_sequence_p({"key": "value"})

is_set_of_p
-----------

This predicate predicate tests if the value if a set, where all items in the set conform to
a given predicate.

.. code-block:: python

    from predicate import is_set_of_p, is_str_p

    is_set_of_str = is_set_of_p(is_str_p)

    assert not is_set_of_str({"one", "two", 3})
    assert is_set_of_str({"foo"})


is_set_p
--------

This predicate tests if the value is of type ``set``.

.. code-block:: python

    from predicate import is_set_p

    assert is_set_p({1, 2, 3})
    assert not is_set_p([1, 2, 3])
    assert not is_set_p(frozenset({1, 2, 3}))

is_str_p
--------

This predicate tests if the value is of type ``str``.

.. code-block:: python

    from predicate import is_str_p

    assert not is_str_p(3.14)
    assert is_str_p("foo")

is_subclass_p
-------------

This predicate tests if a class is a subclass of the given class.

.. code-block:: python

    from predicate import is_subclass_p

    is_int_subclass = is_subclass_p(int)

    assert is_int_subclass(bool)  # bool is a subclass of int
    assert not is_int_subclass(str)


is_time_p
---------

This predicate tests if the value is of type ``datetime.time``.

.. code-block:: python

    from datetime import time
    from predicate import is_time_p

    assert is_time_p(time(12, 30))
    assert is_time_p(time(0, 0, 0))
    assert not is_time_p("12:30")

is_timedelta_p
--------------

This predicate tests if the value is of type ``datetime.timedelta``.

.. code-block:: python

    from datetime import timedelta
    from predicate import is_timedelta_p

    assert is_timedelta_p(timedelta(days=1))
    assert is_timedelta_p(timedelta(seconds=3600))
    assert not is_timedelta_p(3600)

.. _is_truthy_p:

is_truthy_p
-----------

This predicate tests for truthy values, for example True, "foo", {"foo"}, [1], 13, etc.

.. code-block:: python

    from predicate import is_truthy_p

    assert is_truthy_p(1)
    assert is_truthy_p({"foo"})

is_tuple_of_p
-------------

This predicate tests if the value is a tuple of a specific structure, where each element matches
the corresponding predicate.

.. code-block:: python

    from predicate import is_tuple_of_p, is_int_p, is_str_p

    is_int_str_pair = is_tuple_of_p(is_int_p, is_str_p)

    assert is_int_str_pair((1, "hello"))
    assert not is_int_str_pair((1, 2))
    assert not is_int_str_pair((1, "hello", "extra"))

is_tuple_p
----------

This predicate tests if the value is of type ``tuple``.

.. code-block:: python

    from predicate import is_tuple_p

    assert is_tuple_p((1, 2, 3))
    assert is_tuple_p(())
    assert not is_tuple_p([1, 2, 3])

is_uuid_p
---------

This predicate tests if the value is of type ``UUID``.

.. code-block:: python

    from uuid import UUID, uuid4
    from predicate import is_uuid_p

    assert is_uuid_p(uuid4())
    assert is_uuid_p(UUID("12345678-1234-5678-1234-567812345678"))
    assert not is_uuid_p("12345678-1234-5678-1234-567812345678")

juxt_p
------

This predicate applies multiple predicates to the same value, collects the boolean results, and then evaluates
those results with an ``evaluate`` predicate.

In the simplest case, check if a value satisfies exactly two of four predicates:

.. code-block:: python

    from predicate import count_p, eq_p, is_int_p, is_str_p, juxt_p

    p1 = is_int_p
    p2 = is_str_p
    p3 = eq_p(2)
    p4 = eq_p("foo")

    two_true = count_p(predicate=eq_p(True), length_p=eq_p(2))

    predicate = juxt_p(p1, p2, p3, p4, evaluate=two_true)

    assert predicate(2)  # is_int_p and eq_p(2) are both True
    assert predicate("foo")  # is_str_p and eq_p("foo") are both True
    assert not predicate(1)  # only is_int_p is True

``juxt_p`` also works with predicates that themselves accept iterables, enabling compound checks on the
same input in a single predicate:

.. code-block:: python

    from predicate import all_p, count_p, eq_p, exactly_one_p, is_int_p, juxt_p

    all_int = all_p(is_int_p)
    three_zeros = count_p(predicate=eq_p(0), length_p=eq_p(3))
    one_true = exactly_one_p(predicate=eq_p(True))

    predicate = juxt_p(all_int, three_zeros, evaluate=one_true)

    assert predicate([1, 2, 3, 4])  # all ints, not 3 zeros → exactly one True
    assert not predicate(
        [1, 0, 2, 0, 3, 0]
    )  # all ints and 3 zeros → both True, so one_true fails


le_p
----

This predicates tests for less than or equal a value.

.. code-block:: python

    from predicate import le_p

    le_2 = le_p(2)

    assert le_2(2)
    assert not le_2(3)

lt_p
----

This predicates tests for less than a value.

.. code-block:: python

    from predicate import lt_p

    lt_2 = lt_p(2)

    assert not lt_2(2)
    assert lt_2(1)

ne_p
----

This predicate tests for non equality


.. code-block:: python

    from predicate import ne_p

    ne_2 = ne_p(2)

    assert not ne_2(2)
    assert ne_2(3)


raises_p
--------

This predicate tests if a callable (thunk) raises an exception when called.
Returns True if calling the thunk raises any exception, False otherwise.
Both synchronous and async callables are supported.

.. code-block:: python

    from predicate import raises_p

    assert raises_p(lambda: 1 / 0)
    assert raises_p(lambda: int("x"))
    assert not raises_p(lambda: 1)

Async functions are also supported:

.. code-block:: python

    async def fetch():
        raise ConnectionError("unreachable")

    async def ok():
        return 42

    assert raises_p(fetch)
    assert not raises_p(ok)

raises_exception_p
------------------

This predicate tests if a callable raises a specific exception type when called.
Returns True only if the exact exception type (or a subclass of it) is raised.
Both synchronous and async callables are supported.

.. code-block:: python

    from predicate import raises_exception_p

    assert raises_exception_p(ValueError)(lambda: int("x"))
    assert raises_exception_p(Exception)(lambda: 1 / 0)    # ZeroDivisionError is a subclass of Exception
    assert not raises_exception_p(ValueError)(lambda: 1 / 0)  # wrong exception type
    assert not raises_exception_p(ValueError)(lambda: 1)       # no exception raised

    async def async_value_error():
        raise ValueError("bad input")

    assert raises_exception_p(ValueError)(async_value_error)

tee_p
-----

Predicate that always returns True, but is useful for handling side-effects.

.. code-block:: python

    from predicate import all_p, lt_p, tee_p

    log = tee_p(print)

    all_lt_2 = all_p(log | lt_p(2))


zero_p
------

Returns True of the value is zero, otherwise False.

.. code-block:: python

    from predicate import zero_p

    assert zero_p(0)
